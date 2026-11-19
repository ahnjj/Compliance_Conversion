"""Transport adapters for the policy-decision harness."""

import json
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class ModelRequestError(RuntimeError):
    """The backend could not complete a model request."""


@dataclass
class ModelResponse:
    text: str
    metadata: dict


def post_json(url, payload, headers=None):
    request = Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", **(headers or {})},
    )
    try:
        with urlopen(request, timeout=180) as response:
            return json.load(response)
    except HTTPError as error:
        with error:
            detail = ""
            try:
                code = json.load(error).get("error", {}).get("code")
                if isinstance(code, str) and code.isidentifier() and len(code) <= 64:
                    detail = f" ({code})"
            except (ValueError, TypeError, AttributeError, OSError):
                pass
            raise ModelRequestError(f"HTTP {error.code}: {error.reason}{detail}") from error
    except (URLError, TimeoutError, OSError, ValueError) as error:
        raise ModelRequestError(str(error)) from error


class OllamaAdapter:
    backend = "ollama"
    default_model = "qwen3.5:9b"
    supported_models = (
        default_model,
        "mistral:7b-instruct-v0.3-q4_K_M",
        "llama3.1:8b",
        "gemma3:12b",
    )

    def __init__(self, model_id=default_model):
        self.model_id = model_id

    def generate(self, messages, schema):
        payload = {
            "model": self.model_id,
            "messages": messages,
            "stream": False,
            "format": schema,
            "options": {"temperature": 0, "num_ctx": 2048, "num_predict": 128},
        }
        if self.model_id == self.default_model:
            payload["think"] = False
        body = post_json("http://127.0.0.1:11434/api/chat", payload)
        try:
            content = body["message"]["content"]
        except (KeyError, TypeError) as error:
            raise ModelRequestError("Ollama returned an invalid chat response.") from error
        if content is not None and not isinstance(content, str):
            raise ModelRequestError("Ollama returned non-text chat content.")
        return ModelResponse(content or "", {
            "served_model_id": body.get("model"),
            "finish_reason": body.get("done_reason"),
            "usage": {
                "prompt_tokens": body.get("prompt_eval_count"),
                "completion_tokens": body.get("eval_count"),
            },
        })


class ChatCompletionsAdapter:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self, messages, schema):
        body = post_json(
            self.endpoint,
            {
                "model": self.model_id,
                "messages": messages,
                "stream": False,
                "reasoning_effort": "none",
                **self.request_options,
                "response_format": {
                    "type": "json_schema",
                    "json_schema": {"name": "policy_decision", "strict": True, "schema": schema},
                },
            },
            {"Authorization": f"Bearer {self.api_key}"},
        )
        try:
            choice = body["choices"][0]
            content = choice["message"].get("content")
        except (KeyError, IndexError, TypeError, AttributeError) as error:
            raise ModelRequestError(f"{self.backend} returned an invalid chat completion.") from error
        if content is not None and not isinstance(content, str):
            raise ModelRequestError(f"{self.backend} returned non-text chat content.")
        return ModelResponse(content or "", {
            "served_model_id": body.get("model"),
            "finish_reason": choice.get("finish_reason"),
            "usage": body.get("usage"),
            "request_id": body.get("id"),
        })


class UpstageAdapter(ChatCompletionsAdapter):
    backend = "upstage"
    model_id = "solar-mini4"
    endpoint = "https://api.upstage.ai/v1/chat/completions"
    request_options = {"temperature": 0, "max_tokens": 128}


class OpenAIAdapter(ChatCompletionsAdapter):
    backend = "openai"
    model_id = "gpt-6-luna"
    endpoint = "https://api.openai.com/v1/chat/completions"
    request_options = {"max_completion_tokens": 128, "store": False}

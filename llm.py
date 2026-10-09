
import requests

MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://localhost:11434/api/chat"


def generate_response(prompt, temperature=0.2, max_tokens=200):
    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful college tutor. Answer clearly and briefly."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "keep_alive": "10m",
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
            "num_ctx": 2048
        }
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=data,
            timeout=(10, 600)
        )
        response.raise_for_status()
        return response.json()["message"]["content"]

    except requests.exceptions.ConnectTimeout:
        raise RuntimeError(
            "Cannot connect to Ollama. Check whether Ollama is running."
        )
    except requests.exceptions.ReadTimeout:
        raise RuntimeError(
            "Qwen is taking too long. Test it directly using "
            "'ollama run qwen2.5:3b'. Your computer may not have "
            "enough resources to run this model efficiently."
        )
    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Ollama is not responding. Open Ollama and try again."
        )
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(f"Ollama request failed: {exc}")

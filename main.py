import os
import argparse

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")
    client = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = api_key,
    )
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages = [
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ]
    )
    if response.usage is None:
        raise RuntimeError("failed API request")
    print(f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

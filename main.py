import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

def main():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        print("Error: OPENROUTER_API_KEY is not set in the environment variables.")
        return
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    parser = argparse.ArgumentParser(description="Chat with OpenRouter API")
    parser.add_argument("user_prompt", type=str, help="User prompt to send to the OpenRouter API")
    args = parser.parse_args()
    messages = [
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    if response.usage is not None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("Response usage is None. Unable to retrieve token usage information.")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

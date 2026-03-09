import argparse
import os

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Ghinton Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except Exception:
        raise RuntimeError("API key is not found")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt,
    )
    print(f"User prompt: {args.user_prompt}")
    if response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()

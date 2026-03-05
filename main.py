import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
    except Exception:
        raise RuntimeError("API key is not found")
    client = genai.Client(api_key=api_key)
    prompt_text = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_text,
    )
    print(f"User prompt: {prompt_text}")
    if response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response: {response.text}")


if __name__ == "__main__":
    main()

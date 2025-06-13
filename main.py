import os, sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main(): 
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = sys.argv[1:]
    
    if len(sys.argv) < 2:
        print("not enough arguments") 
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )

    if verbose: 
        print(f"User prompt: {user_prompt}")
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print(response.text)

if __name__ == "__main__": 
    main()


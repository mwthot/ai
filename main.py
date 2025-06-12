import os, sys
from google import genai
from dotenv import load_dotenv

def main(): 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) < 2:
        print("not enough arguments") 
        sys.exit(1)
    
    else:  
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=sys.argv[1]
        )

        print(response.text)

        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

if __name__ == "__main__": 
    main()


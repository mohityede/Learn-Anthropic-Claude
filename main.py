from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = Anthropic(
    api_key=os.getenv("LITELLM_MASTER_KEY"),
    base_url="http://localhost:4000"
)

def test_llm_call(message):
    response = client.messages.create(
        model="gemini",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    print(response.content[0].text)

def main():
    print("Hello from learn-anthropic-claude!")
    test_llm_call("Explain vector databases in one sentence")
    


if __name__ == "__main__":
    main()


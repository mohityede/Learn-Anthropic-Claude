from anthropic import Anthropic

client = Anthropic(
    api_key="sk-1234",
    base_url="http://localhost:4000"
)

def main():
    print("Hello from learn-anthropic-claude!")
    response = client.messages.create(
        model="local",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": "Explain vector databases in one sentence"
            }
        ]
    )

    print(response.content[0].text)


if __name__ == "__main__":
    main()


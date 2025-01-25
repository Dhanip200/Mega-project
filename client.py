from openai import OpenAI
client = OpenAI(api_key="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")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named jarvis."},
        {
            "role": "user",
            "content": "what is coding?"
        }
    ]
)

print(completion.choices[0].message.content)
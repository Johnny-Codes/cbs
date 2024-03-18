import os
from openai import OpenAI
from typing import List

models = {"3.5-turbo": "gpt-3.5-turbo"}


def set_openai_client():
    api_key = os.environ.get("OEPNAI_API_KEY")
    return OpenAI(api_key=api_key)


def get_product_description_from_text(text: str):
    """
    text: A description of the coin
    can be title or description
    """
    messages = [
        {
            "role": "system",
            "content": "You are a numismatic expert. You are writing a product description for this coin.",
        },
    ]
    messages.append(
        {
            "role": "user",
            "content": text,
        }
    )
    print("messages", messages)
    client = set_openai_client()
    print("client", client)
    completion = client.chat.completions.create(
        model=models["3.5-turbo"],
        messages=messages,
    )
    print("completion.choices[0].message", completion.choices[0].message)
    return completion.choices[0].message.content


def get_product_description_from_photos(files: List[str]):
    """
    files: List of urls to images of coins
    """
    client = set_openai_client()
    content = [
        {
            "type": "text",
            "text": "Take your time and describe the look, appearance, strike, details, luster, and condition of this coin for a product description. Don't provide any financial or investment advice. The more you describe the details of this specific coins appearance the more I'll tip you. Paragraph form.",
        }
    ]

    for file in files:
        print("file", file)
        content.append(
            {
                "type": "image_url",
                "image_url": file,
            }
        )
    print("content", content)
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        max_tokens=600,
    )
    print(response.choices[0])

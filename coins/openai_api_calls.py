from typing import List
from openai import OpenAI
import asyncio


models = {"3.5-turbo": "gpt-3.5-turbo-1106"}


def set_openai_client(api_key: str):
    return OpenAI(api_key=api_key)


async def get_product_description_from_images(api_key: str, files: List[str]):
    client = set_openai_client(api_key=api_key)

    messages = [
        {
            "type": "text",
            "text": "Take your time and describe the look, appearance, strike, details, luster, and condition of this coin for a product description. Don't provide any financial or investment advice. The more you describe the details of this specific coins appearance the more I'll tip you. Paragraph form.",
        }
    ]

    for file in files:
        messages.append(
            {
                "type": "image_url",
                "image_url": file,
            }
        )

    def process_images():
        print("print processing images")
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": messages,
                },
            ],
            max_tokens=600,
            temperature=0.5,
        )
        content = response.choices[0].message.content
        print("print content", content)
        return {"response": content}

    task = asyncio.create_task(process_images())
    return await task


async def get_product_description_from_text(api_key: str, text: str):
    client = set_openai_client(api_key=api_key)
    print("client", client)

    async def process_text():
        response = client.chat.completions.create(
            model=models["3.5-turbo"],
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional coin grader. Make a coin description for this coin.",
                },
                {"role": "user", "content": text},
            ],
            max_tokens=600,
            temperature=0.5,
        )
        content = response.choices[0].message.content
        return {"response": content}

    task = asyncio.create_task(process_text())
    print("task", task)
    return await task

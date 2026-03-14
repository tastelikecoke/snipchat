from snippingtool import SnippingTool
from ollama import chat
from ollama import AsyncClient
from ollama import ChatResponse
import time
import pydirectinput
import asyncio
import sys

def delete_last_line():
    "Deletes the last line in the STDOUT"
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

async def countTime():
    seconds = 0
    print(f"{seconds} second(s) passed")
    while True:
        await asyncio.sleep(0.5)
        delete_last_line()
        print(f"{seconds} second(s) passed")
        seconds += 0.5

async def main():
    snipping = SnippingTool()
    image, bounding_box = snipping.capture()
    image.save('./my_screenshot3.png')

    client = AsyncClient()
    task = asyncio.create_task(countTime())
    response = await client.chat(
        model="qwen3-vl:2b",
        messages=[{
            "role": "user",
    #        "content": "Give all the text in the image in json format.",
            "content": "Give all the text in the image in plaintext.",
            "images": [
                "./my_screenshot3.png"
            ]
        }],
    )
    task.cancel()
    print("thinking for " + str(response.total_duration /1000000000) + " seconds")
    print(response['message']['content'])

asyncio.run(main())
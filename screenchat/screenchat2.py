from snippingtool import SnippingTool
from ollama import chat
from ollama import ChatResponse
import time
import pydirectinput

snipping = SnippingTool()
image, bounding_box = snipping.capture()
image.save('./my_screenshot3.png')

response: ChatResponse = chat(
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
print("thinking for " + str(response.total_duration /1000000000) + " seconds")
print(response.message.content)
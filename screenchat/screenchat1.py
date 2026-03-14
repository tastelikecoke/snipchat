import pyautogui
from ollama import chat
from ollama import ChatResponse
import time
import pydirectinput

while True:
    question = input("what is your question?")
    print("Go to the window you want to show.")
    time.sleep(5)
    print("checking screen.")
    im1 = pyautogui.screenshot('./my_screenshot1.png')

    response: ChatResponse = chat(model="qwen3-vl:2b", messages=[
        {
            "role": "user",
            "content": question,
            "images": [
                "./my_screenshot1.png"
            ]
        }
    ])

    print(response.message.content)
    print("Hope this response satisfies you.")
    time.sleep(2)
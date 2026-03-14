import pyautogui
from ollama import chat
from ollama import ChatResponse
import time
import pydirectinput

# Sleep for 2 seconds


while True:
    print("checking screen.")
    im1 = pyautogui.screenshot('./my_screenshot2.png')

    response: ChatResponse = chat(model="qwen3-vl:2b", messages=[
        {
            "role": "user",
            "content": "Are there dialogue choices on the bottom right of this screenshot of a game? Ignore the A or ESC on top. Answer only with yes or no.",
            "images": [
                "./my_screenshot2.png"
            ]
        }
    ])

    print(response.message.content)
    if (response.message.content == "yes" or response.message.content == "yes." or response.message.content == "Yes.") :
        print("Choice detected. pressing 1.")
        pydirectinput.press('1')

    print("waiting for next visuals.")
    time.sleep(2)
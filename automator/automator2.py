import pyautogui
from ollama import chat
from ollama import ChatResponse
import time
import pydirectinput
# Sleep for 2 seconds


while True:
    print("checking screen.")
    im1 = pyautogui.screenshot('./my_screenshot22.png')

    response: ChatResponse = chat(model="qwen3-vl:2b", messages=[
        {
            "role": "user",
            "content": "Is there a Click to continue in the screen? Answer only with yes or no.",
            "images": [
                "./my_screenshot22.png"
            ]
        }
    ])

    print(response.message.content)
    if (response.message.content == "yes" or response.message.content == "yes." or response.message.content == "Yes.") :
        print("Continue detected.")
        time.sleep(1)
        print("Clicking.")
        pydirectinput.click()

    print("waiting for next visuals.")
    time.sleep(2)
import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/bot253609155:AAGCp5I5uJiwZkqkyCVEatH3b8vi3RYxuY8/getUpdates")
    d = res.json()

    for elem in d["result"]:
        text = elem["message"]["text"]
        ans = handle_message(text)

        chat_id = elem["message"]["chat"]["id"]

        requests.post("https://api.telegram.org/bot253609155:AAGCp5I5uJiwZkqkyCVEatH3b8vi3RYxuY8/sendMessage", params={ "chat_id": chat_id, "text": ans } )

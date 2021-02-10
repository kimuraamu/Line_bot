from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApiキー
handler = WebhookHandlerキー

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if (event.message.text == "おはよう"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"クルックー"))

    elif (event.message.text == "こんにちは"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"はくちゃん、はくちゃん"))

    elif (event.message.text == "ハクー"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"はくー、はくちゃん"))

    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"キュキュッ"))


if __name__ == "__main__":
    app.run()

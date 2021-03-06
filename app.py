from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('qYQhozjGqOEA9aCh9WFo5IGXlHbuPoX6HTQX98QB9UxOhZdtfidjNzNjYQSwYLAkkxWFSBOW/uPIst/skNpZtIaF3drrcWUdf49HMPp8Z9B7C0S60Qe7pT+awrMDe+Li8RcFTI3nZOHwM/oWqvCskFGUYhWQfeY8sLGRXgo3xvw=
')
# Channel Secret
handler = WebhookHandler('077515768e6b7dead068b17e3f2b9bc6')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = ImageSendMessage(
        original_content_url='https://cadtc.com.tw/images/section02course02.jpg',
        preview_image_url='https://www.cadtc.com.tw/m4/images/20201224arm_mainbanner.jpg'
        )
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

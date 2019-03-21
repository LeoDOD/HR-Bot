import os
import time
import requests
import json
from slackclient import SlackClient
from flask import Flask, request, make_response, Response

app = Flask(__name__)

# Your app's Slack bot user token
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]

# Slack client for Web API requests
slack_client = SlackClient(SLACK_BOT_TOKEN)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    print(request.form)
    message = slack_client.api_call(
        "chat.postMessage",
        channel=request.form['channel_id'],
        text="Hi! I'm HR Bot",
        attachments=[
            {
                "text": "Amanda's worse Nightmare :slightly_smiling_face:"
            }
        ]
    )
    print(message)
    return make_response("", 200)


@app.route('/phrasing', methods=["POST", "GET"])
def phrasing():
    print(request.form)
    r = requests.get(
        f'https://api.giphy.com/v1/gifs/random?api_key={os.environ["GIPHY_BOT_TOKEN"]}&tag=Archer-Phrasing&rating=G')
    phrasing_gif= json.loads(r.content)
    message = slack_client.api_call(
        "chat.postMessage",
        channel=request.form['channel_id'],
        text=f"<{phrasing_gif['data']['url']}|Phrasing>"
    )
    print(message)
    return make_response("", 200)


if __name__ == '__main__':
    app.run()

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sos un asistente claro, breve y copado."},
            {"role": "user", "content": incoming_msg}
        ]
    )

    reply = response.choices[0].message.content

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)
    
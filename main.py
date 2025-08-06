from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.api_route("/webhook", methods=["GET", "POST"])
async def webhook(request: Request):
    return PlainTextResponse("say=שלום וברוך הבא לקו בינה, איך אפשר לעזור?")

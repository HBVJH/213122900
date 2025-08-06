from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "הקו מדבר!"}

@app.api_route("/webhook", methods=["GET", "POST"])
async def webhook(request: Request):
    if request.method == "GET":
        return PlainTextResponse("שלום וברוך הבא לקו בינה, איך אפשר לעזור?")
    elif request.method == "POST":
        try:
            data = await request.json()
            user_text = data.get("text", "")
        except:
            user_text = ""
        return PlainTextResponse("שלום וברוך הבא לקו בינה, איך אפשר לעזור?")

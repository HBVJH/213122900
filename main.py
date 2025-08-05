from fastapi import FastAPI, Request
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "הקו מדבר!"}
@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        user_text = data.get("text", "")
    except:
        user_text = ""
    return {"text": "שלום וברוך הבא לקו בינה, איך אפשר לעזור?"}
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
app = FastAPI()
@app.post("/webhook")
async def webhook():
    return PlainTextResponse("שלום וברוך הבא לקו בינה, איך אפשר לעזור?")
@app.post("/")
@app.post("/webhook")
async def handle_post(request: Request):
    data = await request.json()
    return {"message": "התקבל"}

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "הקו מדבר!"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        user_text = data.get("text", "")
    except:
        user_text = ""
    
    # כאן אפשר להכניס את העיבוד של הטקסט בעתיד

    return PlainTextResponse("שלום וברוך הבא לקו בינה, איך אפשר לעזור?")

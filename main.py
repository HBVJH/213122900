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

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "הקו מדבר!"}

@app.post("/webhook")
async def webhook(request: Request):
    return PlainTextResponse("שלום וברוך הבא לקו בינה, איך אפשר לעזור?")

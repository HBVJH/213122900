from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
app = FastAPI()
# קריאה לבדיקה ידנית
@app.get("/")
def read_root():
    return {"message": "הקו מדבר!"}
# תמיכה גם ב-GET וגם ב-POST עבור ימות
@app.api_route("/webhook", methods=["GET", "POST"])
async def webhook(request: Request):
    if request.method == "GET":
        return PlainTextResponse("שלום וברוך הבא לקו בינה, איך אפשר לעזור?")
    if request.method == "POST":
        try:
            data = await request.json()
            user_text = data.get("text", "")
        except:
            user_text = ""
        return {"text": "שלום וברוך הבא לקו בינה, איך אפשר לעזור?"}

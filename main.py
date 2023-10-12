from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="static_css")
app.mount("/js", StaticFiles(directory="js"), name="static_js")


@app.get("/", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return FileResponse("page/login.html")


@app.post("/process_login")
async def process_login(username: str = Form(...), password: str = Form(...)):
    # Here, you can perform authentication and other logic.
    # Replace this with your actual authentication code.
    if username == 'name' and password == 'pass':
        return FileResponse("page/channel.html")
    else:
        raise HTTPException(status_code=401, detail="Login failed")


@app.get("/meeting", response_class=HTMLResponse)
async def get_meeting_page(request: Request):
    return FileResponse("page/meeting.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

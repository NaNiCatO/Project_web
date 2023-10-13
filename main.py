from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import json

app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="static_css")
app.mount("/js", StaticFiles(directory="js"), name="static_js")



#______________________home______________________
@app.get("/", response_class=HTMLResponse)
@app.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return FileResponse("page/login.html")



#______________________login______________________
@app.post("/process_login")
async def process_login(username: str = Form(...), password: str = Form(...)):
    # Check if the username and password are correct
    user_data_file = os.path.join(data_dir, f"{username}.json")
    if os.path.exists(user_data_file):
        with open(user_data_file, "r") as file:
            user_data = json.load(file)
        if password == user_data["password"]:
            return FileResponse("page/meeting.html")
        else:
            raise HTTPException(status_code=401, detail="Login failed")


#______________________register______________________
data_dir = "user_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


@app.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return FileResponse("page/register.html")


@app.post("/process_register")
async def process_register(email: str = Form(...), username: str = Form(...), password: str = Form(...)):
    user_data = {
        "email": email,
        "username": username,
        "password": password
    }

    # Store user registration data in a JSON file
    user_data_file = os.path.join(data_dir, f"{username}.json")
    with open(user_data_file, "w") as file:
        json.dump(user_data, file)

    # Redirect to the login page after registration
    return FileResponse("page/login.html")
    

#______________________meeting______________________
@app.get("/meeting", response_class=HTMLResponse)
async def get_meeting_page(request: Request):
    return FileResponse("page/meeting.html")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import json
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="static_css")
app.mount("/js", StaticFiles(directory="js"), name="static_js")


#*********************************************************
import ZODB , ZODB.FileStorage
import transaction
import BTrees.OOBTree

mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root

class User():
    def __init__(self , username , password , email):
        self.username = username
        self.password = password
        self.email = email

#Create admin user
root.user_data = BTrees.OOBTree.BTree()
root.user_data['admin'] = User('admin1' , 'admin2' , 'admin@gmail.com')
transaction.commit()

connection.close()

#______________________home______________________
@app.get("/", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return FileResponse("page/index.html")


#______________________program______________________
@app.get("/program", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return FileResponse("page/program_choice.html")


#______________________login______________________
@app.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return FileResponse("page/login.html")


@app.post("/process_login")
async def process_login(username: str = Form(...), password: str = Form(...)):
    # Check if the username and password are correct
    user_data_file = os.path.join(data_dir, f"{username}.json")
    if os.path.exists(user_data_file):
        with open(user_data_file, "r") as file:
            user_data = json.load(file)
        if password == user_data["password"]:
            return FileResponse("page/channel.html")
        else:
            raise HTTPException(status_code=401, detail="Login failed")


#______________________register______________________
data_dir = "user_data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


@app.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return FileResponse("page/register.html")

@app.get("/register/{username}/{password}/{email}")
async def register(username: str , password: str , email: str):
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            return  JSONResponse(content={"message": "Username is already taken"})
        if email == user_info.email:    
            return JSONResponse(content={"message": "Email is already taken"})
        
    # put info in database
    connection = db.open()
    root.user_data[username] = User(username , password , email)
    transaction.commit()
    connection.close()
    return JSONResponse(content={"message": "Register successfully"})

@app.get("/register/all_data")
async def get_all_data():
    user_data = root.user_data
    data = []
    for user in user_data:
        user_info = user_data[user]
        data.append({
            "username": user_info.username,
            "password": user_info.password,
            "email": user_info.email
        })
    return JSONResponse(content={"data": data})


#______________________create______________________
templates = Jinja2Templates(directory="templates")
forum_entries = []

@app.get('/create_forum',response_class=HTMLResponse)
async def submit(request: Request):
    return FileResponse("templates/create_forum.html")


from fastapi import FastAPI, Request

@app.post('/create')
async def submit(request: Request):
    data = await request.form()
    type = data.get('type')
    topic = data.get('topic')
    content = data.get('content')
    
    forum_entry = {'type': type, 'topic': topic, 'content': content}
    forum_entries.append(forum_entry)
    
    return templates.TemplateResponse("forum_entries.html", {"request": request, "entries": forum_entries})


@app.get('/channel')
async def submit(request: Request):
    return FileResponse("page/channel.html")


#______________________meeting______________________
@app.get("/join_meeting", response_class=HTMLResponse)
async def get_meeting_page(request: Request):
    return FileResponse("page/meeting.html")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


connection.close()
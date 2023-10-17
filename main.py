from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse ,RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import json
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/css", StaticFiles(directory="css"), name="static_css")
app.mount("/js", StaticFiles(directory="js"), name="static_js")
app.mount("/image", StaticFiles(directory="image"), name="static_image")



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

# check if the all_user file exist
user_data_folder = "data/user"
user_data_dir = "data/user/all_user.json"
if not os.path.exists(user_data_folder):
    os.makedirs(user_data_folder)
if not os.path.exists(user_data_dir):
    with open(user_data_dir, 'w') as file:
        json.dump({}, file)
        file.close()

# On server start load all user data from json to ZODB
@app.on_event("startup")
async def startup_event():
    with open("data/user/all_user.json", 'r') as file:
        all_user = json.load(file)
        connection = db.open()
        root.user_data = BTrees.OOBTree.BTree()
        for user in all_user:
            user_info = all_user[user]
            root.user_data[user] = User(user_info['username'] , user_info['password'] , user_info['email'])
        transaction.commit()
        connection.close()

# On server shutdown save all user data from ZODB to json
@app.on_event("shutdown")
async def shutdown_event():
    with open("data/user/all_user.json", 'w') as file:
        all_user = {}
        connection = db.open()
        for user in root.user_data:
            user_info = root.user_data[user]
            all_user[user] = {
                "username": user_info.username,
                "password": user_info.password,
                "email": user_info.email
            }
        transaction.commit()
        connection.close()
        json.dump(all_user, file)


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

@app.get("/login/{username}/{password}")
async def login(username: str , password: str):
    # Check if the username and password are correct
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username and password == user_info.password:
            return JSONResponse(content={"message": "Login successfully"})
    return JSONResponse(content={"message": "Login failed"})

@app.get("/process_login/{username}")
async def process_login(request: Request, username: str):
    # read all json file form forum folder
    data_dir = "data/forum"
    forum_entries = []
    for filename in os.listdir(data_dir):
        forum_data_file = os.path.join(data_dir, filename)
        with open(forum_data_file, "r") as file:
            forum_entry = json.load(file)
            forum_entries.append(forum_entry) 

    # Check if the username and password are correct
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            return templates.TemplateResponse("channel.html", {"request": request, "entries": forum_entries , "username" : username})
    return RedirectResponse(url='/login')

#______________________register______________________
user_data_dir = "data/user"
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)


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


#______________________create forum______________________
forum_data_dir = "data/forum"
if not os.path.exists(forum_data_dir):
    os.makedirs(forum_data_dir)


forum_entries = []

@app.get('/create_forum/{username}',response_class=HTMLResponse)
async def submit(request: Request,username: str):
    #Check if the username exist or not
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            return FileResponse("templates/create_forum.html")
    return RedirectResponse(url='/login')



@app.post('/create')
async def submit(request: Request):
    data = await request.form()
    type = data.get('type')
    topic = data.get('topic')
    content = data.get('content')
    
    forum_entry = {'type': type, 'topic': topic, 'content': content}
    # save to forum_data (json)
    forum_data_file = os.path.join(forum_data_dir, f"{topic}.json")
    with open(forum_data_file, "w") as file:
        json.dump(forum_entry, file)
    
    return templates.TemplateResponse("forum_entries.html", {"request": request, "entry": forum_entry})


@app.get('/channel')
async def submit(request: Request):
    forum_entries = []
    for filename in os.listdir(forum_data_dir):
        forum_data_file = os.path.join(forum_data_dir, filename)
        with open(forum_data_file, "r") as file:
            forum_entry = json.load(file)
            forum_entries.append(forum_entry)
    
    return templates.TemplateResponse("channel.html", {"request": request, "entries": forum_entries})



#______________________meeting______________________
@app.get("/join_meeting", response_class=HTMLResponse)
async def get_meeting_page(request: Request):
    return FileResponse("page/meeting.html")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


connection.close()
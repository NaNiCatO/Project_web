from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse ,RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import json
from fastapi.templating import Jinja2Templates
from all_classes import User , Forum , Comment

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/css", StaticFiles(directory="css"), name="static_css")
app.mount("/js", StaticFiles(directory="js"), name="static_js")
app.mount("/image", StaticFiles(directory="image"), name="static_image")



#*********************************************************
import ZODB , ZODB.FileStorage
import transaction
import BTrees.OOBTree

#______________________ZODB______________________
mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root
# root.user_data = BTrees.OOBTree.BTree()

# forum_data = ZODB.FileStorage.FileStorage('forum_data.fs')
# db = ZODB.DB(forum_data)
# connection = db.open()
# root = connection.root
# root.forum_data = BTrees.OOBTree.BTree()

#______________________Classes______________________
# import persistent
# class User(persistent.Persistent):
#     def __init__(self , username , password , email):
#         self.username = username
#         self.password = password
#         self.email = email

# class Forum(persistent.Persistent):
#     def __init__(self , creator , type , topic , content):
#         self.creator = creator
#         self.type = type
#         self.topic = topic
#         self.content = content
#         self.like = 0
#         self.likeuser = []
#         self.comment = []
    
#     def add_comment(self , username , comment):
#         self.comment.append(Comment(username , comment))

#     def add_like(self , username):
#         self.like += 1
#         self.likeuser.append(username)

# class Comment(persistent.Persistent):
#     def __init__(self , username , comment):
#         self.username = username
#         self.comment = comment
#         self.like = 0
#         self.likeuser = []
    
#     def add_like(self , username):
#         self.like += 1
#         self.likeuser.append(username)

#______________________Server Start and Shutdown______________________

# # check if the all_user file exist
# user_data_folder = "data/user"
# user_data_dir = "data/user/all_user.json"
# if not os.path.exists(user_data_folder):
#     os.makedirs(user_data_folder)
# if not os.path.exists(user_data_dir):
#     with open(user_data_dir, 'w') as file:
#         json.dump({}, file)
#         file.close()

# # check if the all_forum file exist
# forum_data_folder = "data/forum"
# forum_data_dir = "data/forum/all_forum.json"
# if not os.path.exists(forum_data_folder):
#     os.makedirs(forum_data_folder)
# if not os.path.exists(forum_data_dir):
#     with open(forum_data_dir, 'w') as file:
#         json.dump({}, file)
#         file.close() 

# # On server start load all user data from json to ZODB
# @app.on_event("startup")
# async def startup_event():
#     # Load all user data from json to ZODB
#     # with open("data/user/all_user.json", 'r') as file:
#     #     all_user = json.load(file)
#     #     connection = db.open()
#     #     root.user_data = BTrees.OOBTree.BTree()
#     #     for user in all_user:
#     #         user_info = all_user[user]
#     #         root.user_data[user] = User(user_info['username'] , user_info['password'] , user_info['email'])
#     #     transaction.commit()
        # connection.close()
#     #     file.close()
    
#     # Load all forum data from json to ZODB
#     data_dir = "data/forum/all_forum.json"
#     with open(data_dir, 'r') as file:
#         all_forum = json.load(file)
#         connection = db.open()
#         root.forum_data = BTrees.OOBTree.BTree()
#         for forum in all_forum:
#             forum_info = all_forum[forum]
#             root.forum_data[forum] = Forum(forum_info['creator'] , forum_info['type'] , forum_info['topic'] , forum_info['content'])
#         transaction.commit()
        # connection.close()
#         file.close()


    

        


# # On server shutdown save all user data from ZODB to json
@app.on_event("shutdown")
async def shutdown_event():
    transaction.commit()
    connection.close()
#     # Save all user data from ZODB to json
#     with open("data/user/all_user.json", 'w') as file:
#         all_user = {}
#         connection = db.open()
#         for user in root.user_data:
#             user_info = root.user_data[user]
#             all_user[user] = {
#                 "username": user_info.username,
#                 "password": user_info.password,
#                 "email": user_info.email
#             }
#         transaction.commit()
        # connection.close()
#         json.dump(all_user, file)
#         file.close()
    
#     # Save all forum data from ZODB to json
#     data_dir = "data/forum/all_forum.json"
#     with open(data_dir, 'w') as file:
#         all_forum = {}
#         connection = db.open()
#         for forum in root.forum_data:
#             forum_info = root.forum_data[forum]
#             all_forum[forum] = {
#                 "creator": forum_info.creator,
#                 "type": forum_info.type,
#                 "topic": forum_info.topic,
#                 "content": forum_info.content,
#                 "like": forum_info.like,
#                 "likeuser": forum_info.likeuser,
#                 "comment": forum_info.comment
#             }
#         transaction.commit()
        # connection.close()
#         json.dump(all_forum, file)
#         file.close()

forum_data = root.forum_data
for forum in forum_data:
    forum_info = forum_data[forum]
    data= {
        "creator": forum_info.creator,
        "type": forum_info.type,
        "topic": forum_info.topic,
        "content": forum_info.content,
        "like": forum_info.like,
        "likeuser": forum_info.likeuser,
        "comment": forum_info.comment
    }
    print(data)


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

@app.get("/login_1/{username}/{password}")
async def login(username: str , password: str):
    # Check if the username and password are correct
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            if password == user_info.password:
                return JSONResponse(content={"message": "Login successfully"})
    return JSONResponse(content={"message": "Login failed"})


@app.get("/process_login/{username}")
async def process_login(request: Request, username: str):
    forums_data = root.forum_data
    # Check if the username and password are correct
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            return templates.TemplateResponse("channel.html", {"request": request, "entries": forums_data , "username" : username})
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
    # connection = db.open()
    root.user_data[username] = User(username , password , email)
    # transaction.commit()
    # connection.close()
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

@app.get('/create_forum/{username}')
async def submit(request: Request,username: str):
    #Check if the username exist or not
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            return templates.TemplateResponse("create_forum.html", {"request": request,"username": username})
    return RedirectResponse(url='/login')



@app.post('/create/{username}')
async def submit(request: Request, username: str):
    
    #Check if the username exist or not
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            data = await request.json()
            type = data['type']
            topic = data['topic']
            content = data['content']

            #Check if the topic is already exist or not
            forum_data = root.forum_data
            for forum in forum_data:
                forum_info = forum_data[forum]
                if topic == forum_info.topic:
                    return JSONResponse(content={"message": "Topic is already taken"})
            
            # save to forum_data ZODB
            # connection = db.open()
            root.forum_data[topic] = Forum(username , type , topic , content)
            # transaction.commit()
            # connection.close()

            return JSONResponse(content={"message": "Create forum successfully"})
    return RedirectResponse(url='/login')
        
@app.post("/check_topic/{topic}")
async def check_topic(topic: str):
    #Check if the topic is already exist or not
    forum_data = root.forum_data
    for forum in forum_data:
        forum_info = forum_data[forum]
        if topic == forum_info.topic:
            return JSONResponse(content={"message": "Topic is already taken"})
    return JSONResponse(content={"message": "Topic is available"})



@app.get('/channel/{username}/{topic}')
async def submit(request: Request, username: str, topic: str):
    # forum_entries = []
    # for filename in os.listdir(forum_data_dir):
    #     forum_data_file = os.path.join(forum_data_dir, filename)
    #     with open(forum_data_file, "r") as file:
    #         forum_entry = json.load(file)
    #         forum_entries.append(forum_entry)

    #get all forum data
    # connection = db.open()
    # root = connection.root
    forum_data = root.forum_data
    print(root.forum_data[topic].comment) 
    # for forum in forum_data:
    forum_info = forum_data[topic]
    data= {
        "creator": forum_info.creator,
        "type": forum_info.type, 
        "topic": forum_info.topic,
        "content": forum_info.content,
        "like": forum_info.like,
        "likeuser": forum_info.likeuser,
        "comment": forum_info.comment
    }
    # connection.close()
    
    return templates.TemplateResponse("forum_entries.html", {"request": request, "entries": data, "username": username})


#______________________Add Comment______________________
@app.post('/add_comment/{username}')
async def submit(request: Request, username: str):
    #Check if the username exist or not
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            data = await request.json()
            topic = data['topic']
            comment = data['comment']


            # save to forum_data ZODB
            # connection = db.open()    
            # forum_info = root.forum_data[topic] 
            # forum_info.add_comment(username , comment) 
            # root.forum_data[topic] = forum_info
            root.forum_data[topic].comment.append(Comment(username , comment))
            # print(root.forum_data[topic].comment)
            # transaction.commit()
            # connection.close() 

            return JSONResponse(content={"message": "Comment successfully"})
    return RedirectResponse(url='/login')




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# #______________________ZODB Check______________________
# @app.get("/zodb")
# async def zodb():
#     #get all forum data
    # connection = db.open()
#     forum_data = root.forum_data
#     data = []
#     for forum in forum_data:
#         forum_info = forum_data[forum]
#         data.append({
#             "creator": forum_info.creator,
#             "type": forum_info.type,
#             "topic": forum_info.topic,
#             "content": forum_info.content,
#             "like": forum_info.like,
#             "likeuser": forum_info.likeuser,
#             "comment": forum_info.comment
#         })
#     return JSONResponse(content={"data": data})


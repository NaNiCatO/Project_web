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

# On server start
# @app.on_event("startup")
# async def startup_event():


# # On server shutdown
@app.on_event("shutdown")
async def shutdown_event():
    # save to database
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
    root.user_data[username] = User(username , password , email) 

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
            root.forum_data[topic] = Forum(username , type , topic , content)

            return JSONResponse(content={"message": "Create forum successfully"})
    return RedirectResponse(url='/login')

#______________________delete forum______________________
@app.get('/delete_forum/{username}/{topic}')
async def submit(request: Request, username: str, topic: str):
    #Check if the username exist or not
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            #Check if the topic is already exist or not
            forum_data = root.forum_data
            for forum in forum_data:
                forum_info = forum_data[forum]
                if topic == forum_info.topic:
                    del root.forum_data[topic]
    return RedirectResponse(url='/process_login/'+username)

#______________________edit forum______________________
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
    forum_data = root.forum_data
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
            forum_info = root.forum_data[topic] 
            forum_info.add_comment(username , comment) 
            root.forum_data[topic] = forum_info


            return JSONResponse(content={"message": "Comment successfully"})
    return RedirectResponse(url='/login')

#______________________Add like to Comment______________________
@app.post('/add_like_comment/{username}')
async def submit(request: Request, username: str):
    #Check if the username exist or not
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            data = await request.json()
            topic = data['topic']
            comment = data['comment']
            commentowner = data['commentowner']

            # save to forum_data ZODB
            forum_info = root.forum_data[topic] 
            for i in forum_info.comment:
                if i.username == commentowner and i.comment == comment:
                    if username not in i.likeuser:
                        i.add_like(username)
                        root.forum_data[topic] = forum_info
                        return JSONResponse(content={"message": "Like successfully"})
                    else:
                        i.unlike(username)
                        root.forum_data[topic] = forum_info
                        return JSONResponse(content={"message": "Unlike successfully"})
            root.forum_data[topic] = forum_info
            return JSONResponse(content={"message": "Comment Not found"})
    return JSONResponse(content={"message": "No user found"})

#______________________Save Booking Spots______________________
@app.post('/save_booking/{username}')
async def submit(request: Request, username: str):
    # check if the user is in the database
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:
            data = await request.json()
            roomnumber = data['roomnumber']
            selected_seat = data['selected_seat']


            # save into ZODB
            for i in selected_seat:
                root.booking_data[roomnumber].append(i)
            root.booking_data._p_changed = True


            return JSONResponse(content={"message": "Booking successfully"})
    return RedirectResponse(url='/login')

#______________________Get Booking HTML______________________
@app.get('/booking_room/{username}')
async def booking_room(request: Request, username: str):
    # check if the user is in the database
    user_data = root.user_data
    for user in user_data:
        user_info = user_data[user]
        if username == user_info.username:

            # send the data from ZODB to HTML
            booking_data = root.booking_data
            data = []
            for room in booking_data:
                room_info = booking_data[room]
                data.append({
                    "room": room,
                    "seat": room_info
                })

            return templates.TemplateResponse("booking.html", {"request": request, "entries": data, "username": username})

    return RedirectResponse(url='/login')

#______________________reset Booking Data______________________
@app.get('/reset_booking')
async def reset_booking(request: Request):
    # reset the booking data
    root.booking_data[1] = []
    root.booking_data[2] = []
    root.booking_data[3] = []
    root.booking_data[4] = []
    root._p_changed = True
    return RedirectResponse(url='/login')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


import persistent
class User(persistent.Persistent):
    def __init__(self , username , password , email):
        self.username = username
        self.password = password
        self.email = email

class Forum(persistent.Persistent):
    def __init__(self , creator , type , topic , content):
        self.creator = creator
        self.type = type
        self.topic = topic
        self.content = content
        self.like = 0
        self.likeuser = []
        self.comment = []
    
    def add_comment(self , username , comment):
        self.comment.append(Comment(username , comment))
        self._p_changed = True

    def add_like(self , username):
        self.like += 1
        self.likeuser.append(username)

class Comment(persistent.Persistent):
    def __init__(self , username , comment):
        self.username = username
        self.comment = comment
        self.like = 0
        self.likeuser = []
    
    def add_like(self , username):
        self.like += 1
        self.likeuser.append(username)
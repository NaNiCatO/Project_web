import ZODB , ZODB.FileStorage
import transaction
import BTrees.OOBTree

mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root
root.user_data = BTrees.OOBTree.BTree()
root.forum_data = BTrees.OOBTree.BTree()
root.booking_data = BTrees.OOBTree.BTree()
root.booking_data[1] = []
root.booking_data[2] = []
root.booking_data[3] = []
root.booking_data[4] = []


# forum_data = ZODB.FileStorage.FileStorage('forum_data.fs')
# db1 = ZODB.DB(forum_data)
# connection1 = db1.open()
# root1 = connection1.root
# root1.forum_data = BTrees.OOBTree.BTree()

transaction.commit()
connection.close()

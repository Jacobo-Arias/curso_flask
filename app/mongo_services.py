import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["todos"]
mycol = mydb["users"]

# def get_users():
#     return db.collection('users').get()

def get_user(user_id):
    return mycol.find_one({'user':user_id})


def user_put(user_data):
    mydict = {"user":user_data.username, "password":user_data.password, "todos":[]}
    mycol.insert_one(mydict)

def get_todos(user_id):
    # esto es por la estructura de la base de datos firestore
    # collectiones>documents>collections
    return mycol.find_one({'user':user_id},{'_id':0,'todos':1})['todos']

def put_todo(user_id, description):
    todos = get_todos(user_id)
    # añade un nuevo documento con id aleatorio
    new_todo = {'id':len(todos)+1,'description':description,'done':False}
    todos.append(new_todo)
    myquery = { "user": user_id }
    newvalues = { "$set": { "todos": todos } }
    mycol.update_one(myquery, newvalues)

def delete_todo(user_id, todo_id):
    todos = get_todos(user_id)
    del todos[todo_id-1]
    myquery = { "user": user_id }
    newvalues = { "$set": { "todos": todos } }
    mycol.update_one(myquery, newvalues)

def update_todo(user_id, todo_id, done):
    todos = get_todos(user_id)
    # añade un nuevo documento con id aleatorio
    todos[todo_id-1]['done'] = not done
    myquery = { "user": user_id }
    newvalues = { "$set": { "todos": todos } }
    mycol.update_one(myquery, newvalues)
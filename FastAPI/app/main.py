from http.client import HTTPException
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is Running!"}

@app.get("/user/{id}")
def user(id : int):

    users = ["John","Jack","Jill"]
    
    if users[id]:
        return {"user": users[id]}
    else:
        raise HTTPException(status_code=404, detail="User not found")

    
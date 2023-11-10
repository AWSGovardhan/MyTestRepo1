from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def disp():
    return {'Msg':'Hello'}

@app.get("/good")
async def disp():
    return {'Good Msg':'Good!'}


# @app.get("/good/{pone}")
# async def add(pone):
#     return {'Result ' : pone*5}

@app.get("/good/{pone}")
async def add(pone:int):
    return {'Result ' : pone*5}
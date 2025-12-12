from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello from Localhost!"}

@app.get("/ping")
async def ping():
    return {"ping": "pong!"}


from fastapi import FastAPI
from config import DEBUG_MODE, PORT, HOST
from api import routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(routes)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=HOST , port=PORT, log_level="info", reload=DEBUG_MODE)
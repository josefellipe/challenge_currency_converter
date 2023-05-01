import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "ok"}

if __name__ == "__main__":
    uvicorn.run(app)




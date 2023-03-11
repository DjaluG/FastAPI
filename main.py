from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "name": "Djalu Galang",
        "age": "17"
        }
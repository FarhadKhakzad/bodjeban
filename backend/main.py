from fastapi import FastAPI
from expenses import router as expenses_router

app = FastAPI()

app.include_router(expenses_router)

@app.get("/")
def root():
    return {"message": "🚀 API is running!"}

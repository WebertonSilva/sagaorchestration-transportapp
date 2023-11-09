from fastapi import FastAPI
from routers.transportrouters import router as transport
import uvicorn

app = FastAPI()

# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     responses={418: {"description": "I'm a teapot"}},
# )

#config = dotenv_values("db.env")

@app.get("/")
def root():
    return {"message": "Hello Transport API!"}

app.include_router(transport)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)




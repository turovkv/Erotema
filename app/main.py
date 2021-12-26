import fastapi
import uvicorn

from app.main.endpoint import auth, api

app = fastapi.FastAPI()


def configure():
    app.include_router(auth.router)
    app.include_router(api.router)


configure()
if __name__ == '__main__':
    uvicorn.run(app)

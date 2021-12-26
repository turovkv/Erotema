import fastapi
import uvicorn

from app.main.endpoint import auth, api
from app.main.exception.HTTPExceptionHandlers import add_handlers

app = fastapi.FastAPI()


def configure():
    add_handlers(app)
    app.include_router(auth.router)
    app.include_router(api.router)



configure()
if __name__ == '__main__':
    uvicorn.run(app)

import fastapi
import uvicorn

from app.Endpoints import endpoints
from app.Repositories.repositories import init_db

api = fastapi.FastAPI()


def configure():
    api.include_router(endpoints.router)


configure()
init_db()
if __name__ == '__main__':
    uvicorn.run(api)

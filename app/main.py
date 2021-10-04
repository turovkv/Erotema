import fastapi
import uvicorn

from app.EndpointsHTTP import endpoints
from app.GameServiceGraphQL import game_service
from app.Repositories.repositories import init_db

api = fastapi.FastAPI()


def configure():
    api.include_router(endpoints.router)
    api.include_router(game_service.router)


configure()
init_db()
if __name__ == '__main__':
    uvicorn.run(api)

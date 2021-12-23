import fastapi
import uvicorn

from app.QuizServiceHTTP.EndpointsHTTP import endpoints
from app.GameServiceGraphQL import game_service
from app.QuizServiceHTTP.Repositories.repositories import init_db
from app.main.endpoint import auth
#from app.main.repository.postgres_impl import user_service

api = fastapi.FastAPI()


def configure():
    # api.include_router(endpoints.router)
    # api.include_router(game_service.router)
    # api.include_router(user_service.router)
    api.include_router(auth.router)


configure()
# init_db()
if __name__ == '__main__':
    uvicorn.run(api)

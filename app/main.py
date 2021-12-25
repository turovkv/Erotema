import fastapi
import uvicorn

# from app.QuizServiceHTTP.EndpointsHTTP import endpoints
# from app.GameServiceGraphQL import game_service
# from app.QuizServiceHTTP.Repositories.repositories import init_db
from app.main.endpoint import auth, api
#from app.main.repository.postgres_impl import user_service

app = fastapi.FastAPI()


def configure():
    # api.include_router(endpoint.router)
    # api.include_router(game_service.router)
    # api.include_router(user_service.router)
    app.include_router(auth.router)
    app.include_router(api.router)


configure()
# init_db()
if __name__ == '__main__':
    uvicorn.run(app)

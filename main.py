import fastapi
import uvicorn

from Endpoints import endpoints

api = fastapi.FastAPI()


def configure():
    api.include_router(endpoints.router)


configure()
if __name__ == '__main__':
    uvicorn.run(api)

import fastapi
from graphene import ObjectType, List, String, Int, Field, Schema
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from app.QuizServiceHTTP.Repositories.repositories import fake_db


class Quiz(ObjectType):
    id_token = String(required=True)
    text = String(required=True)
    question_ids: Field(List(String), required=True)


class GameWithQuiz(ObjectType):
    user_id_token = String(required=True)
    quiz = Field(Quiz, required=True)
    status = String(required=True)
    points = Int(required=True)


class Query(ObjectType):
    get_games_for_user = Field(List(GameWithQuiz), user_id=String(default_value="0"))

    async def resolve_get_games_for_user(self, info, user_id):
        games = fake_db["game"].values()
        games_with_quiz = []
        for game in games:
            if game.user_id_token == user_id:
                games_with_quiz.append(
                    GameWithQuiz(
                        user_id_token=game.user_id_token,
                        quiz=fake_db["quiz"][game.quiz_id_token],
                        status=game.status,
                        points=game.points
                    )
                )
        return games_with_quiz


router = fastapi.APIRouter()
router.add_route("/gameGraphQL",
                 GraphQLApp(
                     schema=Schema(query=Query),
                     executor_class=AsyncioExecutor
                 )
                 )

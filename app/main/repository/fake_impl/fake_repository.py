from typing import Optional, List

from app.main.model.models import User, Quiz, Answer, Question, UserQuiz, QuizSession, UserSession
from app.main.repository.repository import Repository

fake_users_db = {
    # "johndoe": {
    #     "id": 1,
    #     "username": "johndoe",
    #     "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"  # 'secret'
    # }
}

users = [
    # User(**{"id": 0, "username": "0", "hashed_password": "0"}),
    # User(**{"id": 1, "username": "1", "hashed_password": "1"}),
    # User(**{"id": 2, "username": "2", "hashed_password": "2"}),
]

answers = [
    Answer(**{"id": 0, "title": "0", "points": 1}),
    Answer(**{"id": 1, "title": "1", "points": 2}),
    Answer(**{"id": 2, "title": "2", "points": 3}),
    Answer(**{"id": 3, "title": "3", "points": 4}),
]

questions = [
    Question(**{"id": 0, "title": "0", "answers": answers[0:2]}),
    Question(**{"id": 1, "title": "1", "answers": answers[1:3]}),
    Question(**{"id": 2, "title": "2", "answers": answers[2:4]}),
]

quizzes = [
    Quiz(**{"id": 0, "title": "0", "questions": questions[0:2], "is_public": False}),
    Quiz(**{"id": 1, "title": "1", "questions": questions[1:3], "is_public": True}),
    Quiz(**{"id": 2, "title": "2", "questions": questions[0:3], "is_public": True}),
]

user_quizzes = [
    UserQuiz(**{"user_id": 0, "quiz_id": 0}),
    UserQuiz(**{"user_id": 0, "quiz_id": 1}),
    UserQuiz(**{"user_id": 1, "quiz_id": 2}),
]

quiz_sessions = [
    QuizSession(**{"id": 0, "quiz_id": 0, "user_id": 1, "is_ended": False}),
    QuizSession(**{"id": 1, "quiz_id": 1, "user_id": 2, "is_ended": False}),
    QuizSession(**{"id": 2, "quiz_id": 2, "user_id": 3, "is_ended": False}),
]

user_sessions = [
    UserSession(**{"id": 0, "quiz_session_id": 0, "user_id": 0, "point_sum": 0}),
    UserSession(**{"id": 1, "quiz_session_id": 0, "user_id": 1, "point_sum": 1}),
    UserSession(**{"id": 2, "quiz_session_id": 1, "user_id": 1, "point_sum": 2}),
    UserSession(**{"id": 3, "quiz_session_id": 2, "user_id": 1, "point_sum": 3}),
]


class FakeRepository(Repository):
    def get_user(self, username: str) -> Optional[User]:
        for u in users:
            if username in u.username:
                return u
        return None

    def create_user(self, username: str, hashed_password: str) -> None:
        user = self.get_user(username)
        if user is not None:
            raise Exception("This user already exists")

        users.append(
            User(
                id=len(users),
                username=username,
                hashed_password=hashed_password
            )
        )
        # fake_users_db[username] = {
        #     "id": len(fake_users_db),
        #     "username": username,
        #     "hashed_password": hashed_password
        # }

    def get_quiz_id_by_session(self, user_session_id: int) -> int:
        user_session = list(filter(lambda us: us.id == user_session_id, user_sessions))[0]
        quiz_session = list(filter(lambda qs: qs.id == user_session.quiz_session_id, quiz_sessions))[0]
        return quiz_session.quiz_id

    def get_quiz(self, quiz_id: int) -> Quiz:
        return list(filter(lambda q: q.id == quiz_id, quizzes))[0]

    def get_saved_quizzes(self, user_id: int) -> List[Quiz]:
        lq = []
        for u_q in user_quizzes:
            if u_q.user_id == user_id:
                lq.append(quizzes[u_q.quiz_id])
        return lq

    def get_public_quizzes(self):
        lq = []
        for q in quizzes:
            if q.is_public:
                lq.append(q)
        return lq

    def update_points(self, user_session_id: int, point_sum: int) -> None:
        user_sessions[user_session_id].point_sum = point_sum

    def update_quiz_publicity(self, user_id: int, quiz_id: int) -> None:
        quizzes[quiz_id].is_public = True

    def create_quiz(self, user_id: int, quiz: Quiz) -> int:
        ind = len(quizzes)
        quiz.id = ind
        quizzes.append(quiz)
        return ind

    def create_quiz_session(self, user_id: int, quiz_id: int) -> int:
        quiz_sessions.append(
            QuizSession(
                id=len(quiz_sessions),
                quiz_id=quiz_id,
                user_id=user_id,
                is_ended=False
            )
        )
        return len(quiz_sessions) - 1

    def create_user_session(self, user_id: int, session_id: int) -> int:
        user_sessions.append(
            UserSession(
                id=len(quiz_sessions),
                quiz_session_id=session_id,
                user_id=user_id,
                point_sum=False
            )
        )
        return len(user_sessions) - 1

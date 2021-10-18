create table Answers
(
    id   serial primary key,
    text text not null
);

create table Questions
(
    id   serial primary key,
    text text not null
);

create table Quizes
(
    id   serial primary key,
    text text not null
);

create table QuestionAnswers
(
    question_id int not null references Questions (id),
    answer_id   int not null references Answers (id),
    points      int not null
);

create table QuizQuestions
(
    quiz_id     int not null references Quizes (id),
    question_id int not null references Questions (id)
);
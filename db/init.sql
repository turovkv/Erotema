DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;

create table Quizzes
(
    id   int primary key,
    text text unique not null
);

create table Questions
(
    id   int primary key,
    text text unique not null
);

create table Quiz_Question_Edges
(
    question_id int not null references Questions (id),
    quiz_id     int not null references Quizzes (id)
);

create table Answers
(
    id          int primary key,
    text        text unique not null,
    is_correct  boolean     not null,
    question_id int         not null references Questions (id)
);

create table Game_Sessions
(
    id         int primary key,
    quiz_id    int       not null references Quizzes (id),
    start_time timestamp not null,
    seconds    int       not null
);

create table Users
(
    id            int primary key,
    login         text unique not null,
    password_hash text        not null
);

create table User_Game_Sessions
(
    user_id         int not null references Users (id),
    game_session_id int not null references Game_Sessions (id),
    points          int not null
);

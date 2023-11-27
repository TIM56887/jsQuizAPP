drop database codeQuiz;
CREATE DATABASE codeQuiz;
use codeQuiz;
create table questions(
question_id INT PRIMARY KEY auto_increment,
question varchar(80),
question_code varchar(512),
option1 varchar(100),
option2 varchar(100),
option3 varchar(100),
option4 varchar(100),
answer 	TINYINT UNSIGNED,
question_type varchar(32),
explanation text

);
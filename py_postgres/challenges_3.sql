
-- ASSESSMENT TEST 3

-- Create a new database called "School" this database should have two tables: teachers and students.

-- The students table should have columns for student_id, first_name,last_name, homeroom_number, phone,email, and graduation year.

create table school.students(
student_id INTEGER primary key, 
first_name VARCHAR(50),
last_name VARCHAR(50), 
homeroom_number INTEGER not null, 
phone VARCHAR(50) not null,
email VARCHAR(50) unique,
graduation_year VARCHAR(50)
)

-- The teachers table should have columns for teacher_id, first_name, last_name,homeroom_number, department, email, and phone.

create table school.teachers(
teacher_id INTEGER primary key, 
first_name VARCHAR(50), 
last_name VARCHAR(50),
homeroom_number INTEGER not null,  
department VARCHAR(50), 
email VARCHAR(50) unique, 
phone VARCHAR(50)
)


--The constraints are mostly up to you, but your table constraints do have to consider the following:
--We must have a phone number to contact students in case of an emergency.
--We must have ids as the primary key of the tables
--Phone numbers and emails must be unique to the individual.


--insert a student named Mark Watney (student_id=1) who has a phone number of 777-555-1234 and doesn't have an email. He graduates in 2035 and has 5 as a homeroom number.

insert into school.students(student_id, phone, homeroom_number, graduation_year)
values (1,'777-555-1234',5,'2035')

insert into school.teachers(teacher_id, homeroom_number, email)
values (1,5,'jsalk@school.org')

--insert a teacher names Jonas Salk (teacher_id = 1) who as a homeroom number of 5 and is from the Biology department. His contact info is: jsalk@school.org and a phone number of 777-555-4321.


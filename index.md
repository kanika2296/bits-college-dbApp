## ERP Database Application

Objective: To implement the erp system, having entities like Students, Teachers, Courses, Location of courses , Scores and TAs

### Functions:
### Teacher:
1. Teachers can view all students enrolled for a course 
2. Teachers can view all TAs assigned for a course
3. Teachers can update student scores
4. Teachers can view and update their personal information
5. Teachers can fetch top three scorers for a course
### Students:
1. Students can enroll in a course
2. Students can  drop a course    
3. Students can view scores
4. Students can view and update their personal information
5. View courses available to enroll as TA
6. Students can view Class Average and Highest marks 
### TA:
1. TA can update score of students
2. View courses available to enroll 

### Models
Students : Primary key(PK) - studentid 
Courses : PK courseid
Teachers : PK teacherid
Scorelookup : PK grade
Place : PK placeid
TA: PK courseid and studentid, fk referenced from courses and students respectively 

To depict many to many relations between entities:
teacherCourse
studentCourse
coursePlace

## Steps to Run:
```steps to run:
1. Open PowerShell and mkdir bitshyd
2. Run python -m venv venv
3. Activate scripts by running venv\Scripts\activate
4. pip install django
5. pip install mysqlclient
6. django-admin startproject bits
7. cd bits and run python manage.py startapp erpApp *copy erpApp files to this folder*
8. python manage.py inspectdb > models.py
9. python manage.py makemigrations erpApp
10. make migration 
11. python manage.py runserver
12. Navigate to 127.0.0.1:8000/erp/
```
### Markdown


![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(61).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(62).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(64).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(66).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(67).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(68).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(69).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(70).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(72).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(73).png)
![Image](https://github.com/kanika2296/bitsErpApp/blob/master/screenshot/Screenshot%20(74).png)





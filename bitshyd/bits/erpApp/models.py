from django.db import models

class Courseplace(models.Model):
    courses_courseid = models.OneToOneField('Courses', models.DO_NOTHING, db_column='courses_courseid', primary_key=True)
    place_placeid = models.ForeignKey('Place', models.DO_NOTHING, db_column='place_placeid')

    class Meta:
        managed = False
        db_table = 'courseplace'
        unique_together = (('courses_courseid', 'place_placeid'),)


class Courses(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursenumber = models.CharField(max_length=45, blank=True, null=True)
    coursename = models.CharField(max_length=45, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'

class Login(models.Model):
    userid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'login'
        unique_together = (('userid', 'role'),)


class Place(models.Model):
    placeid = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    block = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class Scorelookup(models.Model):
    score = models.IntegerField(blank=True, null=True)
    grade = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'scorelookup'


class Studentcourse(models.Model):
    students_studentid = models.OneToOneField('Students', models.DO_NOTHING, db_column='students_studentid', primary_key=True)
    courses_courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='courses_courseid')
    grade = models.ForeignKey(Scorelookup, models.DO_NOTHING, db_column='grade')

    class Meta:
        managed = False
        db_table = 'studentcourse'
        unique_together = (('students_studentid', 'courses_courseid'),)


class Students(models.Model):
    studentid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=45, blank=True, null=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    department = models.CharField(max_length=45, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Ta(models.Model):
    courses_courseid = models.OneToOneField(Courses, models.DO_NOTHING, db_column='courses_courseid', primary_key=True)
    students_studentid = models.ForeignKey(Students, models.DO_NOTHING, db_column='students_studentid')

    class Meta:
        managed = False
        db_table = 'ta'
        unique_together = (('courses_courseid', 'students_studentid'),)


class Teachercourse(models.Model):
    teachers_teacherid = models.OneToOneField('Teachers', models.DO_NOTHING, db_column='teachers_teacherid', primary_key=True)
    courses_courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='courses_courseid')

    class Meta:
        managed = False
        db_table = 'teachercourse'
        unique_together = (('teachers_teacherid', 'courses_courseid'),)


class Teachers(models.Model):
    teacherid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=45, blank=True, null=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'

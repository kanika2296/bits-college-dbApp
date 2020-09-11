from django import forms

ROLESDB = (  
    ('teacher', 'Teacher'),
    ('student', 'Student'),
    ('ta', 'TA'),
)
Courses = (  
    ('teacher', 'Course One'),
    ('student', 'Student'),
    ('ta', 'TA'),
)
class loginform(forms.Form):
    userid = forms.IntegerField(label='UserName',required=True)
    password = forms.CharField(label='Password',required=True)
    category = forms.ChoiceField(choices=ROLESDB, required=True )

class editTeacher(forms.Form):
    update_email = forms.CharField(label='Update Email',required=True)
    update_phone = forms.CharField(label='Update Phone',required=True)




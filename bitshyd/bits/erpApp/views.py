from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import loginform,editTeacher
from erpApp.models import *
from django.http import JsonResponse
import json
from django.db.models import Q
def home(request):
    form = loginform(request.POST)
    if form.is_valid():
        id = form.cleaned_data.get('userid')
        rl = form.cleaned_data.get('category')
        pwd = form.cleaned_data.get('password')
        request.session['userid'] = id
        request.session['role'] = rl
        tfull = Login.objects.filter(userid=id).filter(role=rl).first()
        if(tfull.password == pwd):
            if(rl == "teacher"):
                return HttpResponseRedirect('teacher/%s'% 0)
            elif (rl=="student"):
                return HttpResponseRedirect('student/%s'% 0)
            else:
                return HttpResponseRedirect('ta/%s'% 0)
        else:
            form = loginform(request.POST)
    return render(request, 'erpApp/home.html',{'form': form})
# teacher
def teacher(request,id,id1="0"):
    if(id == "1"):
        ids = Teachercourse.objects.values_list('courses_courseid', flat=True).filter(teachers_teacherid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/teacher.html',context=context1)
    if(id =="2" and id1!="0"):
         ids = Studentcourse.objects.values_list('students_studentid', flat=True).filter(courses_courseid=id1)
         std_list = Students.objects.filter(studentid__in = ids)
         context1 = { 'students': std_list,'id':"ViewStudentsbyCourse"}
         return render(request, 'erpApp/teacher.html',context=context1)
    if(id =="2"):
        ids = Teachercourse.objects.values_list('courses_courseid', flat=True).filter(teachers_teacherid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/teacher.html',context=context1)
    if(id =="3" and id1!="0"):
         ids = Ta.objects.values_list('students_studentid', flat=True).filter(courses_courseid=id1)
         std_list = Students.objects.filter(studentid__in = ids)
         context1 = { 'students': std_list,'id':"ViewTAbyCourse"}
         return render(request, 'erpApp/teacher.html',context=context1)
    if(id =="3"):
        ids = Teachercourse.objects.values_list('courses_courseid', flat=True).filter(teachers_teacherid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/teacher.html',context=context1)
    if(id == "4" and id1!="0"):
        ids = Teachers.objects.filter(teacherid=request.session['userid']).first()
        form = editTeacher(request.POST)
        if form.is_valid():
            mail = form.cleaned_data.get('update_email')
            ph = form.cleaned_data.get('update_phone')
            tfull = Teachers.objects.filter(teacherid=request.session['userid']).first()
            tfull.email = mail
            tfull.phone = ph
            tfull.save()
            return render(request,'erpApp/teacher.html',{'id':"4",'tfull':tfull})
        else:
            form = editTeacher()
        return render(request, 'erpApp/teacher.html', {'form': form,'id':"editTeacher",'tfull':ids},)
    if(id == "4"):
        ids = Teachers.objects.filter(teacherid=request.session['userid']).first()
        context1 = { 'tfull': ids, 'id':id}
        return render(request, 'erpApp/teacher.html',context=context1)
    if(id =="6" and id1!="0"):
         s = Studentcourse.objects.filter(courses_courseid__in=id1)
         std_list = s.values('students_studentid','grade','students_studentid__fname','students_studentid__lname')
         context1 = { 'students': std_list,'id':"StudentlistScore",'courseid':id1}
         return render(request, 'erpApp/teacher.html',context=context1)
    if(id == "6"):
        ids = Teachercourse.objects.values_list('courses_courseid', flat=True).filter(teachers_teacherid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/teacher.html',context=context1)
    if(id=="5"):
        request.session['userid']=""
        request.session['role']=""
        return HttpResponseRedirect('../../')
    else:
        return render(request, 'erpApp/teacher.html')
    return render(request, 'erpApp/teacher.html',context=context1)

# update score
def updatescore(request):
    response = {'msg': 'Invalid'}
    if request.method == "POST" and request.is_ajax:
        s = Studentcourse.objects.filter(students_studentid = request.POST["sid"]).filter(courses_courseid  = request.POST["cid"]).update(grade=request.POST["grade"])
    return HttpResponse(json.dumps(response), content_type="application/json")
#student 
def student(request,id,id1="0"):
    if(id == "1" and id1!="0"):
        st = Students.objects.get(studentid = request.session["userid"])
        i = int(id1)
        ct = Courses.objects.get(courseid = i)
        g = Scorelookup.objects.get(grade = "F")
        s=Studentcourse.objects.create(courses_courseid=ct,students_studentid = st,grade=g)
        cl = Ta.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid').union(Studentcourse.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid'))
        cl2 = Courses.objects.filter(~Q(courseid__in = cl))
        ids = Studentcourse.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id,'avl':cl2}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "1"):
        cl = Ta.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid').union(Studentcourse.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid'))
        cl2 = Courses.objects.filter(~Q(courseid__in = cl))
        ids = Studentcourse.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id,'avl':cl2}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "2" and id1!="0"):
        Studentcourse.objects.filter(students_studentid = request.session["userid"]).filter(courses_courseid=id1).delete()
        ids = Studentcourse.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "2"):
        ids = Studentcourse.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "3"):
        ids = Studentcourse.objects.filter(students_studentid=request.session['userid']).values('courses_courseid__courseid','courses_courseid__coursename','grade__score','grade__grade')
        context1 = { 'courses': ids, 'id':id}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "4" and id1!="0"):
        st = Students.objects.get(studentid = request.session["userid"])
        i = int(id1)
        ct = Courses.objects.get(courseid = i)
        g = Scorelookup.objects.get(grade = "F")
        s=Ta.objects.create(courses_courseid=ct,students_studentid = st)
        cl = Ta.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid').union(Studentcourse.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid'))
        cl2 = Courses.objects.filter(~Q(courseid__in = cl))
        ids = Ta.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id,'avl':cl2}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "4"):
        cl = Ta.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid').union(Studentcourse.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid'))
        cl2 = Courses.objects.filter(~Q(courseid__in = cl))
        ids = Ta.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id,'avl':cl2}
        return render(request, 'erpApp/student.html',context=context1)
    if(id == "6" and id1!="0"):
        ids = Students.objects.filter(studentid=request.session['userid']).first()
        form = editTeacher(request.POST)
        if form.is_valid():
            mail = form.cleaned_data.get('update_email')
            ph = form.cleaned_data.get('update_phone')
            tfull = Students.objects.filter(studentid=request.session['userid']).first()
            tfull.email = mail
            tfull.phone = ph
            tfull.save()
            return render(request,'erpApp/student.html',{'id':"6",'tfull':tfull})
        else:
            form = editTeacher()
        return render(request, 'erpApp/student.html', {'form': form,'id':"editStudent",'tfull':ids},)
    if(id == "6"):
        ids = Students.objects.filter(studentid=request.session['userid']).first()
        context1 = { 'tfull': ids, 'id':id}
        return render(request, 'erpApp/student.html',context=context1)
    if(id=="5"):
        request.session['userid']=""
        request.session['role']=""
        return HttpResponseRedirect('../../')
    else:
        return render(request, 'erpApp/student.html')
    return render(request, 'erpApp/student.html')

#ta
def ta(request,id,id1="0"):
    if(id == "1" and id1!="0"):
        st = Students.objects.get(studentid = request.session["userid"])
        i = int(id1)
        ct = Courses.objects.get(courseid = i)
        g = Scorelookup.objects.get(grade = "F")
        s= Ta.objects.create(courses_courseid=ct,students_studentid = st)
        cl = Ta.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid').union(Studentcourse.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid'))
        cl2 = Courses.objects.filter(~Q(courseid__in = cl))
        ids = Ta.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id,'avl':cl2}
        return render(request, 'erpApp/ta.html',context=context1)
    if(id == "1"):
        cl = Ta.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid').union(Studentcourse.objects.filter(students_studentid = request.session["userid"]).values_list('courses_courseid'))
        cl2 = Courses.objects.filter(~Q(courseid__in = cl))
        ids = Ta.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id,'avl':cl2}
        return render(request, 'erpApp/ta.html',context=context1)
    if(id =="2" and id1!="0"):
         s = Studentcourse.objects.filter(courses_courseid__in=id1)
         std_list = s.values('students_studentid','grade','students_studentid__fname','students_studentid__lname')
         context1 = { 'students': std_list,'id':"StudentlistScore",'courseid':id1}
         return render(request, 'erpApp/ta.html',context=context1)
    if(id == "2"):
        ids = Ta.objects.values_list('courses_courseid', flat=True).filter(students_studentid=request.session['userid'])
        courseid_list = Courses.objects.filter(courseid__in = ids)
        context1 = { 'courses': courseid_list, 'id':id}
        return render(request, 'erpApp/ta.html',context=context1)
    if(id=="3"):
        request.session['userid']=""
        request.session['role']=""
        return HttpResponseRedirect('../../')
    else:
        return render(request, 'erpApp/ta.html')
    return render(request, 'erpApp/ta.html')

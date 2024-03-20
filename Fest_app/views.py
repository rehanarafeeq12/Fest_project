
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages, auth
from Fest_app.filters import ContestFilter
from Fest_app.forms import ContestFilterForm, SchoolReg, UserReg, StudentReg, achievements_form, contactform, contest_list, feedback_form, gallery_form, guests_form, judges_list, management_form, participant_list, performers_list, programmes_list, result_list,  teachers_form, venue_list, volunteers_list
from Fest_app.models import School, Student, achievements, contest, feedbacks, gallery, guests, judges, management, participant, performer, programmes, result, teachers, venue, volunteers

# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')
def homepage(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect ('main_admin')
        elif user is not None and user.is_School:
            if user.school.approval_status==1:
                login(request,user)
                return redirect('adminpage')
        elif user is not None and user.is_Student:
            if user.student.approval_status==1:
                login(request,user)
                return redirect('homepage')
        else:
            messages.info(request,'Not a Registered User')            
    return render(request,'login.html')




def registerpage(request):
    return render(request,'register.html')

def adminpage(request):
    return render(request,'admin.html')

def main_admin(request):
    return render(request,'main_admin.html')

def schoolregister(request):
    user_form=UserReg()
    school_form=SchoolReg()
    if request.method=='POST':
        user_form=UserReg(request.POST)
        school_form=SchoolReg(request.POST)
        if user_form.is_valid() and school_form.is_valid():
            user=user_form.save(commit=False)
            user.is_School=True
            user.save()
            school=school_form.save(commit=False)
            school.user=user
            school.save()
            messages.info(request,'School Registered Successfully')
            return redirect('loginpage')
    return render(request,'schoolregister.html',{'user_form':user_form,'school_form':school_form})

def studentregister(request):
    user_form=UserReg()
    stud_form=StudentReg()
    if request.method=='POST':
        user_form=UserReg(request.POST)
        stud_form=StudentReg(request.POST)
        if user_form.is_valid() and stud_form.is_valid():
            user=user_form.save(commit=False)
            user.is_Student=True
            user.save()
            stud=stud_form.save(commit=False)
            stud.user=user
            stud.save()
            messages.info(request,'Student Registered successfully')
            return redirect('loginpage')
    return render(request,'studentregister.html',{'user_form':user_form,'stud_form':stud_form})

def school_view(request):
    data=School.objects.all()
    return render(request,'school_view.html',{'data':data})
def approve_school(request,id):
    school=School.objects.get(user_id=id)
    school.approval_status=True
    school.save()
    return redirect('school_view')

def student_view(request):
    data=Student.objects.all()
    return render(request,'student_view.html',{'data':data})
def approve_student(request,id):
    student=Student.objects.get(user_id=id)
    student.approval_status=True
    student.save()
    return redirect('student_view')

def contestadd(request):
    form=contest_list()
    if request.method=='POST':
        form=contest_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('contestadd')
    return render(request,'contestadd.html',{'form':form})
def contestview(request):
    data=contest.objects.all()
    return render(request,'contestview.html',{'data':data}) 
def update_list(request,id):
    data=contest.objects.get(id=id)
    form=contest_list(instance=data)
    if request.method=='POST':
        form=contest_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('contestview')
    return render(request,'contest_update.html',{'form':form})
def del_list(request,id):
    contest.objects.get(id=id).delete()
    return redirect('contestview')

def participant_add(request):
    form=participant_list()
    if request.method=='POST':
        form=participant_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('participant_add')
    return render(request,'participant_add.html',{'form':form})
def participant_view(request):
    data=participant.objects.all()
    
    return render(request,'participant_view.html',{'data':data}) 
def update_participant(request,id):
    data=participant.objects.get(id=id)
    form=participant_list(instance=data)
    if request.method=='POST':
        form=participant_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('participant_view')
    return render(request,'participant_update.html',{'form':form})
def del_participant(request,id):
    participant.objects.get(id=id).delete()
    return redirect('participant_view')

def judges_add(request):
    form=judges_list()
    if request.method=='POST':
        form=judges_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('judges_add')
    return render(request,'judges_add.html',{'form':form})
def judges_view(request):
    data=judges.objects.all()
    return render(request,'judges_view.html',{'data':data}) 
def update_judges(request,id):
    data=judges.objects.get(id=id)
    form=judges_list(instance=data)
    if request.method=='POST':
        form=judges_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('judges_view')
    return render(request,'judges_update.html',{'form':form})
def del_judges(request,id):
    judges.objects.get(id=id).delete()
    return redirect('judges_view')

def result_add(request):
    form=result_list()
    if request.method=='POST':
        form=result_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('result_add')
    return render(request,'result_add.html',{'form':form})
def result_view(request):
    data=result.objects.all()
    return render(request,'result_view.html',{'data':data}) 
def update_result(request,id):
    data=result.objects.get(id=id)
    form=result_list(instance=data)
    if request.method=='POST':
        form=result_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('result_view')
    return render(request,'result_update.html',{'form':form})
def del_result(request,id):
    result.objects.get(id=id).delete()
    return redirect('result_view')

def programmes_add(request):
    form=programmes_list()
    if request.method=='POST':
        form=programmes_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('programmes_add')
    return render(request,'programmes_add.html',{'form':form})
def programmes_view(request):
    data=programmes.objects.all()
    return render(request,'programmes_view.html',{'data':data}) 
def update_programmes(request,id):
    data=programmes.objects.get(id=id)
    form=programmes_list(instance=data)
    if request.method=='POST':
        form=programmes_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('programmes_view')
    return render(request,'programmes_update.html',{'form':form})
def del_programmes(request,id):
    programmes.objects.get(id=id).delete()
    return redirect('programmes_view')

def performer_add(request):
    form=performers_list()
    if request.method=='POST':
        form=performers_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('performer_add')
    return render(request,'performer_add.html',{'form':form})
def performer_view(request):
    data=performer.objects.all()
    return render(request,'performer_view.html',{'data':data}) 
def update_performer(request,id):
    data=performer.objects.get(id=id)
    form=performers_list(instance=data)
    if request.method=='POST':
        form=performers_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('performer_view')
    return render(request,'performer_update.html',{'form':form})
def del_performer(request,id):
    performer.objects.get(id=id).delete()
    return redirect('performer_view')

def venue_add(request):
    form=venue_list()
    if request.method=='POST':
        form=venue_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('venue_add')
    return render(request,'venue_add.html',{'form':form})
def venue_view(request):
    data=venue.objects.all()
    return render(request,'venue_view.html',{'data':data}) 
def update_venue(request,id):
    data=venue.objects.get(id=id)
    form=venue_list(instance=data)
    if request.method=='POST':
        form=venue_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('venue_view')
    return render(request,'venue_update.html',{'form':form})
def del_venue(request,id):
    venue.objects.get(id=id).delete()
    return redirect('venue_view')

def volunteers_add(request):
    form=volunteers_list()
    if request.method=='POST':
        form=volunteers_list(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('volunteers_add')
    return render(request,'volunteers_add.html',{'form':form})
def volunteers_view(request):
    data=volunteers.objects.all()
    return render(request,'volunteers_view.html',{'data':data}) 
def update_volunteers(request,id):
    data=volunteers.objects.get(id=id)
    form=volunteers_list(instance=data)
    if request.method=='POST':
        form=volunteers_list(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('volunteers_view')
    return render(request,'volunteers_update.html',{'form':form})
def del_volunteers(request,id):
    volunteers.objects.get(id=id).delete()
    return redirect('volunteers_view')

def guests_add(request):
    form=guests_form()
    if request.method=='POST':
        form=guests_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('guests_add')
    return render(request,'guests_add.html',{'form':form})
def guests_view(request):
    data=guests.objects.all()
    return render(request,'guests_view.html',{'data':data}) 
def update_guests(request,id):
    data=guests.objects.get(id=id)
    form=guests_form(instance=data)
    if request.method=='POST':
        form=guests_form(request.POST,request.FILES,instance=data)
        
        if form.is_valid():
            form.save()
            return redirect('guests_view')
    return render(request,'guests_update.html',{'form':form})
def del_guests(request,id):
    guests.objects.get(id=id).delete()
    return redirect('guests_view')

def gallery_add(request):
    form=gallery_form()
    if request.method=='POST':
        form=gallery_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('gallery_add')
    return render(request,'gallery_add.html',{'form':form})
def gallery_view(request):
    data=gallery.objects.all()
    return render(request,'gallery_view.html',{'data':data}) 
def update_gallery(request,id):
    data=gallery.objects.get(id=id)
    form=gallery_form(instance=data)
    if request.method=='POST':
        form=gallery_form(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('gallery_view')
    return render(request,'gallery_update.html',{'form':form})
def del_gallery(request,id):
    gallery.objects.get(id=id).delete()
    return redirect('gallery_view')

def achievements_add(request):
    form=achievements_form()
    if request.method=='POST':
        form=achievements_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('achievements_add')
    return render(request,'achievements_add.html',{'form':form})
def achievements_view(request):
    data=achievements.objects.all()
    return render(request,'achievements_view.html',{'data':data}) 
def update_achievements(request,id):
    data=achievements.objects.get(id=id)
    form=achievements_form(instance=data)
    if request.method=='POST':
        form=achievements_form(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('achievements_view')
    return render(request,'achievements_update.html',{'form':form})
def del_achievements(request,id):
    achievements.objects.get(id=id).delete()
    return redirect('achievements_view')

def management_add(request):
    form=management_form()
    if request.method=='POST':
        form=management_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('management_add')
    return render(request,'management_add.html',{'form':form})
def management_view(request):
    data=management.objects.all()
    return render(request,'management_view.html',{'data':data}) 
def update_management(request,id):
    data=management.objects.get(id=id)
    form=management_form(instance=data)
    if request.method=='POST':
        form=management_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('management_view')
    return render(request,'management_update.html',{'form':form})
def del_management(request,id):
    management.objects.get(id=id).delete()
    return redirect('management_view')

def teachers_add(request):
    form=teachers_form()
    if request.method=='POST':
        form=teachers_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('teachers_add')
    return render(request,'teachers_add.html',{'form':form})
def teachers_view(request):
    data=teachers.objects.all()
    return render(request,'teachers_view.html',{'data':data}) 
def update_teachers(request,id):
    data=teachers.objects.get(id=id)
    form=teachers_form(instance=data)
    if request.method=='POST':
        form=teachers_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('teachers_view')
    return render(request,'teachers_update.html',{'form':form})
def del_teachers(request,id):
    teachers.objects.get(id=id).delete()
    return redirect('teachers_view')

def contestlist(request):
    data=contest.objects.all()
    return render(request,'contest_list.html',{'data':data})

def participantlist(request):
    Contest_Name=request.GET.get('Contest_Name')
    participants=participant.objects.all()
    if Contest_Name:
        participants=participants.filter(Contest_Name__icontains=Contest_Name)
    context={
        'form':ContestFilterForm(),
        'data':participants
    }
    return render(request,'participant_lists.html',context)

def judgeslist(request):
    data=judges.objects.all()
    return render(request,'judges_list.html',{'data':data})

def resultlist(request):
    data=result.objects.all()
    return render(request,'result.html',{'data':data})

def guestlist(request):
    data=guests.objects.all()
    return render(request,'guest.html',{'data':data})

def programlist(request):
    data=performer.objects.all()
    return render(request,'program.html',{'data':data})

def venue_vol(request):
    data=venue.objects.all()
    data=volunteers.objects.all()
    return render(request,'venue_vol.html',{'data':data})
def programlist(request):
    data=performer.objects.all()
    return render(request,'program.html',{'data':data})

def photoshop(request):
    data=gallery.objects.all()
    return render(request,'photoshop.html',{'data':data})

def school_achievements(request):
    data=achievements.objects.all()
    return render(request,'achievements.html',{'data':data})

def tchrs(request):
    data=teachers.objects.all()
    return render(request,'teachers.html',{'data':data})

def mngmnt(request):
    data=management.objects.all()
    return render(request,'management.html',{'data':data})

def achievements_add(request):
    form=achievements_form()
    if request.method=='POST':
        form=achievements_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('achievements_add')
    return render(request,'achievements_add.html',{'form':form})
def achievements_view(request):
    data=achievements.objects.all()
    return render(request,'achievements_view.html',{'data':data}) 

# def contest_search(request):
#     participants = participant.objects.all()

#     if 'contest_name' in request.GET:
#         contest_name_query = request.GET['contest_name']
#         participants = participants.filter(Contest_Name__Name__icontains=contest_name_query)

#     return render(request, 'participant_lists.html', {'participants': participants})
# def contest_search(request):
#     data=participant.objects.get(name='')
#     contestFilter=ContestFilter(request.GET,queryset=data)
#     data=contestFilter.qs
#     context = {
#         'data': data,
#         'contestFilter': contestFilter
#     }
#     return render(request,'participant_lists.html',context)

def feedbacks_add(request):
    form=feedback_form()
    if request.method=='POST':
        form=feedback_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'feedback_add.html',{'form':form})

    
    
def feedbacks_view(request):
    data=feedbacks.objects.all()
    return render(request,'feedback_view.html',{'data':data}) 

def aboutpage(request):
    return render(request,'about.html')

def supportpage(request):
    return render(request,'support.html')

def contactpage(request):
    form=contactform()
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    return render(request,'contact.html',{'form':form})
def success(request):
    return HttpResponse("Success!")


# def custom_filter(quaryset,value):
#     return quaryset.filter(participant(Contest_Name=value))

# def my_view(request):
#     queryset=participant.objects.all()
#     my_filter=MyFilter(request.Get,queryset=queryset)
#     filtered_queryset=my_filter.qs
#     return render(request,'participant_lists.html',{'queryset':filtered_queryset})  




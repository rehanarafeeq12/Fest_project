from django import forms
from django.contrib.auth.forms import UserCreationForm

from Fest_app.models import School, Student, User, achievements, contact, contest, feedbacks, gallery, guests, judges, management, participant, performer, programmes, result, teachers, venue, volunteers

class DateInput(forms.DateInput):
    input_type='date'


class UserReg(UserCreationForm):
    username=forms.EmailField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password1','password2')

class SchoolReg(forms.ModelForm):
    class Meta:
        model=School
        exclude=('user','approval_status')
class StudentReg(forms.ModelForm):
    DOB=forms.DateField(widget=DateInput)
    class Meta:
        model=Student
        exclude=('user','approval_status')
class contest_list(forms.ModelForm):
    class Meta:
        model=contest
        fields='__all__'
class participant_list(forms.ModelForm):
    class Meta:
        model=participant
        fields='__all__'
class judges_list(forms.ModelForm):
    class Meta:
        model=judges
        fields='__all__'
class result_list(forms.ModelForm):
    class Meta:
        model=result
        fields='__all__'
class programmes_list(forms.ModelForm):
    class Meta:
        model=programmes
        fields='__all__'
class performers_list(forms.ModelForm):
    class Meta:
        model=performer
        fields='__all__'
class venue_list(forms.ModelForm):
    class Meta:
        model=venue
        fields='__all__'
class volunteers_list(forms.ModelForm):
    class Meta:
        model=volunteers
        fields='__all__'
class guests_form(forms.ModelForm):
    class Meta:
        model=guests
        fields='__all__'
class gallery_form(forms.ModelForm):
    class Meta:
        model=gallery
        fields='__all__'
class achievements_form(forms.ModelForm):
    class Meta:
        model=achievements
        fields='__all__'
class management_form(forms.ModelForm):
    class Meta:
        model=management
        fields='__all__'
class teachers_form(forms.ModelForm):
    class Meta:
        model=teachers
        fields='__all__'
        
class feedback_form(forms.ModelForm):
    class Meta:
        model=feedbacks
        fields='__all__'   
   
class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'   

class ContestFilterForm(forms.Form):
    Contest_Name=forms.CharField()

        
        


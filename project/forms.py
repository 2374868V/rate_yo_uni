from django import forms
from django.contrib.auth.models import User
from project.models import Bathroom

class BathroomForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           help_text="Please enter the bathroom name.")
    building = forms.CharField(max_length=100, help_text="Please enter the name of the building")
    level = forms.CharField(max_length=4, help_text="Please enter on which level the bathroom is situated" )


    gender = forms.ChoiceField(choices=[('M', 'Male'),('F', 'Female'),('N','Neutral')])
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Bathroom
        fields = ('name', 'building', 'level', 'gender')
       
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:

        #model = UserProfile
        fields = ('website', 'picture')

from django import forms
from django.contrib.auth.models import User
from project.models import *


class BathroomForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           help_text="Please enter the bathroom name.")
    building = forms.CharField(max_length=100, help_text="Please enter the name of the building")
    level = forms.CharField(max_length=4, help_text="Please enter on which level the bathroom is situated")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neutral')])
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    b_slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Bathroom
        fields = ('name', 'building', 'level', 'gender', 'b_slug')

       
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

        model = UserProfile
        fields = ('website', 'picture')


class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(help_text="Enter single digit rating out of five", max_value=5, min_value=0)
    user = forms.CharField(required=True, widget=forms.HiddenInput())
    bathroom = forms.CharField(required=True, widget=forms.HiddenInput())

    class Meta:
        model = Rate
        fields = ('rating', 'bathroom', 'user')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    user = forms.CharField(required=True, widget=forms.HiddenInput())
    bathroom = forms.CharField(required=True, widget=forms.HiddenInput())
    date = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('comment', 'bathroom', 'user')

from django import forms
from project.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class BathroomForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           help_text="Please enter the bathroom name.")
    building = forms.CharField(max_length=100, help_text="Please enter the name of the building")
    level = forms.CharField(max_length=4, help_text="Please enter on which level the bathroom is situated")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Neutral')])
    bSlug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Bathroom
        fields = ('name', 'building', 'level', 'gender', 'bSlug')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    user = forms.CharField(widget=forms.HiddenInput())
    bathroom = forms.CharField(widget=forms.HiddenInput())
    date = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('comment', )


class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(help_text="Enter single digit rating out of five", max_value=5)
    user = forms.CharField()
    bathroom = forms.CharField()

    class Meta:
        model = Rate
        fields = ('rating', )

from django import forms
from project.models import *


class BathroomForm(forms.ModelForm):
    name = forms.CharField(max_length=20,
                           help_text="Please enter the bathroom name.")
    building = forms.CharField(max_length=100, help_text="Please enter the name of the building")
    level = forms.CharField(max_length=4, help_text="Please enter on which level the bathroom is situated")

    gender = forms.ChoiceField(choices=[('M', 'Male'),('F', 'Female')])
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Bathroom
        fields = ('name', 'building', 'level', 'gender')


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    date = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('comment', )

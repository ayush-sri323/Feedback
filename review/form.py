from django import forms
from django.forms import fields
from .models import Review
"""
class ReviewForms(forms.Form):
    user_name = forms.CharField(label='Your Name',required= True,error_messages={
        "required" :'your name must not be empty'
    })
    review_text = forms.CharField(label='your review',widget=forms.Textarea)
    rating = forms.IntegerField(label='your rating',min_value=1,max_value=5)
"""
class ReviewForms(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        error_message = {
           'rating' : { 'max_value' : 5}
        }

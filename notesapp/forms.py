from django import forms
from .models import *

class notestableForm(forms.ModelForm):
   class Meta:
       model = notestable
       fields = "__all__" 

from django import forms
from djangomodelform.model import studenteMobilis


class EmpForm(forms.ModelForm):
    class Meta:
        model = studenteMobilis
        fields = "__all__"
        widgets = {'firstname': forms.TextInput(attrs={'placeholder': 'Enter your firstname'}),
                   'lastname': forms.TextInput(attrs={'placeholder': 'Enter your lastname'}),
                   'age': forms.TextInput(attrs={'placeholder': 'Enter your age'}),
                   'gender': forms.TextInput(attrs={'placeholder': 'specify:''male/female'})
                   }

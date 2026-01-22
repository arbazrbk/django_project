from django import forms
from myapp.models import Student



class StudentForm(forms.ModelForm):
    class meta:
        model = Student
        list_fields = ['name', 'roll_no', 'email', 'phone_number', 'department']    
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
            'roll_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Roll Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Your Phone Number'}),
            'department':forms.Select(attrs={'class':'form-control'}),
        }
from django import forms 
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['title','author','genre','published_date','isbn_number','description']
        
    widgets = {
        'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Book Title'}),
        'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Author Name'}),
        'genra': forms.Select(attrs={'class':'form-control', 'placeholder':'Select Genra'}),
        'published_date': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Select Published Date'}),
        'isbn_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter ISBN Number'}),
        'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Book Description'}),  
    }
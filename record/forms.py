from django import forms

from .models import Record, Book

class RecordForm(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required =True)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required = True)
    class Meta:
        model = Record
        fields = [
            "location","text",
            ]


class BookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required =True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = True)
    #phonenumber=forms.PhoneNumberField(widget=forms.Textarea(attrs={'class': 'form-control'}), required = True)
    phonenumber=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required = True)

    class Meta:
        model = Book
        fields = [
            "name","email","phonenumber",
            ]

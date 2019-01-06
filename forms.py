from django import forms

class ListForm(forms.Form):
    text=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Add Item','aria-label':'Search','name':'Item'}))
        

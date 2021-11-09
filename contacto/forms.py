from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label='Nombre', required=True, max_length=50)

    email = forms.CharField(label='Email', required=True, max_length=100)

    contenido = forms.CharField(label='Contenido', max_length=400, widget=forms.Textarea)

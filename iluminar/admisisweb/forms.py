from django import forms

#Formulario para obtener nombre y contraseña 
class LoginForm(forms.Form):
    usuario = forms.CharField(label='Nombre de usuario')
    passd = forms.CharField(label='Contraseña', widget=forms.PasswordInput)



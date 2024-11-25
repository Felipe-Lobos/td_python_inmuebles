from django import forms
from gestion_inmuebles.models import Usuario,Inmueble

class UsuarioForm(forms.ModelForm):
    """Form definition for Usuario."""
    class Meta:
        """Meta definition for Usuarioform."""
        model = Usuario
        fields = ('nombres','apellidos','rut','username','password','tipo_usuario')
    
    def save(self, commit=True):
        print('form user save')
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            print('user  save')
        return user

class ProfileForm(forms.ModelForm):
    """Form definition for Profile."""

    class Meta:
        """Meta definition for Profileform."""
        model = Usuario
        #fields = "__all__"
        fields = ["nombres", "apellidos", "rut","direccion","telefono","tipo_usuario"]
        #exclude = ["title"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_usuario'].disabled = True


class InmuebleForm(forms.ModelForm):
    """Form definition for Inmueble."""

    class Meta:
        """Meta definition for Inmuebleform."""

        model = Inmueble
        fields = "__all__"
        exclude = ['dueño']
       
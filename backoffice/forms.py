from django import forms
from .models import Auteur, Livre


class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = ['prenom', 'nom', 'nationalite']
        widgets = {
            'prenom': forms.TextInput(attrs={'placeholder': 'Prénom'}),
            'nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'nationalite': forms.TextInput(attrs={'placeholder': 'Nationalité (optionnel)'}),
        }


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['nom', 'auteur', 'prix', 'livre_type', 'livre_status']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Titre du livre'}),
            'prix': forms.NumberInput(attrs={'placeholder': 'Prix (€)', 'step': '0.01'}),
        }

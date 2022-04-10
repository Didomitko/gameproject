from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from game_app.game_accounts.models import Profile
from game_app.common.helps import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField()
    data_of_birth = forms.DateField()
    description = forms.CharField(
        widget=forms.Textarea
    )
    email = forms.EmailField()
    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            data_of_birth=self.cleaned_data['data_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'ENTER URL',
                }
            )
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class EditProfileForm(BootstrapFormMixin, ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = get_user_model()
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'ENTER name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'ENTER second name'
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'ENTER URL'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'ENTER @mail.bg'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'ENTER description',
                    'rows': 3,
                }
            ),
            'gender': forms.Select(
                choices=Profile.GENDERS,
            ),
            'data_of_birth': DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # taka ne e dobre trqbwa da e s signali za da trie snimkite na potrebitelq
        pets = list(self.instance.pet_set.all())
        # ResultProfil.objects.filter(tagged_result__in=result).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()


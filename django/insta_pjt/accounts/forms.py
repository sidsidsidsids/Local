from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username','email','first_name','last_name')

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('nickname','introduction')

    def save(self, user):
        try:
            profile = user.profile
        except Profile.DoesNotExist:
            profile = Profile(user-user)
        profile.nickname = self.cleaned_data['nickname']
        profile.introduction = self.cleaned_data['introduction']
        profile.save()
        return profile
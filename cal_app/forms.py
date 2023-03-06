# django imports
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User
# local imports
from .models import Food,Profile


 
class SelectFoodForm(forms.ModelForm):
    """ used to select the food item """
    class Meta:
        model = Profile
        fields = ('food_selected','quantity',)

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['food_selected'].queryset = Food.objects.all() #filter(person_of=user)


class ProfileForm(forms.ModelForm):
    """ used to get user information like calorie goal for that day """
    class Meta:
        model = Profile
        fields = ('calorie_goal',)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


    
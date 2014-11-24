from django import forms
from product_finder.models import Request,Category, UserProfile
from django.contrib.auth.models import User

class RequestForm(forms.ModelForm):
	requester = forms.CharField(widget=forms.HiddenInput(),required=False)
	category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.MultipleHiddenInput(),required=False)
	product_name = forms.CharField(max_length=256,help_text="Please enter product's name.")
	product_brand = forms.CharField(max_length=256,help_text="Please enter product's brand. (Enter 'none' if there isn't one.)")
	product_quantity = forms.IntegerField(help_text="Please enter the quantity that you are looking for.")
	description = forms.CharField(max_length=600,help_text="Please enter a short description.")
	area_local = forms.BooleanField(help_text="At local stores",required=False)
	area_online = forms.BooleanField(help_text="At an on-line stores",required=False)
	completed = forms.BooleanField(widget=forms.HiddenInput(),required=False)
	class Meta:
		model = Request
		fields = ('product_name', 'product_brand', 'product_quantity', 'area_local', 'area_online','description')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'phone', 'city', 'country')

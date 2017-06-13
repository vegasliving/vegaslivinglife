from django import forms

class PodioForm(forms.Form):
	firstName= forms.CharField(label="First Name", max_length=300, widget = forms.TextInput(attrs={"class":"mdl-textfield__input"}))
	lastName = forms.CharField(label="Last Name", max_length=300, widget = forms.TextInput(attrs={"class":"mdl-textfield__input"}))
	email = forms.EmailField(label="Email",  widget = forms.TextInput(attrs={"class":"mdl-textfield__input"}))
	phone = forms.IntegerField(label="Phone", widget = forms.TextInput(attrs={"class":"mdl-textfield__input"}))

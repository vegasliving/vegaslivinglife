from django import forms

class PodioForm(forms.Form):
	firstName= forms.CharField(label="First Name", max_length=300, widget = forms.TextInput(attrs={"class":"mdl-textfield__input", "style":"width: 100%; border-bottom: 2px solid #2d3739; margin: 5px 0px"}))
	lastName = forms.CharField(label="Last Name", max_length=300, widget = forms.TextInput(attrs={"class":"mdl-textfield__input", "style":"width: 100%; border-bottom: 2px solid #2d3739; margin: 5px 0px" }))
	email = forms.EmailField(label="Email",  widget = forms.TextInput(attrs={"class":"mdl-textfield__input", "style":"width: 100%; border-bottom: 2px solid #2d3739; margin: 5px 0px"}))
	phone = forms.IntegerField(label="Phone", widget = forms.TextInput(attrs={"class":"mdl-textfield__input", "style":"width: 100%; border-bottom: 2px solid #2d3739; margin: 5px 0px"}))

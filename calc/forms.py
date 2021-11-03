from django import forms

class Calc(forms.Form):
	number1 = forms.IntegerField(label="عدد اول")
	number2 = forms.IntegerField(label="عدد دوم")
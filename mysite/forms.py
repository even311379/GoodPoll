from django import forms
from mysite import models
# from captcha.fields import CaptchaField

class PollItemForm(forms.ModelForm):
	# captcha = CaptchaField()
	class Meta:
		model = models.PollItem
		fields = ['name']

	def __init__(self, *args, **kwargs):
		super(PollItemForm,self).__init__(*args, **kwargs)
		self.fields['name'].label = '投票選項1'
		self.fields['name'].label = '投票選項2'
		self.fields['name'].label = '投票選項2'
		self.fields['name'].label = '投票選項4'


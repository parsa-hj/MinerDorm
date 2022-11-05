from django.forms import ModelForm
from .models import Review

class DormForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


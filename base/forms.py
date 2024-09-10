from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']



# class ProfileForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['fullname', 'username']
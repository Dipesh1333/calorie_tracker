# django imports
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# local imports
from .models import Profile

# to create auto profile when user register
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(person_of=instance)
		print("profile created")

post_save.connect(create_profile,sender=User)


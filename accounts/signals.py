from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Setting


from .models import Account

def account_profile(sender, instance, created, **kwargs):
	if created:
		# group = Group.objects.get(name='customer')
		group, created = Group.objects.get_or_create(name='guest')
		instance.groups.add(group)
		Account.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

		# Create a default Setting instance for the new Account
		Setting.objects.create(
			account=instance.account,
			name = 'theme',
			value = 'light',
		)
		print('Setting created!')

post_save.connect(account_profile, sender=User)
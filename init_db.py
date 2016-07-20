"""
Initialize the Database, User, Groups, Permissions.
"""
from django.contrib.auth.models import User, Group, Permission
from rms_app.models import Gericht

# Create Super User
superuser = User.objects.create_superuser(username='superuser',
                                          first_name="vorname_superuser",
                                          last_name="nachname_superusert",
                                          password='django_test',
                                          email="test@web.de")
superuser.save()


gericht = Gericht.objects.create(gericht_name="Spaghetti")
gericht.save()
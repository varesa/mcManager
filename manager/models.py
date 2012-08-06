from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

#class Meta:
#    app_label="servermanager"

# Create your models here.
class Perms(models.Model):
    #user = models.OneToOneField(User)
    class Meta:
	permissions = (
            ('index_view', 'Can view the Admin-page.'),
            ('users_view', 'Can view users.'),
            ('users_write','Can modify users.'),
        )

class Server(models.Model):
    #class Meta:
        #permissions = (
        #    ('admin_index_view', '!Can view the Admin-page'),
        #    ('admin_users_view', '!Can view users'),
        #    ('admin_users_write','!Can modify users'),
        #)
    name = models.CharField(max_length=50)
    port = models.PositiveIntegerField()
    
    path = models.CharField(max_length=300)
    
    command = models.CharField(max_length=100)

    #state = models.CharField(max_length=15, choices=(
#        (u'S', u'Stopped'),
#        (u'R', u'Running'),
#        (u'E', u'Error'),
        
#    ))
    
    owners = models.ManyToManyField(User) # 'name' allows relation to be specified before the object itself
    
    def __unicode__(self):
        return self.name
    
#class Person(models.Model):
#    name = models.CharField(max_length=50)
#    
#    def __unicode__(self):
#        return self.name

admin.site.register(Server)
#admin.site.register(Person)


class SettingsGroup(models.Model):
    name = models.CharField(max_length=50)

class Setting(models.Model):
    group = models.ForeignKey(SettingsGroup)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name + ': ' + self.value

admin.site.register(SettingsGroup)
admin.site.register(Setting)

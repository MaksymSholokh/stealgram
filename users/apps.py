from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users' 


#more effective use to create togather user+profile 
    # def ready(self):
    #     import users.signals  

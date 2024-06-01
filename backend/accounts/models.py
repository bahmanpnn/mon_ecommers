from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email=models.EmailField(max_length=127,unique=True)
    phone_number=models.CharField(max_length=11,unique=True)
    fullname=models.CharField(max_length=127)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=True)
    
    objects=UserManager() 
    
    # this is for authenticating user and we want to change default(username)
    USERNAME_FIELD='phone_number' 
    # fields use for creating user in cli,default username_field is in and
    # does not need to add to fields
    REQUIRED_FIELDS=['fullname','email']

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        'user has a specific permission? add in this method'
        return True
    
    def has_module_perms(self,app_lable):
        'user has a permission to view the app? add app_lable in this method'
        return True

    @property    
    def is_staff(self):
        'is user a staff? check is_admin of user,because every admin is staff'
        return self.is_admin
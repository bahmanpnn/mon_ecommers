from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email=models.EmailField(max_length=127,unique=True)
    phone_number=models.CharField(max_length=11,unique=True)
    fullname=models.CharField(max_length=127)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    
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
    

class OtpCode(models.Model):
    '''
        one time password is for authenticating user after registration with phone number.
        we can connect phone number in this model with user models phone number but it does not need.

        first we want authenticate user in next view then we get code that user fills and
        we create user object.
    '''

    phone_number=models.CharField(max_length=11,unique=True)
    code=models.PositiveSmallIntegerField()
    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created_date}'
    
    
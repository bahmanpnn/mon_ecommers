from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    '''
        this manager uses for creating user and we can use it in views after receiving datas with form
        new_user=create_user(cd['phone_number'],cd['email'],...)
    '''
    def create_user(self,phone_number,email,fullname,password):
        if not phone_number:
            raise ValueError('user must have phone number')

        if not email:
            raise ValueError('user must have email')

        if not fullname:
            raise ValueError('user must have fullname')
        
        user=self.model(phone_number=phone_number,email=self.normalize_email(email),fullname=fullname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone_number,email,fullname,password):
        user=self.create_user(phone_number,email,fullname,password)
        user._is_admin=True
        user.save(using=self._db)
        return user
    


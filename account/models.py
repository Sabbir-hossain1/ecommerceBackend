from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, fullName, email, tc, date_of_birth=None, password=None, confirm_password=None):    
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            fullName=fullName,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            tc=tc,            
            )            
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, fullName, email, tc, date_of_birth=None, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            fullName=fullName, 
            email=self.normalize_email(email),
            tc=tc,
            date_of_birth=None,
            password=password,
            confirm_password=None            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    fullName = models.CharField(("Full Name: "), max_length=50)
    email = models.EmailField(verbose_name="email address",max_length=255,unique=True,)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"),auto_now_add=False, blank=True, null=True)
    tc = models.BooleanField(("Terms & Condition: "), default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullName','tc']

    def __str__(self):
        return self.email
    
    def get_user(self, user_id):
        try:
            return self.objects.get(pk=user_id)
        except self.DoesNotExist:
            return None

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    additional_mail = models.CharField(max_length=50, blank=True, null=True)
    phoneNumber = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)

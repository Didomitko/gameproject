import datetime

from django.contrib.auth import models as auth_models

# 1. create models
# 2. Config this models in settings.py
# 3. Create user manager
from django.core.validators import MinLengthValidator

from django.db import models

from game_app.game_accounts.managers import GameUserManager
from game_app.common.validators import only_letters_validator


class GameUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = GameUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    # @property
    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    picture = models.URLField()
    # photo = cloudinary_models.CloudinaryField('image') ----from cloudinary

    data_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # @property  # За дата на раждане в welcome.html
    # def age(self):
    #     return datetime.datetime.now().year - self.data_of_birth.year
    #
    # class Meta:
    #     unique_together = ('user', 'name')

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )

    user = models.OneToOneField(
       GameUser,
       on_delete=models.CASCADE,   #да изтрива узера
       primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

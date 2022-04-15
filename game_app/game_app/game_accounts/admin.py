from django.contrib import admin
from django.contrib.auth import get_user_model

from game_app.game_accounts.models import Profile, GameQuests

UserModel = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(GameQuests)
class GameAdmin(admin.ModelAdmin):
    pass


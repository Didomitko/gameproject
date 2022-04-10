from django.urls import path

from game_app.game_accounts.views import ProfileDetailsView, UserLoginView, UserRegisterView, WelcomeView, HomeView, \
    EditProfileView, DeleteProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),


    path('login/', UserLoginView.as_view(), name='login user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('confirm/', UserConfirmView.as_view(), name='confirm'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),

]
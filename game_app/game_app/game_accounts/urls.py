from django.urls import path

from game_app.game_accounts.views import ProfileDetailsView, UserLoginView, UserRegisterView, WelcomeView, HomeView, \
    EditProfileView, DeleteProfileView, UserLogoutView, ErrorLogin

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('401/', ErrorLogin.as_view(), name='401'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),


    path('login/', UserLoginView.as_view(), name='login user'),
    path('logiout/<int:pk>', UserLogoutView.as_view(), name='logout user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('confirm/', UserConfirmView.as_view(), name='confirm'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('profile/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),


]
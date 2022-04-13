from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView

from game_app.game_accounts.forms import CreateProfileForm, DeleteProfileForm, EditProfileForm
from game_app.game_accounts.models import Profile
from game_app.common.view_mixins import RedirectToWelcome
from django.views.generic import TemplateView, ListView
from django.views.generic import edit as edit_profile


class UserRegisterView(RedirectToWelcome, CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('index')


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('welcome')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(edit_profile.UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('welcome')


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


class HomeView(RedirectToWelcome, TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class WelcomeView(ListView):
    model = Profile
    template_name = 'main/welcome.html'
    context_object_name = 'welcome'


class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'main/home_page.html'
    success_url = reverse_lazy('index')
    form_class = DeleteProfileForm


class UserLogoutView(LogoutView):
    model = Profile
    template_name = 'main/home_page.html'
    success_url = reverse_lazy('index')

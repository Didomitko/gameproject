from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView

from game_app.game_accounts.forms import CreateProfileForm
from game_app.game_accounts.models import Profile
from game_app.common.view_mixins import RedirectToWelcome
from django.views.generic import TemplateView, ListView
from django.views.generic import edit as edit_profile

# from petstagram.main.models import PetPhoto

class UserRegisterView(RedirectToWelcome, CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('welcome')


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
    context_object_name = 'profile'


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pets = list(Pet.objects.filter(user_id=self.object.user_id))
    #
    #     pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    #     # .filter(tagged_pets__user_profile=profile).distinct()
    #
    #     total_likes_count = sum(x.likes for x in pet_photos)
    #     total_pet_photos_count = len(pet_photos)
    #
    #     context.update(
    #         {
    #             'total_likes_count': total_likes_count,
    #             'total_pet_photos_count': total_pet_photos_count,
    #             'is_owner': self.object.user_id == self.request.user.id,
    #             'pets': pets,
    #         }
    #     )
    #     return context


class HomeView(RedirectToWelcome, TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class WelcomeView(HomeView):

    template_name = 'main/welcome.html'
    context_object_name = 'welcome'


# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'main/profile_edit.html')
#
#
class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('welcome')

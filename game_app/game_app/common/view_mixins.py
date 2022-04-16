from django.shortcuts import redirect


class RedirectToWelcome:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('welcome')
        # else:
        #     return redirect('401')
        return super().dispatch(request, *args, **kwargs)


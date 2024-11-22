from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator

class BaseTemplateView(TemplateView):
    template_name = "base.html"

@method_decorator(login_not_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('panel')
        return super(HomeView, self).dispatch(request, *args, **kwargs)

from django.shortcuts import redirect
from django.views.generic import TemplateView

class BaseTemplateView(TemplateView):
    template_name = "base.html"

class HomeView(TemplateView):
    template_name = "home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('panel')
        return super(HomeView, self).dispatch(request, *args, **kwargs)

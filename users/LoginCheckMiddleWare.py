from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "users.AnalystLogin":
                    pass
                elif modulename == "users.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("Analyst_home"))
            elif user.user_type == "2":
                if modulename == "users.GenerAluSERloGIN":
                    pass
                elif modulename == "users.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("generalusers_home"))
            
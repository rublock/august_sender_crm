from django.urls import path
from accounts.forms import LoginUserForm
from accounts.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginUserForm), name='login'),
]

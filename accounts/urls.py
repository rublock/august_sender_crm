from django.urls import path
from accounts.forms import LoginUserForm
from accounts.views import CustomLoginView

from django.contrib.auth import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True,
                                           authentication_form=LoginUserForm), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='mainapp:home_page'), name='logout'),
]

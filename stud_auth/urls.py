from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView

from stud_auth.views import UserList, UserView, UserEditView, UserExtraEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/profile/', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    path('accounts/profile/<int:pk>/', login_required(UserView.as_view()), name='user'),
    path('accounts/profile/edit/', login_required(UserEditView.as_view()), name='profile_edit'),
    path('accounts/profile/edit/extra', login_required(UserExtraEditView.as_view()), name='profile_extra_edit'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='auth_logout'),
    path('accounts/', include('registration.backends.default.urls')),

    path('users/', login_required(UserList.as_view()), name='users'),
]

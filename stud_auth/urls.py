from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from stud_auth.views import UserList, UserView, UserEditView, UserExtraEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^accounts/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', login_required(UserView.as_view()), name='user'),
    url(r'^accounts/profile/edit/$', login_required(UserEditView.as_view()), name='profile_edit'),
    url(r'^accounts/profile/edit/extra$', login_required(UserExtraEditView.as_view()), name='profile_extra_edit'),
    url(r'^accounts/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^users/$', UserList.as_view(), name='users'),
]

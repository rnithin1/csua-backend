from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from apps.db_data.views import EventsView

urlpatterns = [
    path("nihti/", views.sikh_name, name="nihti"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

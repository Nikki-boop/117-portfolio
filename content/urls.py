from django.urls import path
from . import views
from .views import ProjectsListView, ProjectCreateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", ProjectsListView.as_view(), name="projects_list"),
    path("projects_new", ProjectCreateView.as_view(), name="projects_new"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url
from .views import projects_list, project_detail,\
project_create, project_update, template_2_pdf

urlpatterns = [
    url(r'^list/', projects_list, name="projects_list"),
    url(r'^details/', project_detail, name="project_detail"),
    url(r'^create/', project_create, name="project_create"),
    url(r'^update/', project_update, name="project_update"),
    url(r'^download/', template_2_pdf, name="template_2_pdf")
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("intro/", views.intro, name="introduction"),
    path("evidence/", views.evidence, name="evidence"),
    # path("data/", views.data, name="data"),
    path("drugrepurposing/", views.function, name="function"),
    path("tutorial/", views.tutorial, name="tutorial"),
    path("contact/", views.contact, name="contact"),
    # path("table_update/", views.table_update, name="table_update"),
    # path("test_ajax/", views.test_ajax,name="test_ajax"),
]

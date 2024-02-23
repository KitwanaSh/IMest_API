from django.urls import path
from . import views


urlpatterns = [
    path("json_response/", views.json_response),
    path("http_response/", views.http_response),
    path("profile/", views.userProfile),
    path("filters/<int:pk>", views.filter_queries),
    path("schedules/fetch_sch/", views.fetch_class_schedules),
    path("schedule/create/", views.create_class_schedule),
]
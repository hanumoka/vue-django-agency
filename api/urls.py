from django.urls import path

from api import views

app_name = "api"


urlpatterns = [
    # /blog/post/99/
    path("post/list/", views.ApiPostLV.as_view(), name="post_list"),
]

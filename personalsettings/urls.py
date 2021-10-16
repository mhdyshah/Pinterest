from django.urls import path

from personalsettings import views


urlpatterns = [
    path("profile/", views.PublicProfileView.as_view(), name="profile"),
    path("edit-profile/",
         views.PublicProfileUpdateView.as_view(), name="edit-profile"),
]

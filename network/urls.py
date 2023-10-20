
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("all_posts", views.all_posts, name="all_posts"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("follow/<int:target_user_id>", views.follow, name="follow"),
    path("unfollow/<int:target_user_id>", views.unfollow, name="unfollow"),
    path("following", views.following, name="following")
]
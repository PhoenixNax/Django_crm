from django.urls import path
from website import views

app_name = "website"

urlpatterns = [
  path("", views.home, name="home"),
  #path("login/", views.login_user, name="login"),
  path("logout/", views.logout_user, name="logout"),
  path("register/", views.register_user, name="register"),
  path("record/<int:record_id>/", views.customer_record, name="record"),
  path("delete/<int:record_id>/", views.delete_record, name="delete_record"),
  path("add_record/", views.add_record, name="add_record"),
  path("update_record/<int:record_id>/", views.update_record, name="update_record"),
]
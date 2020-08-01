from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("items/", views.items, name="items"),
    path("order/<int:inventory_id>", views.make_order, name="make_order"),
]

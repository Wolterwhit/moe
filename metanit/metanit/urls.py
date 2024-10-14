from django.contrib import admin
from django.urls import path
from hello import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("<int:my_id>/", views.indexItem, name="detail"),
    path("", views.index)
]
    

from django.urls import path
from . import views


app_name = 'myapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('pdf/<int:id>', views.audio, name="pdf"),
    path('del/<int:id>', views.delete, name="remove")
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<int:pk>/',views.detail,name='detail'),
    path('form/',views.new_post,name='new-form'),
    path('post/<int:pk>/update',views.update_form,name='update'),
]

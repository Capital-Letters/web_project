from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('article/<int:article_id>/', views.article_page),
    path('edit/<int:article_id>/',views.article_edit,name='edit_page'),
    path('edit/action',views.edit_action,name='edit_action'),
]
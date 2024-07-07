from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.index_page_1, name='name_index_page_1'),
    path('/b2', views.page_2, name='name_page_2'),
    path('/b3', views.page_3, name='name_page_3'),
]
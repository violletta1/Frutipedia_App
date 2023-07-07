from django.urls import path, include
from Frutipedia_App.frutipedia import views

urlpatterns = ([
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/', include([
        path('details/', views.profile_details, name='profile-details'),
        path('create/', views.profile_create, name='profile-create'),
        path('delete/', views.profile_delete, name='profile-delete'),
        path('edit/', views.profile_edit, name='profile-edit'),

    ])),

    path('create/', views.create_fruit, name='create-fruit'),
    path('<int:pk>/details/', views.fruit_details, name='fruit-details'),
    path('<int:pk>edit/', views.fruit_edit, name='fruit-edit'),
    path('<int:pk>delete/', views.fruit_delete, name='fruit-delete')
])

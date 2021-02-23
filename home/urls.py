from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signupUser, name='signup'),
    path('logout', views.logoutUser, name='logout'),
    path('addpost', views.add_post, name='addpost'),
    path('updatepost/<int:id>/', views.update_post, name='updatepost'),
    path('deletepost/<int:id>/', views.delete_post, name='deletepost')
    ]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
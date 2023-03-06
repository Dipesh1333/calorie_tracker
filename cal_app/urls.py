# django imports
from django.urls import path

from .views import HomePageView,LoginPage,LogOutPage,select_food,RegisterPage,ProfilePage,delete_food

urlpatterns = [
	path('', HomePageView,name='home'),
	path('select_food/',select_food,name='select_food'),
	path('delete_food/<str:pk>/',delete_food,name='delete_food'),
	path('profile/',ProfilePage,name='profile'),
	path('register/',RegisterPage,name='register'),
	path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
	
]
from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
		path('<slug>', views.IndexView, name='home'),
	]

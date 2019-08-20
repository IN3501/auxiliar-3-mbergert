from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path('form/', form, name='form'),
	path('github/', github, name='github'),
]

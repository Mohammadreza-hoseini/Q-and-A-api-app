from django.urls import path, include
from . import views
from . import api_views


app_name = 'core'

api_urls = [
	path('questions/', api_views.QuestionListView.as_view()),
	path('questions/create/', api_views.QuestionCreateView.as_view()),
	path('questions/update/<int:pk>/', api_views.QuestionUpdateView.as_view()),
	path('questions/delete/<int:pk>/', api_views.QuestionDeleteView.as_view()),
	path('answers/create/', api_views.AnswerCreateView.as_view()),
	path('answers/update/<int:pk>/', api_views.AnswerUpdateView.as_view()),
	path('answers/delete/<int:pk>/', api_views.AnswerDeleteView.as_view()),
]

urlpatterns = [
	path('', views.Home.as_view(), name='home'),
	path('api/', include(api_urls)),
]
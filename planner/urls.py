from django.urls import path
from .views import GenerateStudyPlanView


urlpatterns = [
    path('generate-plan/', GenerateStudyPlanView.as_view(), name='generate-plan'),
]

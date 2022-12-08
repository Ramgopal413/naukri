
from django.urls import path, include
from naukriapp.models import Job

from .views import SkillViewSet, JobViewSet,CompanyViewSet, ApplicantViewSet, ExperienceViewSet, QualificationViewSet

from .views import RecruiterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'recruitor', RecruiterViewSet, basename='recruiter')
router.register(r'skill', SkillViewSet, basename='skill')
# router.register(r'job', JobViewSet, basename='job')
router.register(r'applicant', ApplicantViewSet, basename='applicant')
router.register(r'experience', ExperienceViewSet, basename='experience')
router.register(r'qualification', QualificationViewSet, basename='qualificaton')


urlpatterns = [
    path('', include(router.urls)),
]


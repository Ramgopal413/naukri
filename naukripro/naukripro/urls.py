
from django.contrib import admin
from django.urls import path, include
from naukriapp.views import Excel, JobViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('job',JobViewSet,basename='JobAdmin')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('naukriapp.urls')),
    path("api/",include(router.urls)),
    path("auth/",include('rest_framework.urls',namespace='rest_framework')),
    path("excel/",Excel.as_view())

]

from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register ViewSet with Router
router.register('getbill', views.GetBillViewSet, basename='getbill')
router.register('tenant', views.TenantViewSet, basename='tenant')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

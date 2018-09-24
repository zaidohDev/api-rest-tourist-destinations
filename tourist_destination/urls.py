"""tourist_destination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.api.viewSets import TouristDestinationViewSet
from tourist_equipment.api.viewSets import TouristEquipmentViewSet
from comments.api.viewSets import CommentViewSet
from locality.api.viewSets import LocalityViewSet
from assessments.api.viewSets import AssessmentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'tourist_destination', TouristDestinationViewSet, base_name='tourist_destination')
router.register(r'tourist_equipment', TouristEquipmentViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'localities', LocalityViewSet)
router.register(r'assessments', AssessmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamMemberView

router = DefaultRouter()
router.register('member', TeamMemberView)

urlpatterns = [
    path('v1/', include(router.urls))
]
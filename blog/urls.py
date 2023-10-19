from blog.views import BlogView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog-list', BlogView)

urlpatterns = [
    path('v1/', include(router.urls))
]
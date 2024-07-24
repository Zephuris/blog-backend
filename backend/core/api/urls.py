from rest_framework.routers import DefaultRouter
from blog.api.urls import blog_router
from django.urls import path,include

router = DefaultRouter()
router.registry.extend(blog_router.registry)

urlpatterns =  [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
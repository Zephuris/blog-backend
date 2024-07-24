from rest_framework_nested import routers
from . import views

blog_router = routers.DefaultRouter()

blog_router.register('post',views.PostViewSet,basename='post')
blog_router.register('comment',views.CommentViewSet,basename='comment')
blog_router.register('category',views.CategoryViewSet,basename='category')

# router.register('author',views.AuthorViewSet)
# router.register('category',views.CategoryViewSet,basename='category')

urlpatterns = blog_router.urls
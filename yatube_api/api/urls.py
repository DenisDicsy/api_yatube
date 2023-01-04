from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

app_name = "api"

router_v1 = DefaultRouter()
router_v1.register(r"posts", PostViewSet, basename="post")
router_v1.register(r"groups", GroupViewSet, basename="group")
router_v1.register(
    r"posts\/(?P<post_id>\d+)\/comments", CommentViewSet, basename="comment"
)


urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/api-token-auth/", obtain_auth_token),
]

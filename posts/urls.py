from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SharePostViewSet,
    SharePostCommentViewSet,
    HelpPostViewSet,
    HelpPostCommentViewSet,
)

router = DefaultRouter()
router.register(r'share-posts', SharePostViewSet, basename='share-posts')
router.register(r'help-posts', HelpPostViewSet, basename='help-posts')

urlpatterns = [
    path('', include(router.urls)),

    # SharePost comments
    path(
        'share-posts/<int:share_post_id>/comments/',
        SharePostCommentViewSet.as_view({
            'get': 'list',
            'post': 'create',

        }),
    ),
path(
    'share-posts/<int:share_post_id>/comments/<int:pk>/',
    SharePostCommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }),
),
    # HelpPost comments
    path(
        'help-posts/<int:help_post_id>/comments/',
        HelpPostCommentViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
    ),
]
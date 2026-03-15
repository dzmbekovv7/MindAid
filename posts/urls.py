from django.urls import path
from . import views

urlpatterns = [
    path('share-posts/', views.GetSharePosts.as_view()),
    path('share-posts/<int:share_post_id>/comments/', views.GetSharePostComments.as_view()),
    path('share-posts/create/', views.CreateSharePost.as_view()),
    path('share-posts/update/', views.ChangeSharePost.as_view()),
    path('share-posts/create/<int:share_post_id>/comment/', views.CreateSharePostComment.as_view()),
]
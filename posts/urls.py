from django.urls import path
from . import views

urlpatterns = [
    path('share-posts/', views.GetSharePosts.as_view()),
    path('share-posts/<int:share_post_id>/comments/', views.GetSharePostComments.as_view()),
    path('share-posts/create/', views.CreateSharePost.as_view()),
    path('share-posts/<int:pk>/update/', views.ChangeSharePost.as_view()),
    path('share-posts/<int:pk>/delete/', views.DeleteSharePost.as_view()),
    path('share-posts/create/<int:share_post_id>/comment/', views.CreateSharePostComment.as_view()),

    path('help-posts/', views.GetHelpPosts.as_view()),
    path('help-posts/<int:help_post_id>/comments/', views.GetHelpPostComments.as_view()),
    path('help-posts/create/', views.CreateHelpPost.as_view()),
    path('help-posts/create/<int:help_post_id>/comment/', views.CreateHelpPostComment.as_view()),
    path('help-posts/<int:pk>/update/', views.ChangeHelpPost.as_view()),
    path('help-posts/<int:pk>/delete/', views.DeleteHelpPost.as_view()),
]
from django.shortcuts import render
from rest_framework import generics
from .models import SharePost, SharePostComment
from .serializers import GetSharePostsSerializer, GetSharePostCommentsSerializer, CreateSharePostSerializer, UpdateSharePostSerializer, CreateSharePostCommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class GetSharePosts(generics.ListAPIView):
    queryset = SharePost.objects.all()
    serializer_class = GetSharePostsSerializer
    permission_classes = [AllowAny]

class GetSharePostComments(generics.ListAPIView):
    serializer_class = GetSharePostCommentsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        share_post_id = self.kwargs['share_post_id']
        return SharePostComment.objects.filter(share_post_id=share_post_id)

class CreateSharePost(generics.CreateAPIView):
    serializer_class = CreateSharePostSerializer
    permission_classes = [IsAuthenticated]

class ChangeSharePost(generics.UpdateAPIView):
    serializer_class = UpdateSharePostSerializer
    permission_classes = [IsAuthenticated]

class CreateSharePostComment(generics.CreateAPIView):
    serializer_class = CreateSharePostCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        share_post_id = self.kwargs['share_post_id']
        share_post = SharePost.objects.get(id=share_post_id)

        serializer.save(user=self.request.user,share_post=share_post)
from django.shortcuts import render
from rest_framework import generics
from .models import SharePost, SharePostComment, HelpPost, HelpPostComment
from .serializers import (GetSharePostsSerializer, GetSharePostCommentsSerializer,
                          CreateSharePostSerializer, UpdateSharePostSerializer,
                          CreateSharePostCommentSerializer, GetHelpPostsSerializer,
                          GetHelpPostCommentsSerializer, CreateHelpPostSerializer,
                          CreateHelpPostCommentSerializer, UpdateHelpPostSerializer)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

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

    def get_queryset(self):
        return SharePost.objects.filter(user=self.request.user)

class DeleteSharePost(generics.DestroyAPIView):
    serializer_class = UpdateSharePostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SharePost.objects.filter(user=self.request.user)

class CreateSharePostComment(generics.CreateAPIView):
    serializer_class = CreateSharePostCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        share_post_id = self.kwargs['share_post_id']
        # share_post = SharePost.objects.get(id=share_post_id)
        share_post = get_object_or_404(SharePost, id=share_post_id)
        serializer.save(user=self.request.user,share_post=share_post)

class GetHelpPosts(generics.ListAPIView):
    queryset = HelpPost.objects.all()
    serializer_class = GetHelpPostsSerializer
    permission_classes = [AllowAny]

class GetHelpPostComments(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GetHelpPostCommentsSerializer

    def get_queryset(self):
        help_post_id = self.kwargs['help_post_id']
        return HelpPostComment.objects.filter(help_post_id=help_post_id)

class CreateHelpPost(generics.CreateAPIView):
    serializer_class = CreateHelpPostSerializer
    permission_classes = [IsAuthenticated]

class ChangeHelpPost(generics.UpdateAPIView):
    serializer_class = UpdateHelpPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HelpPost.objects.filter(user=self.request.user)

class DeleteHelpPost(generics.DestroyAPIView):
    serializer_class = UpdateHelpPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HelpPost.objects.filter(user=self.request.user)

class CreateHelpPostComment(generics.CreateAPIView):
    serializer_class = CreateHelpPostCommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        help_post_id = self.kwargs['help_post_id']
        # help_post = HelpPost.objects.get(id=help_post_id)
        help_post= get_object_or_404(HelpPost, id=help_post_id)
        serializer.save(user=self.request.user,help_post=help_post)

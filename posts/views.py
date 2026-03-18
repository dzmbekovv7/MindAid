from django.shortcuts import render
from rest_framework import generics
from .models import SharePost, SharePostComment, HelpPost, HelpPostComment
from .serializers import (GetSharePostsSerializer, GetSharePostCommentsSerializer,
                          CreateSharePostSerializer, UpdateSharePostSerializer,
                          CreateUpdateSharePostCommentSerializer, GetHelpPostsSerializer,
                          GetHelpPostCommentsSerializer, CreateHelpPostSerializer,
                          CreateHelpPostCommentSerializer, UpdateHelpPostSerializer)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from core.permissions import IsAdminOrModerator, IsAdmin, IsOwnerOrAdminOrReadOnly

class SharePostViewSet(viewsets.ModelViewSet):
    queryset = SharePost.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['filter']
    search_fields = ['heading']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminOrReadOnly()]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateSharePostSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateSharePostSerializer
        return GetSharePostsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SharePostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = GetSharePostCommentsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminOrReadOnly()]


    def get_queryset(self):
        share_post_id = self.kwargs.get('share_post_id')
        return SharePostComment.objects.filter(share_post_id=share_post_id)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateUpdateSharePostCommentSerializer
        return GetSharePostCommentsSerializer

    def perform_create(self, serializer):
        share_post_id = self.kwargs.get('share_post_id')
        share_post = get_object_or_404(SharePost, id=share_post_id)
        serializer.save(user=self.request.user, share_post=share_post)


class HelpPostViewSet(viewsets.ModelViewSet):
    queryset = HelpPost.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['filter']
    search_fields = ['heading']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminOrReadOnly()]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateHelpPostSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateHelpPostSerializer
        return GetHelpPostsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HelpPostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = GetHelpPostCommentsSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrAdminOrReadOnly()]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateHelpPostCommentSerializer
        return GetHelpPostCommentsSerializer

    def get_queryset(self):
        help_post_id = self.kwargs.get('help_post_id')
        return HelpPostComment.objects.filter(help_post_id=help_post_id)

    def perform_create(self, serializer):
        help_post_id = self.kwargs.get('help_post_id')
        help_post = get_object_or_404(HelpPost, id=help_post_id)
        serializer.save(user=self.request.user, help_post=help_post)

from rest_framework import serializers
from .models import SharePost, SharePostComment, HelpPost, HelpPostComment

class GetSharePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePost
        fields = '__all__'

class GetHelpPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = '__all__'

class GetSharePostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePostComment
        fields = '__all__'

class GetHelpPostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPostComment
        fields = '__all__'

class CreateSharePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePost
        fields = ['heading', 'text', 'show_nickname', 'filter']

    def create(self, validated_data):
        user = self.context['request'].user
        return SharePost.objects.create(
            user=user,
            **validated_data
        )

class CreateHelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = ['heading', 'text', 'show_nickname', 'filter']

    def create(self, validated_data):
        user = self.context['request'].user
        return HelpPost.objects.create(user=user, **validated_data)

class CreateSharePostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePostComment
        fields = ['comment']

class CreateHelpPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPostComment
        fields = ['comment']


class UpdateSharePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePost
        fields = ['heading', 'text', 'show_nickname', 'filter']


class UpdateHelpPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPost
        fields = ['heading', 'text', 'show_nickname', 'filter']

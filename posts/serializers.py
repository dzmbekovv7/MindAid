from rest_framework import serializers
from .models import SharePost, SharePostComment

class GetSharePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePost
        fields = '__all__'

class GetSharePostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePostComment
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
class CreateSharePostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePostComment
        fields = ['comment']

class UpdateSharePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharePost
        fields = ['heading', 'text', 'show_nickname', 'filter']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


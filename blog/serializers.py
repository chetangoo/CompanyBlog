from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = ('id','url','post','author','text','created_date','approved_comment')

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ('id','url','author','title','text','created_date','published_date')


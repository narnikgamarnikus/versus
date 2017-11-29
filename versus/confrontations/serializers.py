from rest_framework import serializers

from .models import (Category, Topic, Option,
					Opinion, Recomendation, Comment)


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Topic
		fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Option
		fields = '__all__'


class OpinionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Option
		fields = '__all__'


class RecomendationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recomendation
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'	
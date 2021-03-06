from channels_api.bindings import ResourceBinding
from .models import (Category, Topic, Option,
					Opinion, Recomendation, Comment)
from .serializers import (CategorySerializer, TopicSerializer, OptionSerializer,
						OpinionSerializer, RecomendationSerializer, CommentSerializer)


'''
class MyBinding(ResourceBinding):

     def _group_name(self, action, id=None):
           if action == "create":
                  return "{}-{}-{}".format(self.model_label, action, user_id)
'''


class CategoryBinding(ResourceBinding):

	model = Category
	stream = "categories"
	serializer_class = CategorySerializer
	queryset = Category.objects.all()


class TopicBinding(ResourceBinding):

	model = Topic
	stream = "topics"
	serializer_class = TopicSerializer
	queryset = Topic.objects.all()


class OptionBinding(ResourceBinding):

	model = Option
	stream = "options"
	serializer_class = OptionSerializer
	queryset = Option.objects.all()

    
class OpinionBinding(ResourceBinding):

	model = Opinion
	stream = "opinions"
	serializer_class = OpinionSerializer
	queryset = Opinion.objects.all()


class RecomendationBinding(ResourceBinding):

	model = Recomendation
	stream = "recommendations"
	serializer_class = RecomendationSerializer
	queryset = Recomendation.objects.all()


class CommentsBinding(ResourceBinding):

	model = Comment
	stream = "comments"
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()

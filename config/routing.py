from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from versus.confrontations.bindings import (CategoryBinding, TopicBinding, OptionBinding,
											OpinionBinding, RecomendationBinding, CommentsBinding)

from versus.confrontations.auth import path_token_user

class APIDemultiplexer(WebsocketDemultiplexer):

	@path_token_user
	def connect(self, message, **kwargs):
		print(message)

	@path_token_user
	def disconnect(self, message, **kwargs):
		print(message)

	consumers = {
	  'categories': CategoryBinding.consumer,
	  'topics': TopicBinding.consumer,
	  'options': OptionBinding.consumer,
	  'opinions': OpinionBinding.consumer,
	  'recommendations': RecomendationBinding.consumer,
	  'comments': CommentsBinding.consumer
	}

channel_routing = [
    route_class(APIDemultiplexer)
]

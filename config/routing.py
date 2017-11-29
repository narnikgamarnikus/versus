from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from versus.confrontations.bindings import (CategoryBinding, TopicBinding, OptionBinding,
											OpinionBinding, RecomendationBinding, CommentsBinding)

class APIDemultiplexer(WebsocketDemultiplexer):

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

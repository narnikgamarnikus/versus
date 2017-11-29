'''
from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class

from polls.bindings import QuestionBinding

class APIDemultiplexer(WebsocketDemultiplexer):

    consumers = {
      'questions': QuestionBinding.consumer
    }

channel_routing = [
    route_class(APIDemultiplexer)
]
'''
from graphene import relay
from graphene_django import DjangoObjectType
from pay.models import Moviment

class MovimentType(DjangoObjectType):
    
    class Meta:
        model = Moviment
        interfaces = (relay.Node, )
        fields = '__all__'

class MovimentConnection(relay.Connection):

    class Meta:
        node = MovimentType
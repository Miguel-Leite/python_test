from graphene import relay
from graphene_django import DjangoObjectType
from pay.models import Deposit

class DepositType(DjangoObjectType):

    class Meta:
        model = Deposit
        interfaces = (relay.Node,)
        fields = '__all__'

class DepositConnection(relay.Connection):

    class Meta:
        node = DepositType

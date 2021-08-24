from graphene import relay
from graphene_django import DjangoObjectType
from pay.models import Account, Moviment, Deposit

class AccountType(DjangoObjectType):
    
    class Meta:
        model = Account
        interfaces = (relay.Node,)
        fields = '__all__'

class AccountConnection(relay.Connection):
    
    class Meta:
        node = AccountType
import graphene
from graphene import relay
from .models import Account, Moviment, Deposit


from pay.GraphQL.query.Account import AccountType, AccountConnection
from pay.GraphQL.query.Deposit import DepositType, DepositConnection
from pay.GraphQL.query.Moviment import MovimentType, MovimentConnection

from pay.GraphQL.mutation.Account import AddAccount, UpdateAccount, DeleteAccount
# from pay.GraphQL.mutation.Moviment import AddMoviment, UpdateMoviment, DeleteMoviment
from pay.GraphQL.mutation.Deposit import AddDeposit, UpdateDeposit, DeleteDeposit

class Mutation(graphene.ObjectType):

    """
        Mutation of Account
        - Add Account
        - Update Account
        - Delete Account
    """
    AddAccount = AddAccount.Field()
    UpdateAccount = UpdateAccount.Field()
    DeleteAccount = DeleteAccount.Field()

    """
        Mutation of Deposit
        - Add Deposit
        - Update Deposit
        - Delete Deposit
    """
    AddDeposit = AddDeposit.Field()
    UpdateDeposit = UpdateDeposit.Field()
    DeleteDeposit = DeleteDeposit.Field()

class Query(graphene.ObjectType):
    all_accounts = graphene.List(AccountType)
    all_moviments = graphene.List(MovimentType)
    all_deposits = graphene.List(DepositType)

    accountConnection = relay.ConnectionField(AccountConnection)
    movimentConnection = relay.ConnectionField(MovimentConnection)
    depositConnection = relay.ConnectionField(DepositConnection)

    def resolve_all_accounts(self, info):
        return Account.objects.all()

    def resolve_all_moviments(self, info):
        return Moviment.objects.all()

    def resolve_all_deposits(self, info):
        return Deposit.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)

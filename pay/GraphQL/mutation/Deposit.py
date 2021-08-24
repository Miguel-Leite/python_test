import graphene
from pay.models import Deposit, Moviment
from pay.GraphQL.query.Deposit import DepositType

from pay.app.usecase.Moviment.moviment_usecase import MovimentUsecase


class DepositInput(graphene.InputObjectType):
    id = graphene.String()
    amount_numeric = graphene.String()
    applied_fee = graphene.String()
    deposit_limit = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

class AddDeposit(graphene.Mutation):
    class Arguments:
        deposit_data = DepositInput(required=True)

    deposit = graphene.Field(DepositType)

    def mutate(self, info, deposit_data=None):
        deposit_instance = Deposit(
                amount_numeric= deposit_data.amount_numeric,
                applied_fee= deposit_data.applied_fee,
                deposit_limit= deposit_data.deposit_limit,
                created_at = deposit_data.created_at,
                updated_at = deposit_data.updated_at
            )
        moviment_instance = Moviment(
            code_movement = deposit_instance.id,
            debit_account_number = deposit_data.amount_numeric,
            amount_movement = deposit_data.amount_numeric,
            data_movement = deposit_data.created_at,
            data_validate_movement = deposit_data.created_at,
        )

        deposit_instance.save()
        moviment_instance.save()

        return AddDeposit(deposit=deposit_instance)

class UpdateDeposit(graphene.Mutation):
    class Arguments:
        deposit_data = DepositInput(required=True)

    deposit = graphene.Field(DepositType)

    def mutate(self, info, deposit_data=None):

        deposit_instance = Deposit(pk=deposit_data.id)

        if deposit_instance:
            deposit_instance.amount_numeric = deposit_data.amount_numeric
            deposit_instance.applied_fee = deposit_data.applied_fee
            deposit_instance.deposit_limit = deposit_data.deposit_limit
            deposit_instance.created_at = deposit_data.created_at
            deposit_instance.updated_at = deposit_data.updated_at
            deposit_instance.save()
            return UpdateDeposit(deposit=deposit_instance)

        return UpdateDeposit(deposit=None)

class DeleteDeposit(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    deposit = graphene.Field(DepositType)

    def mutate(self, info, deposit_data=None):
        deposit_instance = Deposit.objects.get(pk=deposit_data.id)
        deposit_instance.delete()

        return None
import graphene
from pay.models import Account
from pay.GraphQL.query.Account import AccountType


class Input(graphene.InputObjectType):
    id = graphene.String()
    account_status = graphene.String()
    account_purpose = graphene.String()
    account_description = graphene.String()
    creation_date = graphene.DateTime()
    update_date = graphene.DateTime()

class AddAccount(graphene.Mutation):
    class Arguments:
        data = Input(required=True)

    account = graphene.Field(AccountType)

    def mutate(self, info, data=None):
        account_instance = Account(
            account_status = data.account_status,
            account_purpose = data.account_purpose,
            account_description = data.account_description,
            creation_date = data.creation_date,
            update_date = data.update_date,
        )
        
        account_instance.save()
        return AddAccount(account=account_instance)

class UpdateAccount(graphene.Mutation):
    class Arguments:
        account_data = Input(required=True)
    
    account = graphene.Field(AccountType)

    def mutate(self, info, account_data=None):
        
        account_instance = Account.objects.get(pk=account_data.id)

        if account_instance:
            account_instance.account_status = account_data.account_status
            account_instance.account_purpose = account_data.account_purpose
            account_instance.account_description = account_data.account_description
            account_instance.creation_date = account_data.creation_date
            account_instance.update_date = account_data.update_date
            account_instance.save()
            return UpdateAccount(account=account_instance)
        return UpdateAccount(account=None)

class DeleteAccount(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    account = graphene.Field(AccountType)

    def mutate(self, info, account_data=None):
        account_instance = Account.objects.get(pk=account_data.id)
        account_instance.delete()

        return None


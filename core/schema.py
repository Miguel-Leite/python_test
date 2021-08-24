import graphene
import pay.schema

class Query(pay.schema.Query, graphene.ObjectType):
    pass

class Mutation(pay.schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
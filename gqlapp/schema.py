import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gqlapp.models import ProductModel

class Products(DjangoObjectType):
    class Meta:
        model = ProductModel
        filter_fields = ['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']
        interfaces = (relay.Node, )

class ProductAdd(graphene.Mutation):
    class Input:
        id = graphene.ID()
        Segment = graphene.String(required=True)
        Country = graphene.String(required=True)
        Product = graphene.String(required=True)
        Units = graphene.Int(required=True)
        Sales = graphene.Int(required=True)
        Datesold = graphene.String(required=True)

    product = graphene.Field(Products)

    @classmethod
    def mutate(cls,root, info, **kwargs):
        product_instance = ProductModel(Segment=kwargs['Segment'], Country=kwargs['Country'], Product=kwargs['Product'], Units=kwargs['Units'], Datesold=kwargs['Datesold'])
        product_instance.save()
        return ProductAdd(product_instance=product_instance)
    

class Query(graphene.ObjectType):
        prodinfo = relay.Node.Field(Products)
        all_prodinfo = DjangoFilterConnectionField(Products)
        
        def resolve_prodinfo(self,info):
            return ProductModel.objects.all()

class Mutation(graphene.ObjectType):
    addProduct = ProductAdd.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
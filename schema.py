import graphene

from cookbook.ingredients.schema import Query as IngredientQuery

class Query(IngredientQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
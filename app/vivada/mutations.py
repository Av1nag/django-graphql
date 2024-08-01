import graphene
from .models import Groceries
from .queries import GroceriesType
import graphene
import graphql_jwt



class GroceriesAddMutation(graphene.Mutation):
    class Arguments:
        groceryName = graphene.String(required=True)
        groceryType = graphene.String(required=False)
        groceryPrice = graphene.Int(required=True)

    groceries = graphene.Field(GroceriesType)

    @classmethod
    def mutate(cls, root, info, groceryName, groceryType, groceryPrice):
        groceries, created = Groceries.objects.update_or_create(
            groceryName=groceryName,
            defaults={
                "groceryType": groceryType,
                "groceryPrice": groceryPrice,
            },
        )
        groceries.save()
        return GroceriesAddMutation(groceries=groceries)


class GroceriesUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        groceryName = graphene.String(required=False)
        groceryType = graphene.String(required=False)
        groceryPrice = graphene.Int(required=False)

    groceries = graphene.Field(GroceriesType)

    @classmethod
    def mutate(cls, root, info, id, groceryName, groceryType, groceryPrice):
        groceries = Groceries.objects.get(id=id)
        groceries.groceryName = groceryName
        groceries.groceryType = groceryType
        groceries.groceryPrice = groceryPrice
        groceries.save()
        return GroceriesUpdateMutation(groceries=groceries)


class GroceriesDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    groceries = graphene.Field(GroceriesType)

    @classmethod
    def mutate(cls, root, info, id):
        groceries = Groceries.objects.get(id=id)
        groceries.delete()
        return 0

class Mutation(graphene.ObjectType):
    add_groceries = GroceriesAddMutation.Field()
    update_groceries = GroceriesUpdateMutation.Field()
    delete_groceries = GroceriesDeleteMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

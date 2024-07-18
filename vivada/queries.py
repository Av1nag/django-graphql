import graphene
from graphene_django import DjangoObjectType
from .models import Books, Questions, Answers, Groceries

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "bookName", "excerpt")


class QuestionsType(DjangoObjectType):
    class Meta:
        model = Questions
        fields = ("id", "question", "questionCategory")
        
class AnswersType(DjangoObjectType):
    class Meta:
        model = Answers
        fields = ("id", "answer")
        
class GroceriesType(DjangoObjectType):
    class Meta:
        model = Groceries        
        fields = ("id", 'groceryName', "groceryType", "groceryPrice")
        
class Query(graphene.ObjectType):
    all_books = graphene.Field(BooksType, id=graphene.Int())
    all_questions =  graphene.List(QuestionsType)
    all_answers = graphene.List(AnswersType)
    all_groceries = graphene.List(GroceriesType)
    
    def resolve_all_books(root, info, id ):
        return Books.objects.get(pk=id)
    
    def resolve_all_questions(root, info):
        return Questions.objects.all()
    
    def resolve_all_answers(root, info):
        return Answers.objects.all()
    
    def resolve_all_groceries(root, info):
        return Groceries.objects.all()
        
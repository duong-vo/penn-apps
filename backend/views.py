from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from backend.models import Keywords, Users, UserKeyword, UserArticle, Articles
from backend.serializers import ArticlesSerializer
from django.http.response import JsonResponse
import ast

@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        print("Receive POST request")
        fname, lname = request.data['firstname'], request.data['lastname']
        email = request.data['email']
        saved_user = Users.objects.create(firstname=fname, lastname=lname, email=email)

        keywords = ast.literal_eval(request.data['keywords'])
        

        for keyword in keywords:
            print(keyword)
            keyword = keyword.strip().lower()
            if not Keywords.objects.filter(name=keyword).exists():
                saved_keyword = Keywords.objects.create(name=keyword)
            else:
                saved_keyword = list(Keywords.objects.filter(name = keyword))[0]

            saved_user_keyword = UserKeyword.objects.create(user=saved_user, keyword=saved_keyword, isActive=True)
        return Response({"message": "User added successfully"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def add_keyword(request, user_id):
    if request.method == 'POST':
        keyword= request.data['keyword']

        keyword = keyword.strip().lower()
        user = Users.objects.get(id=user_id)
        if not Keywords.objects.filter(name=keyword).exists():
            saved_keyword = Keywords.objects.create(name=keyword)
            saved_userkeyword = UserKeyword.objects.create(user=user, keyword=saved_keyword, isActive=True)
        return Response({"message": "Keyword added successfully"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_articles(request, user_id):
    user = Users.objects.get(pk=user_id)
    user_articles = UserArticle.objects.filter(user=user)
    article_ids = user_articles.values_list('article_id', flat=True)
    articles = Articles.objects.filter(id__in=article_ids)
    articles_serializer = ArticlesSerializer(articles, many=True)
    print(articles_serializer.data)
    return JsonResponse(articles_serializer.data, safe=False, status=status.HTTP_200_OK)


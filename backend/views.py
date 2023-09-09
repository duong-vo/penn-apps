from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework import status
from backend.models import Keywords, Users, UserKeyword

def add_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        fname, lname = user_data['firstname'], user_data['lastname']
        email = user_data['email']
        saved_user = Users.objects.create(firstname=fname, lastname=lname, email=email)

        keywords = user_data['keywords']

        for keyword in keywords:
            keyword = keyword.strip().lower()
            if not Keywords.objects.filter(name=keyword).exists():
                saved_keyword = Keywords.objects.create(name=keyword)
            else:
                saved_keyword = list(Keywords.objects.filter(name = keyword))[0]

            saved_user_keyword = UserKeyword.objects.create(user=saved_user, keyword=saved_keyword, isActive=True)

def add_keyword(request):
    if request.method == 'POST':
        keyword_data = JSONParser().parse(request)
        keyword, uid = keyword_data['keyword', 'user_id']

        keyword = keyword.strip().lower()
        user = Users.objects.get(id=uid)
        if not Keywords.objects.filter(name=keyword).exists():
            saved_keyword = Keywords.objects.create(name=keyword)
        else:
            saved_keyword = list(Keywords.objects.create(user=user, keyword=keyword, isActive=True))
        


def user_articles(request, user_id):
    # Get the user object based on the user_id
    user = User.objects.get(pk=user_id)
    # Filter the articles for the specific user
    articles = UserArticle.objects.filter(author=user)
    # You can then pass the 'articles' queryset to a template for rendering
    context = {
        'user': user,
        'articles': articles,
    }
    return render(request, 'user_articles.html', context)

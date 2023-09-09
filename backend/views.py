from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import Keywords, Users, UserKeyword
from backend.serializers import TodoSerializer
from backend.ProcessData import ProcessData

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
        keyword
        keyword = keyword.strip().lower()
        if not Keywords.objects.


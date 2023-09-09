from rest_framework import serializers
from .models import Users, Keywords, UserKeyword, Articles, KeywordArticle, UserArticle

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'

class UserKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKeyword
        fields = '__all__'

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

class KeywordArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordArticle
        fields = '__all__'

class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserArticle
        fields = '__all__'

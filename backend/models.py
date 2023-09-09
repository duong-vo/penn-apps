from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()

class Keywords(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

class UserKeyword(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)

class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)

class KeywordArticle(models.Model):
    id = models.AutoField(primary_key=True)
    keyword = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

class UserArticle(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    hasSeen = models.BooleanField(default=False)
# ProcessData.py
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pennapps.settings")

from collections import deque, defaultdict
from backend.models import UserKeyword, Keywords, Articles, Users, UserArticle
from metaphor_python import Metaphor
from dotenv import load_dotenv
import os

load_dotenv()

class ProcessData:
    def __init__(self):
        self.keyword_queue = deque()
        self.metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))
    def fetch_keyword_from_database(self):
        active_keywords = list(Keywords.objects.filter(userkeyword__isActive=True))
        self.keyword_queue = deque(active_keywords)

    def metaphor_search(self, keyword):
        response = self.metaphor.search(
            keyword,
            num_results=10,
            use_autoprompt=True,
            type="keyword",
            )
        print(response)
        return response
    
    def update_database(self):
        self.fetch_keyword_from_database()
        while self.keyword_queue:
            cur_keyword = self.keyword_queue.popleft()
            users_with_activated_keyword = Users.objects.filter(userkeyword__keyword__name=cur_keyword.name, userkeyword__isActive=True)

            articles = self.metaphor_search(cur_keyword.name)

            for article in articles:
                try:
                    existing_article = Articles.objects.get(url=article.url)
                except Articles.DoesNotExist:
                    new_article = Articles(url=article.url, title=article.title, author=article.author)
                    new_article.save()
                    for user in users_with_activated_keyword:
                        UserArticle.objects.create(user=user,article=new_article, hasSeen=False)

    def run(self):
        unseen_article = UserArticle.objects.filter(hasSeen=False).select_related()

        unseen_user_article = unseen_article.select_related('user', 'article')

        user_article_dict = defaultdict(list)

        for user_article in unseen_user_article:
            user_article_dict[user_article.user].append(user_article.article)
        return user_article_dict
        
processData = ProcessData()
processData.update_database()
processData.run()
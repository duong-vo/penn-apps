from collections import deque
from backend.models import UserKeyword, Keywords
from metaphor_python import Metaphor
from dotenv import load_dotenv
import os

load_dotenv()

class ProcessData:
    def __init__(self):
        self.keyword_queue = deque()
        self.metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))
    def fetch_keyword_from_database(self):
        active_keywords = list(Keywords.objects.filter(userkeyword__isActive=True).name)
        self.keyword_queue = deque(active_keywords)
    def metaphor_search(self, keyword):
        response = self.metaphor.search(
            keyword,
            num_results=10,
            use_autoprompt=True,
            type="keyword",
            )
        return response
    
    def run(self):
        self.fetch_keyword_from_database()
        while self.keyword_queue:
            cur_keyword = self.keyword_queue.popleft()
            articles = self.metaphor_search(cur_keyword)

    

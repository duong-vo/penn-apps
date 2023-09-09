import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class EmailService:
    def __init__(self, recipients, subject, content):
        self.message = Mail("vodh2@miamioh.edu", "duong.kej@gmail.com", "Test subject", "Test content")
        self.sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    def send(self):
        try: 
            response = self.sg.send(self.message)
            print(response)
        except Exception as e:
            print(e)

es = EmailService('test', 'subject', 'content')
es.send()

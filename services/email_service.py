import os
from sendgrid import SendGridAPIClient
from django.template.loader import render_to_string
from sendgrid.helpers.mail import Mail

class EmailService:
    def __init__(self, recipient, subject, articles):
        html_content = render_to_string('email_template.html', {'articles': articles})
        print(html_content)
        self.message = Mail("vodh2@miamioh.edu", recipient, "Test subject", html_content=html_content)
        self.sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    def send(self):
        try: 
            response = self.sg.send(self.message)
            print(response)
        except Exception as e:
            print(e)

# es = EmailService('test', 'subject', 'content')
# es.send()

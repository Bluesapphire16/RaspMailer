from django import http
import json
from .models import Mail

def get_json_response(jsonobject):
    response = http.HttpResponse(json.dumps(jsonobj).encode("utf-8"))
    response["Content-Type"] = "application/json"
    return response

def get_plaintext_response(plain):
    response = http.HttpResponse(plain.encode("utf-8"))
    response["Content-Type"] = "text/plain"
    return response

class REST_API_v1:
    @staticmethod
    def get_mail(query={}):
        mails = []
        if not query:
            mails = Mail.objects.all()
    
        jsonobj = []
        for mail in mails:
            jsonobject.append({"id": mail.id, "mailtype": mail.mailtype,
                    "from": [i.email_address for i in mail.mail_from.all()],
                    "to": [i.email_address for i in mail.to.all()],
                    "cc": [i.email_address for i in mail.cc.all()],
                    "bcc": [i.email_address for i in mail.bcc.all()],
                    "subject": self.subject})

        return get_json_response(jsonobj)

    @staticmethod
    def get_payload(id):
        mail = Mail.objects.get(id=id)
        return get_plaintext_response(mail.payload)

    @staticmethod
    def get_contact(query={}):
        pass
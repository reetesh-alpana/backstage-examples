import json
from peewee import *
from backstage.core import View, Response

class User(Model):
    id = IntegerField(primary_key=True, unique=True)
    username = CharField(unique=True)
    email = CharField(unique=True)

    class Meta:
        db = "sqlite.db"
        database = SqliteDatabase(db)

class UserView(View):
    def get(self, request):
        import pdb; pdb.set_trace()
        
        response = Response()
        response.status_code = 200
        response.status_message = "OK"
        response.message = json.dumps({'id': 1, 'name': 'alpana', 'email': 'repo@alpanahub.com'})
        response.headers = {"Content-type": "application/json", "Access-Control-Allow-Origin": "*"}
        return response


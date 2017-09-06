import json
#from sqlalchemy import Column, Integer, String, Text, DateTime, Table
#from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TransactionProcessor(object):

    def pre_process(self,request):
        connection_string = settings.DB_SESSION_HANDLERS[label]
        engine = create_engine(connection_string, echo=echo)
        Session = sessionmaker(bind=engine)
        session = Session()
        setattr(request, 'session', session)

    def post_process(self, request):
        request.session.commit()


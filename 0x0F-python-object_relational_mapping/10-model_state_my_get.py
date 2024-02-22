#!/usr/bin/python3
"""
To print given state object in the database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def state_obj(user, password, database, state):
     engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, password, database
                )
            )
     Session = sessionmaker(bind=engine)
     session = Session()
     obj = 0
     for states in session.query(State).order_by(State.id):
         if state == states
             obj += 1
         else:
             print("Not found")
     print(obj)


if __name__ == "__main__":
     user = sys.argv[1]
     password = sys.argv[2]
     database = sys.argv[3]
     state = sys.argv[4]

     state_obj(user, password, database, state)

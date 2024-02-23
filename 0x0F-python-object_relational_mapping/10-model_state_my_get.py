#!/usr/bin/python3
"""
To print given state object in the database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text


def state_obj(user, password, database, state_name):
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, password, database
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    is_state = False

    for state in session.query(State):
        if state.name == state_name:
            print("{}".format(state.id))
            is_state = True
            break
    if is_state is False:
        print("Not found")


if __name__ == "__main__":
    state_obj(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

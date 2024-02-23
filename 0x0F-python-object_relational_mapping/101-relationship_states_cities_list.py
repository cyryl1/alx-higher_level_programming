#!/usr/bin/python3
"""
To lists all State objects, and corresponding City objects,
contained in the database
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        cities = session.query(City).filter_by(
                state_id=state.id
                ).order_by(City.id).all()
        for city in cities:
            print("     {}: {}".format(city.id, city.name))

#!/usr/bin/python3
"""
This is a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""
from relationship_state import Base, State
from relationship_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_col = session.query(State).outerjoin(City).order_by(
        State.id, City.id).all()

    for state in state_col:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

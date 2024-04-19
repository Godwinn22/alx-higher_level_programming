#!/usr/bin/python3
"""
This is a script that lists all State objects
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:\
        {}@localhost/{}'.format(username, passwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    for each_instance in session.query(State).order_by(State.id):
        print("{}: {}".format(each_instance.id, each_instance.name))

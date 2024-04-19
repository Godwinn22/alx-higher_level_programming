#!/usr/bin/python3
"""
This is a script that lists all State objects
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwd, db_name))

    Session = sessionmaker(bind=engine)

    session = Session()

    first_instance = session.query(State).order_by(State.id).first()

    if not first_instance:
        print("Nothing")
    else:
        print("{}: {}".format(first_instance.id, first_instance.name))

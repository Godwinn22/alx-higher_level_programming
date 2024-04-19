#!/usr/bin/python3
"""
This is a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    sns = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwd, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    sns_search = session.query(State).filter(State.name == sns).first()

    if not sns_search:
        print("Not found")

    else:
        print("{}".format(sns_search.id))

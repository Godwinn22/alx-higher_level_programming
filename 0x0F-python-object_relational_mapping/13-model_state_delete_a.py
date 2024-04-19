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
    """
    Deletes State objects on the database.
    """
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for each_instance in session.query(State).filter(State.name.contains('a')):
        session.delete(each_instance)

    session.commit()
    session.close()

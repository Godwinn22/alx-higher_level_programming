#!/usr/bin/python3
"""
This is a script that lists all State objects
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import City
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

    for city, state in session.query(City,
                                     State).join(
                                         State).order_by(
                                             City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

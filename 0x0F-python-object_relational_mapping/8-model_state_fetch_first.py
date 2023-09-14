#!/usr/bin/python3
"""
return first statee object from database via python
parameters givenn to script: username, password, database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query first python instance in database
    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print("{:d}: {:s}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")

    session.close()

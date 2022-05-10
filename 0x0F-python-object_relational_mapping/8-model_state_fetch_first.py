#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_usa
"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    query = Session(engine)
    for state in query.query(State).order_by(State.id).all():
        if state is None:
            print("Nothing")
        else:
            conta = 1
            conta = conta - 1
            print("{}: {}".format(state.id, state.name))
            if conta == 0:
                break
    query.close()

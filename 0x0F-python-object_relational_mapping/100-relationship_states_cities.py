#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sesionCRUD = Session(engine)

    myState = State(name='California')
    myCity = City(name='San Francisco')
    myState.cities.append(myCity)
    sesionCRUD.add(myState)

    sesionCRUD.commit()
    sesionCRUD.close()

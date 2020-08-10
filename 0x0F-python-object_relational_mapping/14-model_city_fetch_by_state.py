#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, aliased
    from model_state import Base, State
    from model_city import City
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    s = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for st, ct in s:
        print("{}: ({:d}) {}".format(st.name, ct.id, ct.name))
    session.close()

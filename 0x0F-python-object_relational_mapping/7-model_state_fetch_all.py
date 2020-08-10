#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    for s in session().query(State).order_by(state.id):
        print("{}: {}".format(s.id, s.name))
    session().close()

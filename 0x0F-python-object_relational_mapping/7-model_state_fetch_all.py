#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    s = session().query(State).order_by(State.id)
    for st in s:
        print("{}: {}".format(st.id, st.name))
    session().close()

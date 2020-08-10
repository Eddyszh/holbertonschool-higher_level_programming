#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a
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
    s = session().query(State).filter(State.name.like('%a%')).all()
    if s:
        for st in s:
            session().delete(st)
        session().commit()
    session().close()

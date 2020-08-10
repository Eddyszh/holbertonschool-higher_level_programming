#!/usr/bin/python3
"""changes the name of a State object
"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    engine = create_engine('mysql+mysqlb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    s = session().query(State).filter_by(id=2).first()
    s.name = "New Mexico"
    session().commit()
    session().close()

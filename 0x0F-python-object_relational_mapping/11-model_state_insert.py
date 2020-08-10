#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    s = State(name="Louisiana")
    session().add(s)
    session().commit()
    print(s.id)
    session().close()

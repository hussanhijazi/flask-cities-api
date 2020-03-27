from sqlalchemy import MetaData, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine('sqlite:///mydb.sqlite', connect_args={'check_same_thread': False}, echo=False)
Base = declarative_base()
db_session = sessionmaker(bind=engine)()


# Table city
class City(Base):
    __tablename__ = 'City'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)


def get_cities():
    return db_session.query(City)


def get_city(city_id):
    city = db_session.query(City).get(city_id)
    return city


def add_city(city_name):
    city = City(city_name=city_name)
    city = db_session.add(city)
    db_session.commit()
    return city


def update_city(city_id, city_name):
    city = get_city(city_id)
    city.city_name = city_name
    city = db_session.add(city)
    db_session.commit()
    return city


def delete_city(city_id):
    city = db_session.query(City).filter(City.city_id == city_id).delete()
    return city

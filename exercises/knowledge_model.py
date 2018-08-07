from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='know'
	IDnumber=Column(Integer,primary_key=True)
	name=Column(String)
	topic=Column(String)
	rating=Column(Integer)
	def __repr__(self):
		return("\n If you want to learn about {}, "
			"you should look at the Wikipedia article called {}. "
			"We gave this article a rating of {} out of 10! ").format(
			self.topic,
			self.name,
			self.rating)

site1= Knowledge(IDnumber=1,name="sport",topic="swimming",rating=8)
# print(site1.__repr__())



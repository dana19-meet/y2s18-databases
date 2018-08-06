from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	ID number=column(integer,primary_key=True)
	name=column(string)
	topic=column(string)
	rating=column(integer)
	def __repr__(self):
		return ("primarykey: {}\n"
				"name: {}\n"
				"topic: {}\n"
				"rating: {}").format(
					self.primarykey,
					self.name,
					self.topic,
					self.rating)
				print("If you want to learn about "+self.topic+", you should look at the Wikipedia article called "+self.name+". We gave this article a rating of "+self.rating+" out of 10!")

site1= Knowledge(1,"sport","swimming",8)
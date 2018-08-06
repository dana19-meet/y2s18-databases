from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(IDnumber,name,topic,rating):
	site= Knowledge(IDnumber=IDnumber,
		name=name,
		topic=topic,
		rating=rating)

	session.add(site)
	session.commit()

def query_all_articles():
	sites = session.query(
		Knowledge).all()
	return sites


def query_article_by_topic(topic):
	sites = session.query(
		Knowledge).filter_by(
		topic=topic).all()
	return sites

def query_article_by_rating(threshold):
	sites = session.query(Knowledge).filter(
		rating<threshold).all()
	return sites

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
	topic=topic).delete()
	session.commit()

def delete_all_articles():
	pass

def edit_article_rating():
	pass

# add_article(3,"basketball","sport",7)
# add_article(4,"mango","food",10)
# add_article(5,"soccer","sport",7)
# add_article(6,"grapes","food",8)




# print(query_all_articles())
# print(query_article_by_topic("food"))
# delete_article_by_topic("food")
print(query_article_by_rating(8))

from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, desc, quant, price):
  if price < 1000:
    p = Product(name=name, description=desc, quantity=quant, price=price)
    session.add(p)
    session.commit()
  else:
    print("ERROR: 'PRICE TOO HIGH'")

def update_product_quant(id, quant):
  prod = session.query(Product).filter_by(id=id).first()
  prod.quantity=quant
  session.commit()

def update_product_pict(id, pict):
  prod = session.query(Product).filter_by(id=id).first()
  prod.pict=pict
  session.commit()

def delete_product(id):
  session.query(Product).filter_by(id=id).delete()
  session.commit()

def delete_all_products():
  session.query(Product).delete()
  session.commit()

def get_product(id):
  prod = session.query(Product).filter_by(id=id).first()
  return prod

def get_all_products():
  products = session.query(Product).all()
  return products

def prod_by_name(name):
  prods = session.query(Product).all()
  prs =[]
  if name != "":
    nameLen = len(name)
    for p in prods:
      pName = p.name
      if pName[:nameLen].lower() == name.lower():
        prs.append(p)
  return prs

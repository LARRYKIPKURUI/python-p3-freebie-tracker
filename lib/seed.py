#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

from faker import Faker

import random

# Connect to Database
if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker() # Instantiating it then using it  to generate dummy data
    
    #dev instance
    devs = []
    for _ in range(6):
        dev = Dev(
            dev_name = fake.name()
        )
        devs.append(dev)
        session.add_all(devs)
        session.commit()
        
  
    #company instance
    companies = [] 
    for _ in range (6): # the _ represents  a placeholder for a var we dont need
        company = Company(
            company_name = fake.company(),
            founding_year = random.randint(2010,2020)
        )
        companies.append(company)
        session.add_all(companies)
        session.commit() #save
    
      # My Junction -> Many to Many table (company_dev table)
    for dev in devs:
        related_companies = random.sample(companies, random.randint(1,5))
        for company in related_companies:
            dev.companies.append(company)
    session.commit()
       
     # freebies has-manys
    freebies = []
    item_names = ['Flask', 'Tshirts', 'stickers', 'Notebook', 'Pens','Gadgets']
    for _ in range(10):
        freebie = Freebie(
            item_name=random.choice(item_names),
            value=random.randint(1,10),
            company=random.choice(companies),
            dev=random.choice(devs)
        )
        freebies.append(freebie)
    session.add_all(freebies)
    session.commit()

    print("Congrats Data Seeded,lol ")
        
    
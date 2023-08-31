#!/usr/bin/env python3

# Script goes here!
from app import db, Company, Dev

def create_sample_data():
    company1 = Company(name='Company A', founding_year=2000)
    company2 = Company(name='Company B', founding_year=2010)
    dev1 = Dev(name='Developer 1')
    dev2 = Dev(name='Developer 2')

    db.session.add_all([company1, company2, dev1, dev2])
    db.session.commit()

if __name__ == '__main__':
    create_sample_data()

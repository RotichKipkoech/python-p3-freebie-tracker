from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    founding_year = db.Column(db.Integer, nullable=False)

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(dev=dev, company=self, item_name=item_name, value=value)
        db.session.add(freebie)
        db.session.commit()

    @classmethod
    def oldest_company(cls):
        return cls.query.order_by(cls.founding_year).first()

class Dev(db.Model):
    __tablename__ = 'devs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        if freebie.dev == self:
            freebie.dev = other_dev
            db.session.commit()


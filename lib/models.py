from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    company_name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.company_name}>'
    
    devs = relationship("Dev", secondary="company_dev", back_populates="companies")

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    dev_name = Column(String())

    def __repr__(self):
        return f'<Dev {self.dev_name}>'

    companies = relationship("Company", secondary="company_dev", back_populates="devs")

class Freebie(Base):
    __tablename__ = 'freebies'
    
    id = Column(Integer(), primary_key=True)
    value = Column(Integer(), nullable=False)
    item_name = Column(String(), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    
    def __repr__(self):
        dev_name = self.dev.dev_name if self.dev else "Could not find Dev"
        company_name = self.company.company_name if self.company else "Could not find Company"
        return f"< {self.item_name} was won by {dev_name} from {company_name}>"

    
    company = relationship("Company")
    dev = relationship("Dev")
    
# Junction table (many-to-many relationship) 
company_dev = Table(
    'company_dev',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', Integer, ForeignKey('devs.id'), primary_key=True)
)
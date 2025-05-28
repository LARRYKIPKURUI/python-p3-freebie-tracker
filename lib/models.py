from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

# Junction table for many-to-many between Company and Dev
company_dev = Table(
    'company_dev',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', Integer, ForeignKey('devs.id'), primary_key=True)
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    founding_year = Column(Integer)

    # Relationship to Devs (many-to-many)
    devs = relationship("Dev", secondary="company_dev", back_populates="companies")

    # Relationship to Freebies (one-to-many)
    freebies = relationship("Freebie", back_populates="company")

    def __repr__(self):
        return f"<Company {self.company_name} (founded {self.founding_year})>"


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    dev_name = Column(String, nullable=False)

    # Relationship to Companies (many-to-many)
    companies = relationship("Company", secondary="company_dev", back_populates="devs")

    # Relationship to Freebies (one-to-many)
    freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
        return f"<Dev {self.dev_name}>"


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    item_name = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)

    # Relationships to link both(company and dev)
    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def __repr__(self):
        dev_name = self.dev.dev_name if self.dev else "Unknown Dev"
        company_name = self.company.company_name if self.company else "Unknown Company"
        return f"<Freebie: {self.item_name} worth {self.value} given to {dev_name} from {company_name}>"

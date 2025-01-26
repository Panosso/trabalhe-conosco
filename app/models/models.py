from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint, Text
from sqlalchemy.orm import relationship, DeclarativeBase
from database.database import engine


class Base(DeclarativeBase):
    pass


class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf_cnpj = Column(String, unique=True, nullable=False)
    hash_password = Column(Text, nullable=False)
    properties = relationship("Property", back_populates="producer")


class Crop(Base):
    __tablename__ = "crops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    harvest_year = Column(Integer, nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"))
    property = relationship("Property", back_populates="crops")


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    total_area = Column(Float, nullable=False)
    agricultural_area = Column(Float, nullable=False)
    vegetation_area = Column(Float, nullable=False)
    producer_id = Column(Integer, ForeignKey("producers.id"))
    producer = relationship("Producer", back_populates="properties")
    crops = relationship("Crop", back_populates="property")

    __table_args__ = (
        UniqueConstraint("name", "producer_id", name="uq_property_producer"),
    )


# Create tables
Base.metadata.create_all(bind=engine)
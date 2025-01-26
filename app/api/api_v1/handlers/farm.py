from fastapi import HTTPException, Depends, APIRouter
from typing import List

from schemas.schemas import ProducerResponse, PropertyCreate, ProducerCreate
from models.models import Producer, Property
from database.database import get_db, SessionLocal


farm_router = APIRouter()

@farm_router.post("/producers/", response_model=ProducerResponse)
def create_producer(producer: ProducerCreate, db: SessionLocal = Depends(get_db)):
    db_producer = Producer(name=producer.name, cpf_cnpj=producer.cpf_cnpj, hash_password=producer.hash_password)
    db.add(db_producer)
    db.commit()
    db.refresh(db_producer)
    return db_producer

@farm_router.get("/producers/", response_model=List[ProducerResponse])
def list_producers(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db)):
    return db.query(Producer).offset(skip).limit(limit).all()

@farm_router.post("/properties/", response_model=PropertyCreate)
def create_property(property: PropertyCreate, producer_id: int, db: SessionLocal = Depends(get_db)):
    db_producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not db_producer:
        raise HTTPException(status_code=404, detail="Producer not found")

    db_property = Property(
        name=property.name,
        city=property.city,
        state=property.state,
        total_area=property.total_area,
        agricultural_area=property.agricultural_area,
        vegetation_area=property.vegetation_area,
        producer_id=producer_id,
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

@farm_router.get("/dashboard/")
def get_dashboard(db: SessionLocal = Depends(get_db)):

    total_farms = db.query(Property).count()
    total_area = db.query(Property.total_area)
    a = 0
    b = [x for x in total_area]
    print(b)

    by_state = (
        db.query(Property.state, func.count(Property.id).label("count"))
        .group_by(Property.state)
        .all()
    )

    return {
        "total_farms": total_farms,
        "total_area": total_area,
        "by_state": by_state,
    }

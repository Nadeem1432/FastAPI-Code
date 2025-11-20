
from sqlmodel import SQLModel, create_engine, Session
from .models import Address

DATABASE_URL = "sqlite:///./addresses.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create tables
SQLModel.metadata.create_all(engine)


from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlmodel import select

app = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session


@app.post("/addresses/", response_model=Address)
def create_address(address: Address, session: Session = Depends(get_session)):
    """Create a new address entry"""
    session.add(address)
    session.commit()
    session.refresh(address)
    return address

@app.get("/addresses/{address_id}", response_model=Address)
def read_address(address_id: int, session: Session = Depends(get_session)):
    """Retrieve an address entry by ID"""
    address = session.get(Address, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@app.put("/addresses/{address_id}", response_model=Address)
def update_address(address_id: int, updated_address: Address, session: Session = Depends(get_session)):
    """Update an address entry"""
    address = session.get(Address, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    address.name = updated_address.name
    address.latitude = updated_address.latitude
    address.longitude = updated_address.longitude
    session.add(address)
    session.commit()
    session.refresh(address)
    return address




@app.get("/addresses/", response_model=List[Address])
def list_addresses(session: Session = Depends(get_session)):
    """Retrieve all address entries"""
    addresses = session.exec(select(Address)).all()
    return addresses


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, session: Session = Depends(get_session)):
    address = session.get(Address, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    session.delete(address)
    session.commit()
    return {"message": "Deleted successfully"}


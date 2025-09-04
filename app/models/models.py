from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

# Association table for many-to-many relationship between organizations and activities
organization_activities = Table(
    'organization_activities',
    Base.metadata,
    Column('organization_id', Integer, ForeignKey('organizations.id'), primary_key=True),
    Column('activity_id', Integer, ForeignKey('activities.id'), primary_key=True)
)


class Building(Base):
    __tablename__ = "buildings"
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(Text)
    
    # Relationship with organizations
    organizations = relationship("Organization", back_populates="building")

class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    parent_id = Column(Integer, ForeignKey('activities.id'), nullable=True)
    level = Column(Integer, nullable=False, default=1)
    created_at = Column(Text)
    
    # Self-referential relationship for hierarchical structure
    parent = relationship("Activity", remote_side=[id], back_populates="children")
    children = relationship("Activity", back_populates="parent")
    
    # Relationship with organizations
    organizations = relationship("Organization", secondary=organization_activities, back_populates="activities")

class Organization(Base):
    __tablename__ = "organizations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    building_id = Column(Integer, ForeignKey('buildings.id'), nullable=False)
    created_at = Column(Text)
    
    # Relationships
    building = relationship("Building", back_populates="organizations")
    activities = relationship("Activity", secondary=organization_activities, back_populates="organizations")
    phone_numbers = relationship("OrganizationPhone", back_populates="organization")

class OrganizationPhone(Base):
    __tablename__ = "organization_phones"
    
    organization_id = Column(Integer, ForeignKey('organizations.id'), primary_key=True)
    phone_number = Column(String(20), primary_key=True)
    
    # Relationship
    organization = relationship("Organization", back_populates="phone_numbers")

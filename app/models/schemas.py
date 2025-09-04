from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Base schemas
class BuildingBase(BaseModel):
    address: str
    latitude: float
    longitude: float

class BuildingCreate(BuildingBase):
    pass

class Building(BuildingBase):
    id: int
    created_at: Optional[str] = None
    
    class Config:
        from_attributes = True

class ActivityBase(BaseModel):
    name: str
    parent_id: Optional[int] = None

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    level: int
    created_at: Optional[str] = None
    children: List['Activity'] = []
    
    class Config:
        from_attributes = True

class OrganizationPhoneBase(BaseModel):
    phone_number: str

class OrganizationPhone(OrganizationPhoneBase):
    organization_id: int
    
    class Config:
        from_attributes = True

class OrganizationBase(BaseModel):
    name: str
    building_id: int
    phone_numbers: List[str] = []
    activity_ids: List[int] = []

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    created_at: Optional[str] = None
    building: Building
    activities: List[Activity] = []
    
    class Config:
        from_attributes = True

# Search schemas
class OrganizationSearchByName(BaseModel):
    name: str

class OrganizationSearchByActivity(BaseModel):
    activity_id: int

class OrganizationSearchByBuilding(BaseModel):
    building_id: int

class OrganizationSearchByRadius(BaseModel):
    latitude: float
    longitude: float
    radius_km: float

class OrganizationSearchByRectangle(BaseModel):
    min_latitude: float
    max_latitude: float
    min_longitude: float
    max_longitude: float

# Update the forward reference
Activity.model_rebuild()

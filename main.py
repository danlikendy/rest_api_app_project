from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os

from app.db.database import get_db
from app.models import models, schemas
from app.core.config import settings

app = FastAPI(
    title="Organizations Directory API",
    description="REST API для справочника организаций, зданий и видов деятельности",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key authentication
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key

# Dependency to get current database session
def get_current_db(db: Session = Depends(get_db)):
    return db

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Organizations Directory API", "version": "1.0.0"}

# Organizations endpoints
@app.get("/organizations", response_model=List[schemas.Organization])
async def get_organizations(
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить список всех организаций"""
    organizations = db.query(models.Organization).all()
    return organizations

@app.get("/organizations/{organization_id}", response_model=schemas.Organization)
async def get_organization(
    organization_id: int,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить информацию об организации по ID"""
    organization = db.query(models.Organization).filter(models.Organization.id == organization_id).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization

@app.get("/organizations/building/{building_id}", response_model=List[schemas.Organization])
async def get_organizations_by_building(
    building_id: int,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить список всех организаций в конкретном здании"""
    organizations = db.query(models.Organization).filter(models.Organization.building_id == building_id).all()
    return organizations

@app.get("/organizations/activity/{activity_id}", response_model=List[schemas.Organization])
async def get_organizations_by_activity(
    activity_id: int,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить список организаций по виду деятельности (включая вложенные)"""
    # Get the activity and all its children recursively
    def get_activity_and_children(activity_id: int, level: int = 1):
        if level > 3:  # Limit to 3 levels as per requirements
            return []
        
        activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
        if not activity:
            return []
        
        result = [activity_id]
        children = db.query(models.Activity).filter(models.Activity.parent_id == activity_id).all()
        for child in children:
            result.extend(get_activity_and_children(child.id, level + 1))
        
        return result
    
    activity_ids = get_activity_and_children(activity_id)
    organizations = db.query(models.Organization).join(models.organization_activities).filter(
        models.organization_activities.c.activity_id.in_(activity_ids)
    ).all()
    return organizations

@app.get("/organizations/search/name", response_model=List[schemas.Organization])
async def search_organizations_by_name(
    name: str,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Поиск организаций по названию"""
    organizations = db.query(models.Organization).filter(
        models.Organization.name.ilike(f"%{name}%")
    ).all()
    return organizations

@app.get("/organizations/search/radius", response_model=List[schemas.Organization])
async def search_organizations_by_radius(
    latitude: float,
    longitude: float,
    radius_km: float,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Поиск организаций в заданном радиусе от точки"""
    # Using Haversine formula for distance calculation
    from sqlalchemy import text
    
    query = text("""
        SELECT DISTINCT o.* FROM organizations o
        JOIN buildings b ON o.building_id = b.id
        WHERE (
            6371 * acos(
                cos(radians(:lat)) * cos(radians(b.latitude)) * 
                cos(radians(b.longitude) - radians(:lng)) + 
                sin(radians(:lat)) * sin(radians(b.latitude))
            )
        ) <= :radius
    """)
    
    result = db.execute(query, {"lat": latitude, "lng": longitude, "radius": radius_km})
    organization_ids = [row[0] for row in result.fetchall()]
    
    organizations = db.query(models.Organization).filter(
        models.Organization.id.in_(organization_ids)
    ).all()
    return organizations

@app.get("/organizations/search/rectangle", response_model=List[schemas.Organization])
async def search_organizations_by_rectangle(
    min_latitude: float,
    max_latitude: float,
    min_longitude: float,
    max_longitude: float,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Поиск организаций в прямоугольной области"""
    organizations = db.query(models.Organization).join(models.Building).filter(
        models.Building.latitude >= min_latitude,
        models.Building.latitude <= max_latitude,
        models.Building.longitude >= min_longitude,
        models.Building.longitude <= max_longitude
    ).all()
    return organizations

# Buildings endpoints
@app.get("/buildings", response_model=List[schemas.Building])
async def get_buildings(
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить список всех зданий"""
    buildings = db.query(models.Building).all()
    return buildings

@app.get("/buildings/{building_id}", response_model=schemas.Building)
async def get_building(
    building_id: int,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить информацию о здании по ID"""
    building = db.query(models.Building).filter(models.Building.id == building_id).first()
    if not building:
        raise HTTPException(status_code=404, detail="Building not found")
    return building

# Activities endpoints
@app.get("/activities", response_model=List[schemas.Activity])
async def get_activities(
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить список всех видов деятельности"""
    activities = db.query(models.Activity).all()
    return activities

@app.get("/activities/{activity_id}", response_model=schemas.Activity)
async def get_activity(
    activity_id: int,
    db: Session = Depends(get_current_db),
    api_key: str = Depends(verify_api_key)
):
    """Получить информацию о виде деятельности по ID"""
    activity = db.query(models.Activity).filter(models.Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

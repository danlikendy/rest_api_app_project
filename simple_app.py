#!/usr/bin/env python3
import json
from datetime import datetime
from typing import List, Dict, Any

class InMemoryDB:
    def __init__(self):
        self.buildings = [
            {
                "id": 1,
                "address": "г. Москва, ул. Ленина, д. 1, офис 3",
                "latitude": 55.7558,
                "longitude": 37.6176,
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 2,
                "address": "г. Москва, ул. Тверская, д. 15",
                "latitude": 55.7616,
                "longitude": 37.6094,
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 3,
                "address": "г. Москва, ул. Арбат, д. 25",
                "latitude": 55.7522,
                "longitude": 37.5914,
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 4,
                "address": "г. Москва, ул. Блюхера, д. 32/1",
                "latitude": 55.7890,
                "longitude": 37.6123,
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 5,
                "address": "г. Москва, ул. Красная Площадь, д. 1",
                "latitude": 55.7539,
                "longitude": 37.6208,
                "created_at": datetime.now().isoformat()
            }
        ]
        
        self.activities = [
            {"id": 1, "name": "Еда", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"id": 2, "name": "Мясная продукция", "parent_id": 1, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 3, "name": "Молочная продукция", "parent_id": 1, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 4, "name": "Овощи и фрукты", "parent_id": 1, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 5, "name": "Автомобили", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"id": 6, "name": "Грузовые", "parent_id": 5, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 7, "name": "Легковые", "parent_id": 5, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 8, "name": "Запчасти", "parent_id": 7, "level": 3, "created_at": datetime.now().isoformat()},
            {"id": 9, "name": "Аксессуары", "parent_id": 7, "level": 3, "created_at": datetime.now().isoformat()},
            {"id": 10, "name": "Одежда", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"id": 11, "name": "Мужская одежда", "parent_id": 10, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 12, "name": "Женская одежда", "parent_id": 10, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 13, "name": "Услуги", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"id": 14, "name": "Ремонт", "parent_id": 13, "level": 2, "created_at": datetime.now().isoformat()},
            {"id": 15, "name": "Консультации", "parent_id": 13, "level": 2, "created_at": datetime.now().isoformat()}
        ]
        
        self.organizations = [
            {
                "id": 1,
                "name": "ООО \"Рога и Копыта\"",
                "building_id": 1,
                "phone_numbers": ["2-222-222", "3-333-333", "8-923-666-13-13"],
                "activity_ids": [1, 2],  # Еда, Мясная продукция
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 2,
                "name": "ИП \"Молочный рай\"",
                "building_id": 2,
                "phone_numbers": ["4-444-444", "8-999-123-45-67"],
                "activity_ids": [1, 3],  # Еда, Молочная продукция
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 3,
                "name": "ЗАО \"АвтоМир\"",
                "building_id": 3,
                "phone_numbers": ["5-555-555"],
                "activity_ids": [5, 6, 7],  # Автомобили, Грузовые, Легковые
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 4,
                "name": "ООО \"АвтоЗапчасти\"",
                "building_id": 3,
                "phone_numbers": ["6-666-666", "8-888-888-88-88"],
                "activity_ids": [7, 8],  # Легковые, Запчасти
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 5,
                "name": "ИП \"Модная одежда\"",
                "building_id": 4,
                "phone_numbers": ["7-777-777"],
                "activity_ids": [10, 11, 12],  # Одежда, Мужская, Женская
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 6,
                "name": "ООО \"Ремонт и сервис\"",
                "building_id": 5,
                "phone_numbers": ["8-888-888", "9-999-999"],
                "activity_ids": [13, 14],  # Услуги, Ремонт
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 7,
                "name": "ИП \"Консультант\"",
                "building_id": 1,
                "phone_numbers": ["1-111-111"],
                "activity_ids": [13, 15],  # Услуги, Консультации
                "created_at": datetime.now().isoformat()
            },
            {
                "id": 8,
                "name": "ООО \"Свежие овощи\"",
                "building_id": 2,
                "phone_numbers": ["2-333-444"],
                "activity_ids": [1, 4],  # Еда, Овощи и фрукты
                "created_at": datetime.now().isoformat()
            }
        ]
    
    def get_organizations(self) -> List[Dict[str, Any]]:
        return self.organizations
    
    def get_organization(self, org_id: int) -> Dict[str, Any]:
        for org in self.organizations:
            if org["id"] == org_id:
                return org
        return None
    
    def get_organizations_by_building(self, building_id: int) -> List[Dict[str, Any]]:
        return [org for org in self.organizations if org["building_id"] == building_id]
    
    def get_organizations_by_activity(self, activity_id: int) -> List[Dict[str, Any]]:
        # Получаем все дочерние активности
        def get_child_activities(parent_id: int, level: int = 1) -> List[int]:
            if level > 3:
                return []
            result = [parent_id]
            for activity in self.activities:
                if activity["parent_id"] == parent_id:
                    result.extend(get_child_activities(activity["id"], level + 1))
            return result
        
        activity_ids = get_child_activities(activity_id)
        result = []
        for org in self.organizations:
            if any(aid in activity_ids for aid in org["activity_ids"]):
                result.append(org)
        return result
    
    def search_organizations_by_name(self, name: str) -> List[Dict[str, Any]]:
        return [org for org in self.organizations if name.lower() in org["name"].lower()]
    
    def search_organizations_by_radius(self, lat: float, lng: float, radius_km: float) -> List[Dict[str, Any]]:
        def distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
            import math
            return 6371 * math.acos(
                math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
                math.cos(math.radians(lng2) - math.radians(lng1)) + 
                math.sin(math.radians(lat1)) * math.sin(math.radians(lat2))
            )
        
        result = []
        for org in self.organizations:
            building = next(b for b in self.buildings if b["id"] == org["building_id"])
            dist = distance(lat, lng, building["latitude"], building["longitude"])
            if dist <= radius_km:
                result.append(org)
        return result
    
    def search_organizations_by_rectangle(self, min_lat: float, max_lat: float, min_lng: float, max_lng: float) -> List[Dict[str, Any]]:
        result = []
        for org in self.organizations:
            building = next(b for b in self.buildings if b["id"] == org["building_id"])
            if (min_lat <= building["latitude"] <= max_lat and 
                min_lng <= building["longitude"] <= max_lng):
                result.append(org)
        return result
    
    def get_buildings(self) -> List[Dict[str, Any]]:
        return self.buildings
    
    def get_building(self, building_id: int) -> Dict[str, Any]:
        for building in self.buildings:
            if building["id"] == building_id:
                return building
        return None
    
    def get_activities(self) -> List[Dict[str, Any]]:
        return self.activities
    
    def get_activity(self, activity_id: int) -> Dict[str, Any]:
        for activity in self.activities:
            if activity["id"] == activity_id:
                return activity
        return None

db = InMemoryDB()

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        api_key = self.headers.get('X-API-Key')
        if api_key != 'your-secret-api-key-here':
            self.send_response(401)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"detail": "Invalid API key"}).encode())
            return
        
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        if path == '/':
            response = {"message": "Organizations Directory API", "version": "1.0.0"}
        elif path == '/organizations':
            response = db.get_organizations()
        elif path.startswith('/organizations/'):
            parts = path.split('/')
            if len(parts) == 3 and parts[2].isdigit():
                org_id = int(parts[2])
                response = db.get_organization(org_id)
                if not response:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"detail": "Organization not found"}).encode())
                    return
            elif len(parts) == 4 and parts[2] == 'building' and parts[3].isdigit():
                building_id = int(parts[3])
                response = db.get_organizations_by_building(building_id)
            elif len(parts) == 4 and parts[2] == 'activity' and parts[3].isdigit():
                activity_id = int(parts[3])
                response = db.get_organizations_by_activity(activity_id)
            elif len(parts) == 4 and parts[2] == 'search':
                if parts[3] == 'name' and 'name' in query_params:
                    name = query_params['name'][0]
                    response = db.search_organizations_by_name(name)
                elif parts[3] == 'radius' and all(k in query_params for k in ['latitude', 'longitude', 'radius_km']):
                    lat = float(query_params['latitude'][0])
                    lng = float(query_params['longitude'][0])
                    radius = float(query_params['radius_km'][0])
                    response = db.search_organizations_by_radius(lat, lng, radius)
                elif parts[3] == 'rectangle' and all(k in query_params for k in ['min_latitude', 'max_latitude', 'min_longitude', 'max_longitude']):
                    min_lat = float(query_params['min_latitude'][0])
                    max_lat = float(query_params['max_latitude'][0])
                    min_lng = float(query_params['min_longitude'][0])
                    max_lng = float(query_params['max_longitude'][0])
                    response = db.search_organizations_by_rectangle(min_lat, max_lat, min_lng, max_lng)
                else:
                    response = {"detail": "Invalid search parameters"}
            else:
                response = {"detail": "Not found"}
        elif path == '/buildings':
            response = db.get_buildings()
        elif path.startswith('/buildings/'):
            parts = path.split('/')
            if len(parts) == 3 and parts[2].isdigit():
                building_id = int(parts[2])
                response = db.get_building(building_id)
                if not response:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"detail": "Building not found"}).encode())
                    return
            else:
                response = {"detail": "Not found"}
        elif path == '/activities':
            response = db.get_activities()
        elif path.startswith('/activities/'):
            parts = path.split('/')
            if len(parts) == 3 and parts[2].isdigit():
                activity_id = int(parts[2])
                response = db.get_activity(activity_id)
                if not response:
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"detail": "Activity not found"}).encode())
                    return
            else:
                response = {"detail": "Not found"}
        else:
            response = {"detail": "Not found"}
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response, ensure_ascii=False, indent=2).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-API-Key, Content-Type')
        self.send_header('Access-Control-Max-Age', '86400')
        self.end_headers()

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, APIHandler)
    print("Сервер запущен на http://localhost:8000")
    print("API ключ: your-secret-api-key-here")
    print("Примеры запросов:")
    print("curl -H 'X-API-Key: your-secret-api-key-here' http://localhost:8000/organizations")
    print("curl -H 'X-API-Key: your-secret-api-key-here' http://localhost:8000/organizations/search/name?name=Рога")
    print("Нажмите Ctrl+C для остановки")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        httpd.server_close()

if __name__ == "__main__":
    run_server()

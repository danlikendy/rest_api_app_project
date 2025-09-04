#!/usr/bin/env python3
"""
Простая инициализация базы данных без миграций
"""
import os
from datetime import datetime
from app.db.database import engine, SessionLocal
from app.models import models

def create_tables():
    """Создать все таблицы в базе данных"""
    models.Base.metadata.create_all(bind=engine)

def seed_data():
    """Заполнить базу данных тестовыми данными"""
    db = SessionLocal()
    
    try:
        # Создаем здания
        buildings_data = [
            {"address": "г. Москва, ул. Ленина, д. 1, офис 3", "latitude": 55.7558, "longitude": 37.6176, "created_at": datetime.now().isoformat()},
            {"address": "г. Москва, ул. Тверская, д. 15", "latitude": 55.7616, "longitude": 37.6094, "created_at": datetime.now().isoformat()},
            {"address": "г. Москва, ул. Арбат, д. 25", "latitude": 55.7522, "longitude": 37.5914, "created_at": datetime.now().isoformat()},
            {"address": "г. Москва, ул. Блюхера, д. 32/1", "latitude": 55.7890, "longitude": 37.6123, "created_at": datetime.now().isoformat()},
            {"address": "г. Москва, ул. Красная Площадь, д. 1", "latitude": 55.7539, "longitude": 37.6208, "created_at": datetime.now().isoformat()},
        ]
        
        buildings = []
        for building_data in buildings_data:
            building = models.Building(**building_data)
            db.add(building)
            buildings.append(building)
        
        db.commit()
        
        # Создаем виды деятельности (иерархическая структура)
        activities_data = [
            # Уровень 1
            {"name": "Еда", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"name": "Автомобили", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"name": "Одежда", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
            {"name": "Услуги", "parent_id": None, "level": 1, "created_at": datetime.now().isoformat()},
        ]
        
        activities = []
        for activity_data in activities_data:
            activity = models.Activity(**activity_data)
            db.add(activity)
            activities.append(activity)
        
        db.commit()
        
        # Уровень 2
        level2_activities = [
            {"name": "Мясная продукция", "parent_id": activities[0].id, "level": 2, "created_at": datetime.now().isoformat()},  # Еда
            {"name": "Молочная продукция", "parent_id": activities[0].id, "level": 2, "created_at": datetime.now().isoformat()},  # Еда
            {"name": "Овощи и фрукты", "parent_id": activities[0].id, "level": 2, "created_at": datetime.now().isoformat()},  # Еда
            {"name": "Грузовые", "parent_id": activities[1].id, "level": 2, "created_at": datetime.now().isoformat()},  # Автомобили
            {"name": "Легковые", "parent_id": activities[1].id, "level": 2, "created_at": datetime.now().isoformat()},  # Автомобили
            {"name": "Мужская одежда", "parent_id": activities[2].id, "level": 2, "created_at": datetime.now().isoformat()},  # Одежда
            {"name": "Женская одежда", "parent_id": activities[2].id, "level": 2, "created_at": datetime.now().isoformat()},  # Одежда
            {"name": "Ремонт", "parent_id": activities[3].id, "level": 2, "created_at": datetime.now().isoformat()},  # Услуги
            {"name": "Консультации", "parent_id": activities[3].id, "level": 2, "created_at": datetime.now().isoformat()},  # Услуги
        ]
        
        level2_activities_objects = []
        for activity_data in level2_activities:
            activity = models.Activity(**activity_data)
            db.add(activity)
            level2_activities_objects.append(activity)
        
        db.commit()
        
        # Уровень 3
        level3_activities = [
            {"name": "Запчасти", "parent_id": level2_activities_objects[4].id, "level": 3, "created_at": datetime.now().isoformat()},  # Легковые
            {"name": "Аксессуары", "parent_id": level2_activities_objects[4].id, "level": 3, "created_at": datetime.now().isoformat()},  # Легковые
            {"name": "Рубашки", "parent_id": level2_activities_objects[5].id, "level": 3, "created_at": datetime.now().isoformat()},  # Мужская одежда
            {"name": "Брюки", "parent_id": level2_activities_objects[5].id, "level": 3, "created_at": datetime.now().isoformat()},  # Мужская одежда
            {"name": "Платья", "parent_id": level2_activities_objects[6].id, "level": 3, "created_at": datetime.now().isoformat()},  # Женская одежда
            {"name": "Юбки", "parent_id": level2_activities_objects[6].id, "level": 3, "created_at": datetime.now().isoformat()},  # Женская одежда
        ]
        
        level3_activities_objects = []
        for activity_data in level3_activities:
            activity = models.Activity(**activity_data)
            db.add(activity)
            level3_activities_objects.append(activity)
        
        db.commit()
        
        # Создаем организации
        organizations_data = [
            {
                "name": "ООО \"Рога и Копыта\"",
                "building_id": buildings[0].id,
                "phone_numbers": ["2-222-222", "3-333-333", "8-923-666-13-13"],
                "activity_ids": [activities[0].id, level2_activities_objects[0].id],  # Еда, Мясная продукция
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ИП \"Молочный рай\"",
                "building_id": buildings[1].id,
                "phone_numbers": ["4-444-444", "8-999-123-45-67"],
                "activity_ids": [activities[0].id, level2_activities_objects[1].id],  # Еда, Молочная продукция
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ЗАО \"АвтоМир\"",
                "building_id": buildings[2].id,
                "phone_numbers": ["5-555-555"],
                "activity_ids": [activities[1].id, level2_activities_objects[3].id, level2_activities_objects[4].id],  # Автомобили, Грузовые, Легковые
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ООО \"АвтоЗапчасти\"",
                "building_id": buildings[2].id,
                "phone_numbers": ["6-666-666", "8-888-888-88-88"],
                "activity_ids": [level2_activities_objects[4].id, level3_activities_objects[0].id],  # Легковые, Запчасти
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ИП \"Модная одежда\"",
                "building_id": buildings[3].id,
                "phone_numbers": ["7-777-777"],
                "activity_ids": [activities[2].id, level2_activities_objects[5].id, level2_activities_objects[6].id],  # Одежда, Мужская, Женская
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ООО \"Ремонт и сервис\"",
                "building_id": buildings[4].id,
                "phone_numbers": ["8-888-888", "9-999-999"],
                "activity_ids": [activities[3].id, level2_activities_objects[7].id],  # Услуги, Ремонт
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ИП \"Консультант\"",
                "building_id": buildings[0].id,
                "phone_numbers": ["1-111-111"],
                "activity_ids": [activities[3].id, level2_activities_objects[8].id],  # Услуги, Консультации
                "created_at": datetime.now().isoformat()
            },
            {
                "name": "ООО \"Свежие овощи\"",
                "building_id": buildings[1].id,
                "phone_numbers": ["2-333-444"],
                "activity_ids": [activities[0].id, level2_activities_objects[2].id],  # Еда, Овощи и фрукты
                "created_at": datetime.now().isoformat()
            },
        ]
        
        for org_data in organizations_data:
            phone_numbers = org_data.pop("phone_numbers")
            activity_ids = org_data.pop("activity_ids")
            
            organization = models.Organization(**org_data)
            db.add(organization)
            db.flush()  # Получаем ID организации
            
            # Добавляем номера телефонов
            for phone in phone_numbers:
                phone_obj = models.OrganizationPhone(
                    organization_id=organization.id,
                    phone_number=phone
                )
                db.add(phone_obj)
            
            # Добавляем связи с видами деятельности
            for activity_id in activity_ids:
                db.execute(
                    models.organization_activities.insert().values(
                        organization_id=organization.id,
                        activity_id=activity_id
                    )
                )
        
        db.commit()
        print("Тестовые данные успешно добавлены в базу данных!")
        
    except Exception as e:
        print(f"Ошибка при заполнении данными: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("Создание таблиц...")
    create_tables()
    print("Заполнение тестовыми данными...")
    seed_data()
    print("Готово!")

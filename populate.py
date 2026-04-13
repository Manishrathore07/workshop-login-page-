import os
import django
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from workshop_app.models import Profile, Workshop, WorkshopType

def populate():
    # Ensure dependencies exist
    # 1. Create a Workshop Type
    wt1, _ = WorkshopType.objects.get_or_create(
        name="Python Fullstack Bootcamp",
        defaults={
            "description": "Comprehensive course on Django and Python.",
            "terms_and_conditions": "Basic Python knowledge required."
        }
    )
    wt2, _ = WorkshopType.objects.get_or_create(
        name="React & Tailwind Workshop",
        defaults={
            "description": "Modern frontend with Tailwind CSS.",
            "terms_and_conditions": "JS knowledge required."
        }
    )
    wt3, _ = WorkshopType.objects.get_or_create(
        name="Machine Learning Intro",
        defaults={
            "description": "Intro to SciKit Learn.",
            "terms_and_conditions": "Math knowledge required."
        }
    )

    # 2. Create Users/Profiles
    u_coord, _ = User.objects.get_or_create(username='coord1', defaults={'email': 'coord1@fossee.in', 'first_name': 'Alice', 'last_name': 'Smith'})
    p_coord, _ = Profile.objects.get_or_create(user=u_coord, defaults={'position': 'coordinator', 'institute': 'IIT Bombay', 'state': 'Maharashtra', 'is_email_verified': True})
    
    u_inst, _ = User.objects.get_or_create(username='inst1', defaults={'email': 'inst1@fossee.in', 'first_name': 'Bob', 'last_name': 'Jones'})
    p_inst, _ = Profile.objects.get_or_create(user=u_inst, defaults={'position': 'instructor', 'institute': 'FOSSEE', 'state': 'Maharashtra', 'is_email_verified': True})

    # 3. Create Workshops
    now = timezone.now()
    
    w1, created1 = Workshop.objects.get_or_create(
        workshop_type=wt1,
        coordinator=u_coord,
        date=now - timedelta(days=2),
        defaults={
            'instructor': u_inst,
            'status': 1,
            'tnc_accepted': True
        }
    )
    w2, created2 = Workshop.objects.get_or_create(
        workshop_type=wt2,
        coordinator=u_coord,
        date=now - timedelta(days=5),
        defaults={
            'instructor': u_inst,
            'status': 1,
            'tnc_accepted': True
        }
    )
    w3, created3 = Workshop.objects.get_or_create(
        workshop_type=wt3,
        coordinator=u_coord,
        date=now - timedelta(days=1),
        defaults={
            'instructor': u_inst,
            'status': 1,
            'tnc_accepted': True
        }
    )
    
    # 4. Create one upcoming
    w4, created4 = Workshop.objects.get_or_create(
        workshop_type=wt1,
        coordinator=u_coord,
        date=now + timedelta(days=10),
        defaults={
            'instructor': u_inst,
            'status': 1,
            'tnc_accepted': True
        }
    )
    
    print(f"Added workshops: {w1.id}, {w2.id}, {w3.id}, {w4.id}")

if __name__ == '__main__':
    populate()

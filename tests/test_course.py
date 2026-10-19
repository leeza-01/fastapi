import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_course():

    response = client.post(
        "/courses",
        json={
            "course_name": "Python",
            "duration": "6 Months",
            "fees": 25000
        }
    )

    assert response.status_code == 200


def test_get_all_courses():

    response = client.get("/courses")

    assert response.status_code == 200


def test_get_course_by_id():

    response = client.get("/courses/1")

    assert response.status_code == 200


def test_update_course():

    response = client.put(
        "/courses/1",
        json={
            "course_name": "Advanced Python",
            "duration": "8 Months",
            "fees": 30000
        }
    )

    assert response.status_code == 200


def test_delete_course():

    response = client.delete("/courses/1")

    assert response.status_code == 200
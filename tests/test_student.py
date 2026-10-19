import uuid
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_student():

    response = client.post(
        "/students",
        json={
            "student_name": "Test Student",
            "email": f"{uuid.uuid4()}@gmail.com",
            "phone": "9876543210"
        }
    )

    assert response.status_code == 200



def test_get_all_students():

    response = client.get("/students")

    assert response.status_code == 200


def test_get_student_by_id():

    response = client.get("/students/1")

    assert response.status_code == 200


def test_update_student():

    response = client.put(
        "/students/1",
        json={
            "student_name": "Updated Leeza",
            "email": "updated@gmail.com",
            "phone": "9999999999"
        }
    )

    assert response.status_code == 200


def test_delete_student():

    response = client.delete("/students/1")

    assert response.status_code == 200
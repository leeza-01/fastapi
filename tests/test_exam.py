import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_exam():

    response = client.post(
        "/exams",
        json={
            "exam_name": "Python Final Exam",
            "exam_type": "Online",
            "total_marks": 100,
            "exam_date": "2026-10-15"
        }
    )

    assert response.status_code == 200


def test_get_all_exams():

    response = client.get("/exams")

    assert response.status_code == 200


def test_get_exam_by_id():

    response = client.get("/exams/1")

    assert response.status_code == 200


def test_update_exam():

    response = client.put(
        "/exams/1",
        json={
            "exam_name": "Advanced Python Exam",
            "exam_type": "Offline",
            "total_marks": 150,
            "exam_date": "2026-11-01"
        }
    )

    assert response.status_code == 200


def test_delete_exam():

    response = client.delete("/exams/1")

    assert response.status_code == 200

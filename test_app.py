import pytest
from fastapi.testclient import TestClient
from app import app
from models import tasks
from datetime import datetime


@pytest.fixture(scope="module")
def client():
    # Очищаем задачи перед тестами
    tasks.clear()
    with TestClient(app) as c:
        yield c


def test_create_task(client):
    # Тест успешного создания задачи
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "deadline": "20-03-2025"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["deadline"] == "20-03-2025"
    assert "id" in data


def test_create_task_invalid_date(client):
    # Тест с невалидной датой
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "deadline": "invalid-date"
        }
    )
    assert response.status_code == 422  # Unprocessable Entity


def test_get_tasks(client):
    # Тест получения списка задач
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 1:
        # Проверяем сортировку по дате
        dates = [datetime.strptime(task["deadline"], "%d-%m-%Y") for task in data]
        assert dates == sorted(dates)


def test_delete_task(client):
    # Сначала создаем задачу для удаления
    create_response = client.post(
        "/tasks",
        json={
            "title": "To Delete",
            "description": "Will be deleted",
            "deadline": "21-03-2025"
        }
    )
    task_id = create_response.json()["id"]

    # Тест удаления задачи
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Task deleted successfully"

    # Проверяем, что задача действительно удалена
    get_response = client.get("/tasks")
    assert all(task["id"] != task_id for task in get_response.json())


def test_delete_nonexistent_task(client):
    # Тест удаления несуществующей задачи
    response = client.delete("/tasks/non-existent-id")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
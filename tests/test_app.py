import pytest
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'DevSecOps Sample App' in response.get_data(as_text=True)


def test_health_endpoint(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.get_json() == {
        'status': 'ok',
        'message': 'DevSecOps app running',
    }


def test_message_endpoint(client):
    response = client.post('/api/message', json={'text': 'hola'})
    assert response.status_code == 200
    assert response.get_json()['received'] == 'hola'
    assert response.get_json()['length'] == 4

import pytest
from deepraaga_api.serve import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the index route returns a 200 status and correct message."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Deep Raga API is running" in response.data

def test_generate_route_fallback(client):
    """Test the generate route fallback when models aren't loaded."""
    response = client.post('/api/generate', json={
        "raga": "Mayamalavagowla",
        "duration": 10
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'notes' in data
    assert 'C4' in data['notes']

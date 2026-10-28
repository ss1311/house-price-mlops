
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_prediction():
    data = {
        "bedrooms": 3,
        "bathrooms": 2.0,
        "sqft_living": 1800,
        "sqft_lot": 5000,
        "floors": 1.0,
        "waterfront": 0,
        "view": 0,
        "condition": 3,
        "sqft_above": 1500,
        "sqft_basement": 300,
        "yr_built": 1990,
        "yr_renovated": 0,
        "city": "Seattle",
        "statezip": "WA 98103"
    }

    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "predicted_price" in response.json()

def test_create_user(client):
    data = {
        "email": "john@example.com",
        "password": "password123"
    }

    response = client.post("/users/", json=data)  # ✅ fixed path
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"
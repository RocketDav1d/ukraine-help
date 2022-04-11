

from urllib import response


def test_home_success(client):
    #Page loads
    response = client.get("/")
    assert response.status_code == 200

def test_housing_success(client):
    #Page loads
    response = client.get("/housing")
    assert response.status_code == 200

def test_chat_success(client):
    #Page loads
    response = client.get("/chat")
    assert response.status_code == 200

def test_supplies_success(client):
    #Page loads
    response = client.get("/supplies")
    assert response.status_code == 200

def test_login_success(client):
    #Page loads
    response = client.get("/login")
    assert response.status_code == 200

def test_register_success(client):
    #Page loads
    response = client.get("/register")
    assert response.status_code == 200


    

    
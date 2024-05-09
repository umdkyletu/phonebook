import pytest
from flask import url_for
from Website import create_app
from Website.models import User
@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test0(client):
    response = client.get("/login")
    assert b"<h3 style=\"text-align: center;\">Login</h3>" in response.data

def test1(client):
    response = client.get("/signup")
    assert b" <h3 style=\"text-align: center;\">Sign Up</h3>" in response.data


# def test3(client):
#     response = client.get("/")
#     assert b"Contacts" in response.data

def test4(client):
    response = client.get("/logout", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/login"

def test5(client):
    response = client.get("/update/1")
    assert b"<h4 align=\"center\">Update Contact</h4>" in response.data


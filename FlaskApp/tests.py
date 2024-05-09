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


def test3(client):
    response = client.get("/")
    assert b"<h4 align=\"center\">Contacts</h4>" in response.data

def test4(client):
    response = client.get("/logout")
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/login"

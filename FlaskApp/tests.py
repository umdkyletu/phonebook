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

def test_request_example(client):
    response = client.get("/login")
    assert b"<h3 style=\"text-align: center;\">Login</h3>" in response.data
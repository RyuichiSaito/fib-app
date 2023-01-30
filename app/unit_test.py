from .fib import fibonacci
from .main import app
from fastapi.testclient import TestClient
import pytest


client = TestClient(app)


def test_fibonacci_API():
    # Valid input
    response = client.get("/fib?n=10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

    # Invalid input (n < 0)
    response = client.get("/fib?n=-1")
    assert response.status_code == 400
    assert response.json() == {
        "status": 400,
        "message": "Bad Request",
        "error": "n must be >= 0"}

    # Invalid input (n is not an integer)
    with pytest.raises(AssertionError):
        response = client.get("/fib?n=1.5")
        assert response.status_code == 400


def test_fibonacci_function():
    # Valid input
    assert fibonacci(10) == 55

    # Invalid input
    with pytest.raises(ValueError):
        fibonacci(-1)


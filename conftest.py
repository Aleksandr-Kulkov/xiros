import requests
from settings import login, password, url_balancer_ural
import pytest
import datetime
from requests.auth import HTTPBasicAuth

s = requests.Session()
s.auth = HTTPBasicAuth(username=login, password=password)

@pytest.fixture
def basic_auth_header():
    """Фикстура возвращает значение заголовка Authorization запроса при Basic Auth."""

    data = {
        "CCID": "777",
        "SPN": "7676",
        "Reg": "LCC",
        "LS": "777888555444"
    }

    response = s.post(url=url_balancer_ural, json=data)
    auth_header = response.request.headers.get('Authorization')
    return auth_header

@pytest.fixture(scope='function', autouse=True)
def time_delta():
    """Фикстура выводит на печать время выполнения теста."""
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    return print(f"\nВремя выполнения теста: {end_time - start_time}")

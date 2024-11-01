import requests
import json
from settings import url_balancer_ural, api_username, api_appkid


class BringsController:
    def __init__(self):
        self.orgus_module = url_balancer_ural

    def post_brings_basic_auth(self, auth_header: str, ccid: str, spn: str, reg: str, ls: str) -> json:
        """Модуль orgus_module, brings-controller, метод POST /brings, Basic Auth."""

        headers = {'Authorization': auth_header}

        data = {
            "CCID": ccid,
            "SPN": spn,
            "Reg": reg,
            "LS": ls
        }

        response = requests.post(self.orgus_module, headers=headers, json=data)

        status = response.status_code
        result = ''
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

    def post_brings_api_auth(self, ccid: str, spn: str, reg: str, ls: str) -> json:
        """Модуль orgus_module, brings-controller, метод POST /brings, api auth."""

        headers = {
            'X-Auth-User': api_username,
            'X-Auth-Key': api_appkid
        }

        data = {
            "CCID": ccid,
            "SPN": spn,
            "Reg": reg,
            "LS": ls
        }

        response = requests.post(self.orgus_module, headers=headers, json=data)

        status = response.status_code
        result = ''
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

    def post_brings_without_auth(self, ccid: str, spn: str, reg: str, ls: str) -> json:
        """Модуль orgus_module, brings-controller, метод POST /brings, without Auth."""

        data = {
            "CCID": ccid,
            "SPN": spn,
            "Reg": reg,
            "LS": ls
        }

        response = requests.post(self.orgus_module, json=data)

        status = response.status_code
        result = ''
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

    def delete_brings_basic_auth(self, auth_header: str, ccid: str, spn: str) -> json:
        """Модуль orgus_module, brings-controller, метод DELETE /brings, Basic Auth."""

        headers = {'Authorization': auth_header}

        data = {
            "CCID": ccid,
            "SPN": spn
        }

        response = requests.delete(self.orgus_module, headers=headers, json=data)

        status = response.status_code
        result = ''
        try:
            result = response.json()
        except:
            result = response.text
        return status, result

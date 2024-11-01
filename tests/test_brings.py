from orgus_module_rest import BringsController
import pytest
from conftest import basic_auth_header

bc = BringsController()


class TestBringsController:
    @pytest.mark.auth
    def test_post_brings_basic_auth(self, basic_auth_header, ccid='777', spn='7676', reg='LCC', ls='777888555444'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Basic Auth. Все параметры. Валидные значения параметров.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.post_brings_basic_auth(basic_auth_header, ccid, spn, reg, ls)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.auth
    def test_post_brings_api_auth(self, ccid='777', spn='7676', reg='LCC', ls='777888555444'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        api Auth. Все параметры. Валидные значения параметров.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.post_brings_api_auth(ccid, spn, reg, ls)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.auth
    def test_post_brings_without_auth(self, ccid='777', spn='7676', reg='LCC', ls='777888555444'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Без Auth. Все параметры. Валидные значения параметров.
        status_code=401"""

        status, result = bc.post_brings_without_auth(ccid, spn, reg, ls)
        assert status == 401

    @pytest.mark.api
    def test_post_brings_empty_ccid(self, basic_auth_header, ccid='', spn='7676', reg='LCC', ls='777888555444'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Basic Auth. ccid=''.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.post_brings_basic_auth(basic_auth_header, ccid, spn, reg, ls)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.api
    def test_post_brings_empty_spn(self, basic_auth_header, ccid='777', spn='', reg='LCC', ls='777888555444'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Basic Auth. spn=''.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.post_brings_basic_auth(basic_auth_header, ccid, spn, reg, ls)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.api
    def test_post_brings_invalid_reg(self, basic_auth_header, ccid='888', spn='11111', reg='MVP',
                                      ls='123456789123'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Basic Auth. Невалидный reg.
        status_code=500. resCode=400. resComment!='' """

        status, result = bc.post_brings_basic_auth(basic_auth_header, ccid, spn, reg, ls)
        assert status == 500
        assert result['resCode'] == 400
        assert result['resComment']

    @pytest.mark.api
    def test_post_brings_empty_ccid_empty_spn(self, basic_auth_header, ccid='', spn='', reg='LCC', ls='777888555444'):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Basic Auth. ccid='', spn=''.
        status_code=500. resCode=1002. resComment!='' """

        status, result = bc.post_brings_basic_auth(basic_auth_header, ccid, spn, reg, ls)
        assert status == 500
        assert result['resCode'] == 1002
        assert result['resComment']

    @pytest.mark.api
    def test_delete_brings_basic_auth(self, basic_auth_header, ccid='777', spn='7676'):
        """Тест. Модуль orgus_module, brings-controller, метод DELETE /brings.
        Basic Auth. Все параметры. Валидные значения параметров.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.delete_brings_basic_auth(basic_auth_header, ccid, spn)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.api
    def test_delete_brings_empty_ccid(self, basic_auth_header, ccid='', spn='7676'):
        """Тест. Модуль orgus_module, brings-controller, метод DELETE /brings.
        Basic Auth. ccid=''.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.delete_brings_basic_auth(basic_auth_header, ccid, spn)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.api
    def test_delete_brings_empty_spn(self, basic_auth_header, ccid='777', spn=''):
        """Тест. Модуль orgus_module, brings-controller, метод DELETE /brings.
        Basic Auth. spn=''.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.delete_brings_basic_auth(basic_auth_header, ccid, spn)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.api
    def test_delete_brings_empty_ccid_empty_spn(self, basic_auth_header, ccid='', spn=''):
        """Тест. Модуль orgus_module, brings-controller, метод DELETE /brings.
        Basic Auth. ccid='', spn=''.
        status_code=500. resCode=400. resComment!='' """

        status, result = bc.delete_brings_basic_auth(basic_auth_header, ccid, spn)
        assert status == 500
        assert result['resCode'] == 400
        assert result['resComment']

    @pytest.mark.api
    @pytest.mark.parametrize('ccid', ['777'],
                             ids=['valid_ccid'])
    @pytest.mark.parametrize('spn', ['7676'],
                             ids=['valid_spn'])
    @pytest.mark.parametrize('reg', ['Ural-stage', 'NorthWest-stage', 'LCC', 'Volga-stage', 'South',
                                        'Siberia-stage', 'South-stage', 'FarEast', 'Center-stage', 'FarEast-stage',
                                        'NorthWest', 'Volga', 'Ural', 'Siberia', 'Center'],
                             ids=['Ural_stage', 'NorthWest_stage', 'LCC', 'Volga_stage', 'South',
                                  'Siberia_stage', 'South_stage', 'FarEast', 'Center_stage', 'FarEast_stage',
                                  'NorthWest', 'Volga', 'Ural', 'Siberia', 'Center'])
    @pytest.mark.parametrize('ls', ['777888555444'],
                             ids=['valid_ls'])
    def test_post_brings_valid_reg(self, basic_auth_header, ccid, spn, reg, ls):
        """Тест. Модуль orgus_module, brings-controller, метод POST /brings.
        Basic Auth. Все параметры. Валидные значения параметров.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.post_brings_basic_auth(basic_auth_header, ccid, spn, reg, ls)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

    @pytest.mark.api
    @pytest.mark.parametrize('ccid, spn', [('777', '7676'), ('777', '11111'), ('888', '7676'), ('888', '11111')],
                             ids=['test_case_1', 'test_case_2', 'test_case_3', 'test_case_4'])
    def test_delete_brings_valid_params(self, basic_auth_header, ccid, spn):
        """Тест. Модуль orgus_module, brings-controller, метод DELETE /brings.
        Basic Auth. Все параметры. Валидные значения параметров.
        status_code=200. resCode=0. resComment!='' """

        status, result = bc.delete_brings_basic_auth(basic_auth_header, ccid, spn)
        assert status == 200
        assert result['resCode'] == 0
        assert result['resComment']

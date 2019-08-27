from pytest_training import functions
from pytest_training import functions2
import pytest
import sys


# *************************************************
def test_add():
    assert functions.add(1, 2) == 3


# def test_multiply():
#     assert functions2.multiply(2, 5) == 10
# *************************************************

# class TestTof:
#     def test_tof_1(self):
#         assert functions.t_or_f(4) is True
#
#     def test_tof_2(self):
#         assert functions.t_or_f(7) is False
#
#     def test_tof_3(self):
#         assert functions.t_or_f(15) is None

# *************************************************

# def test_tof():
#     assert functions.t_or_f(4) is True
#     assert functions.t_or_f(7) is False
#     assert functions.t_or_f(15) is None

# *************************************************

# @pytest.mark.parametrize('test_input, expected', [(4, True), (7, False), (15, None)])
# def test_tof_param(test_input, expected):
#     assert functions.t_or_f(test_input) is expected
#
# # *************************************************
#
# @pytest.mark.skip(reason='Function is not implemented yet...')
# def test_not_implemented(a. b):
#     ...
#
#
# def test_not_implemented2():
#     pytest.skip('Function not implemented.')
#
#
# @pytest.mark.skipif(sys.platform.startswith("win"), reason="Test run on windows")
# def test_linux_only():
#     assert functions.linux_function() is True
#
#
# @pytest.mark.xfail
# def test_impossible():
#     assert functions.impossible_function() == 'Filip is amazing!'
#
#

def response_mock():
    return 'Filip is amazing!'


@pytest.mark.xfail
def test_impossible2(monkeypatch):
    monkeypatch.setattr(functions, 'impossible_function', response_mock)
    assert functions.impossible_function() == 'Filip is amazing!'
#
#
# @pytest.mark.xfail(raises=IndexError)
# def test_raises():
#     assert functions.raises() is True

# *************************************************


def test_getting_response_get(mocker):
    from pytest_training.functions import getting_response
    req = mocker.MagicMock()
    req.method = 'GET'
    assert getting_response(req) == {}


def test_getting_response_post(mocker):
    from pytest_training.functions import getting_response
    req = mocker.MagicMock()
    req.method = 'POST'
    req.POST = {'title': 'title', 'body': 'body'}
    assert getting_response(req) == {'title': 'title', 'body': 'body'}


def test_create_file(tmp_path):
    CONTENT = 'content'
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1

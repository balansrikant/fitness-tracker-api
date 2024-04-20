import pytest

from src.utilities.sample_module.sample_module import SampleModule


def test_get_number():
    sample_module = SampleModule()
    actual_number = sample_module.get_number()
    expected_number = 1

    # https://stackoverflow.com/questions/53651193/what-is-the-correct-order-for-actual-and-expected-in-pytest
    # https://stackoverflow.com/questions/24617397/how-do-i-print-to-console-in-pytest
    assert actual_number == expected_number


# https://docs.pytest.org/en/4.6.x/monkeypatch.html#:~:text=of%20its%20motivation.-,Simple%20example%3A%20monkeypatching%20functions,-%C2%B6
def test_get_number_mocked(monkeypatch):
    def mock_get_number(*args, **kwargs):
        return 3

    monkeypatch.setattr(SampleModule, 'get_number', mock_get_number)
    sample_module = SampleModule()
    actual_number = sample_module.get_number()
    expected_number = 3
    assert actual_number == expected_number


def test_get_alphabet_mocked_fixture():
    sample_module = SampleModule()
    actual_alphabet = sample_module.get_alphabet()
    expected_alphabet = 'b'
    assert actual_alphabet == expected_alphabet

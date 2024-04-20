import os
import sys
import pytest
from src.utilities.sample_module.sample_module import SampleModule

# directory of current file
# https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(src_path)
print(src_path)


@pytest.fixture(autouse=True)
def mock_sample_module(monkeypatch):
    def mock_get_alphabet(*args, **kwargs):
        return 'b'

    monkeypatch.setattr(SampleModule, 'get_alphabet', mock_get_alphabet)

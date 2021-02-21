# Run with pytest -rx -v 3_5_step6.py

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True

@pytest.mark.xfail()
def test_not_succees():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False
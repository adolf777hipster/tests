import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True
    # if not test_not_succeed():
    #     pytest.xfail("failing configuration (but should work)")


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

import pytest

from gradebook.gradebook import validate_name


@pytest.mark.parametrize('name', [
    'Ali Khan',
])
def test_validate_name_valid(name):
    assert validate_name(name) is True


@pytest.mark.parametrize('name', [
    '',
    'A' * 51,
    'Ali123',
])
def test_validate_name_invalid(name):
    with pytest.raises(ValueError):
        validate_name(name)
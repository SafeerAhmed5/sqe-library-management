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


@pytest.mark.parametrize('name,expected_error', [
    ('', True),
    ('A', False),
    ('A' * 49, False),
    ('A' * 50, False),
    ('A' * 51, True),
])
def test_validate_name_length_boundaries(name, expected_error):
    if expected_error:
        with pytest.raises(ValueError):
            validate_name(name)
    else:
        assert validate_name(name) is True
import pytest
import lottery
from lottery import create_ticket
from person import Person


@pytest.fixture
def dummy_person():
    return Person('person', 'password', 20)

def test_create_ticket(dummy_person, capsys, monkeypatch):
    inputs = iter([1, 2, 3, 4, 5, 6, 1])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_ticket(dummy_person)
    assert dummy_person.balance == 18
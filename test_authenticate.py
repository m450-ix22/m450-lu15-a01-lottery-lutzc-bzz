from authenticate import load_people, login

def test_type_load_people():
    people = load_people()
    assert type(people) == list

def test_load_people():
    people = load_people()
    assert len(people) > 0

def test_login(monkeypatch):
    people = load_people()
    for i in range(len(people)):
        person = people[i]
        password = person.password
        inputs = iter([password])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        result = login()
        assert result == person

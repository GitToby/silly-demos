from typing import Set

_data = dict()


def get_locations(name: str) -> Set[str]:
    return _data[name]


def book_location(location: str, name: str) -> Set[str]:
    my_locations = _data.get(name, set())
    my_locations.add(location)
    _data[name] = my_locations
    return get_locations(name)

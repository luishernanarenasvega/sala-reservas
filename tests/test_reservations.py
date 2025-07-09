from app.reservations import check_availability

def test_available_room():
    reservations = [
        {"room": "A", "time": "10:00"},
        {"room": "A", "time": "11:00"}
    ]
    new = {"room": "A", "time": "12:00"}
    assert check_availability(reservations, new) == True

def test_unavailable_room():
    reservations = [
        {"room": "A", "time": "10:00"},
        {"room": "A", "time": "11:00"}
    ]
    new = {"room": "A", "time": "11:00"}
    assert check_availability(reservations, new) == False
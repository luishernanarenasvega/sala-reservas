def check_availability(reservations, new):
    for reservation in reservations:
        if reservation["room"] == new["room"] and reservation["time"] == new["time"]:
            return False
    return True
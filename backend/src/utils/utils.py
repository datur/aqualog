import uuid

def parse_uuid(uid):
    try:
        return uuid.UUID(uid)
    except ValueError:
        return False
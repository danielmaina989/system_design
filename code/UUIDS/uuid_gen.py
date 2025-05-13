# uuid_gen.py
import uuid

def generate_uuid():
    return str(uuid.uuid4())

print("UUID:", generate_uuid())

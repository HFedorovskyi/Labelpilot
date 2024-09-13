import uuid
from datebase.datebase_main import UUID
from datebase.datebase_main import get_db_session


def ger_or_create_uuid():
    with (get_db_session() as db):
        curren_uuid = db.query(UUID).first()
        if not curren_uuid:
            generated_uuid = str(uuid.uuid4())
            new_uuid = UUID(uuid_client=generated_uuid)
            db.add(new_uuid)
            db.commit()
            return generated_uuid
        return curren_uuid.uuid_client


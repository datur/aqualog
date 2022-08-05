
from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass(kw_only=True)
class Base:
    id: uuid.UUID = uuid.uuid4()
    created: datetime = datetime.now()
    last_updated: datetime = datetime.now()
    is_deleted: bool = False

    def update(self,newdata):
        for key,value in newdata.items():
            setattr(self,key,value)
        self.last_updated = datetime.now()
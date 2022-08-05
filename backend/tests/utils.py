from typing import List, Any


class FakeRepository:
    def __init__(self, items: List[Any]):
        self.items = items

    def add(self, item):
        self.items.append(item)
        return item

    def read(self, id):
        result = self.items
        filters = {"id": id}
        for k, v in filters.items():
            remove = [x for x in self.items if x.__getattribute__(k) != v]
            if remove is not []:
                for r in remove:
                    result.remove(r)

        if len(result) > 0:
            return result[0]

        return result

    def list(self, filters):
        result = self.items
        for k, v in filters.items():
            remove = [x for x in self.items if x.__getattribute__(k) != v]
            if remove is not []:
                for r in remove:
                    result.remove(r)

        return remove

    def update(self, filters, update):

        result = self.read(filters)

        for key,value in update.items():
            setattr(result,key,value)

    def soft_delete(self, filters):
        self.update(filters, {"is_deleted": True})
    
    def restore(self, filters):
        self.update(filters, {"is_deleted": False})

    def delete(self, filters):

        result = self.read(filters)

        self.items.remove(result)

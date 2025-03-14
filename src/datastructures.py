from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

   
    def _generateId(self):
        return randint(0, 99999999)

    
    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        member["last_name"] = self.last_name  
        self._members.append(member)
        return member  

    
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False  

    
    def get_member(self, id):
        return next((m for m in self._members if m["id"] == id), None)

    
    def update_member(self, id, updated_data):
        for member in self._members:
            if member["id"] == id:
                member.update(updated_data)  
                return member
        return None  

    
    def get_all_members(self):
        return self._members

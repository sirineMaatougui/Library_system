class Member:
    # Encapsulation: member_id privé
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.name = name

    def get_member_id(self):
        return self.__member_id

    def display_info(self):
        print(f"[Member] ID:{self.__member_id} | Name:{self.name}")

    def to_dict(self):
        return {
            "member_id": self.__member_id,
            "name": self.name
        }

    @staticmethod
    def from_dict(d):
        return Member(d["member_id"], d["name"])

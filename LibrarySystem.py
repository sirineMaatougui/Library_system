# LibrarySystem.py
from DataStore import DataStore
from Book import Book
from Magazine import Magazine
from Member import Member

class LibrarySystem:
    def __init__(self):
        self.items = []
        self.members = []
        self.next_item_id = 1
        self.next_member_id = 1

    # Persistence 
    def load(self):
        data = DataStore.load()

        # load items
        self.items = []
        for d in data.get("items", []):
            if d.get("type") == "Book":
                self.items.append(Book.from_dict(d))
            elif d.get("type") == "Magazine":
                self.items.append(Magazine.from_dict(d))

        # load members
        self.members = []
        for d in data.get("members", []):
            self.members.append(Member.from_dict(d))

        # update IDs
        if len(self.items) > 0:
            self.next_item_id = max(i.item_id for i in self.items) + 1
        if len(self.members) > 0:
            self.next_member_id = max(m.get_member_id() for m in self.members) + 1

    def save(self):
        data = {
            "items": [i.to_dict() for i in self.items],
            "members": [m.to_dict() for m in self.members]
        }
        DataStore.save(data)

    #  Helpers 
    def find_item(self, item_id):
        for i in self.items:
            if i.item_id == item_id:
                return i
        return None

    def find_member(self, member_id):
        for m in self.members:
            if m.get_member_id() == member_id:
                return m
        return None

    # Items 
    def add_book(self, title, author):
        b = Book(self.next_item_id, title, author)
        self.items.append(b)
        self.next_item_id += 1

    def add_magazine(self, title, issue):
        mg = Magazine(self.next_item_id, title, issue)
        self.items.append(mg)
        self.next_item_id += 1

    def list_items(self):
        if len(self.items) == 0:
            print("No items yet.")
            return
        for i in self.items:
            i.display_info()  # polymorphism

    # Members 
    def add_member(self, name):
        m = Member(self.next_member_id, name)
        self.members.append(m)
        self.next_member_id += 1

    def list_members(self):
        if len(self.members) == 0:
            print("No members yet.")
            return
        for m in self.members:
            m.display_info()

    # Borrow / Return 
    def borrow_item(self, item_id, member_id):
        item = self.find_item(item_id)
        member = self.find_member(member_id)

        if item is None:
            print("Item not found.")
            return
        if member is None:
            print("Member not found.")
            return
        if item.available is False:
            print("This item is already borrowed.")
            return

        item.available = False
        item.borrowed_by = member_id
        print("Borrow done ✅")

    def return_item(self, item_id):
        item = self.find_item(item_id)
        if item is None:
            print("Item not found.")
            return
        if item.available is True:
            print("This item is already available (not borrowed).")
            return

        item.available = True
        item.borrowed_by = None
        print("Return done ✅")

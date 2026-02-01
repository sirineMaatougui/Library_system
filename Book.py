from LibraryItem import LibraryItem

class Book(LibraryItem):
    def __init__(self, item_id, title, author, available=True, borrowed_by=None):
        super().__init__(item_id, title, available, borrowed_by)
        self.author = author

    # Polymorphism: override display_info()
    def display_info(self):
        status = "Available" if self.available else f"Borrowed by Member ID {self.borrowed_by}"
        print(f"[Book] ID:{self.item_id} | Title:{self.title} | Author:{self.author} | {status}")

    def to_dict(self):
        return {
            "type": "Book",
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "available": self.available,
            "borrowed_by": self.borrowed_by
        }

    @staticmethod
    def from_dict(d):
        return Book(
            d["item_id"],
            d["title"],
            d["author"],
            d.get("available", True),
            d.get("borrowed_by", None)
        )

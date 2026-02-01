from LibraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue, available=True, borrowed_by=None):
        super().__init__(item_id, title, available, borrowed_by)
        self.issue = issue

    # Polymorphism: override display_info()
    def display_info(self):
        status = "Available" if self.available else f"Borrowed by Member ID {self.borrowed_by}"
        print(f"[Magazine] ID:{self.item_id} | Title:{self.title} | Issue:{self.issue} | {status}")

    def to_dict(self):
        return {
            "type": "Magazine",
            "item_id": self.item_id,
            "title": self.title,
            "issue": self.issue,
            "available": self.available,
            "borrowed_by": self.borrowed_by
        }

    @staticmethod
    def from_dict(d):
        return Magazine(
            d["item_id"],
            d["title"],
            d["issue"],
            d.get("available", True),
            d.get("borrowed_by", None)
        )

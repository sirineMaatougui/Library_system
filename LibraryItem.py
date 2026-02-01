class LibraryItem:
    # Abstraction: les enfants doivent implémenter display_info()
    def __init__(self, item_id, title, available=True, borrowed_by=None):
        self.item_id = item_id
        self.title = title
        self.available = available
        self.borrowed_by = borrowed_by  # member_id ou None

    def display_info(self):
        raise NotImplementedError("display_info() must be implemented by child classes")

class ConsoleUI:
    def __init__(self, sys):
        self.sys = sys

    def _items_menu(self):
        while True:
            print("\n--- ITEMS MENU ---")
            print("1) Add Book")
            print("2) Add Magazine")
            print("3) List Items")
            print("4) Back")
            choice = input("Choose: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                self.sys.add_book(title, author)
                self.sys.save()  # AUTOSAVE
                print("Book saved ✅ (autosave)")

            elif choice == "2":
                title = input("Enter magazine title: ")
                issue = input("Enter issue number: ")
                if not issue.isdigit():
                    print("Issue must be a number.")
                else:
                    self.sys.add_magazine(title, int(issue))
                    self.sys.save()  # AUTOSAVE
                    print("Magazine saved ✅ (autosave)")

            elif choice == "3":
                self.sys.list_items()

            elif choice == "4":
                break
            else:
                print("Invalid choice.")

    def _members_menu(self):
        while True:
            print("\n--- MEMBERS MENU ---")
            print("1) Add Member")
            print("2) List Members")
            print("3) Back")
            choice = input("Choose: ")

            if choice == "1":
                name = input("Enter member name: ")
                self.sys.add_member(name)
                self.sys.save()  # AUTOSAVE
                print("Member saved ✅ (autosave)")

            elif choice == "2":
                self.sys.list_members()

            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def _borrow_menu(self):
        while True:
            print("\n--- BORROW / RETURN ---")
            print("1) Borrow Item")
            print("2) Return Item")
            print("3) Back")
            choice = input("Choose: ")

            if choice == "1":
                item_id = input("Enter item ID: ")
                member_id = input("Enter member ID: ")
                if not item_id.isdigit() or not member_id.isdigit():
                    print("IDs must be numbers.")
                else:
                    self.sys.borrow_item(int(item_id), int(member_id))
                    self.sys.save()  # AUTOSAVE
                    print("Saved ✅ (autosave)")

            elif choice == "2":
                item_id = input("Enter item ID: ")
                if not item_id.isdigit():
                    print("Item ID must be a number.")
                else:
                    self.sys.return_item(int(item_id))
                    self.sys.save()  # AUTOSAVE
                    print("Saved ✅ (autosave)")

            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def run(self):
        print("Welcome! Data loaded ✅ (autoload)")

        while True:
            print("\n===== LIBRARY SYSTEM =====")
            print("1) Items")
            print("2) Members")
            print("3) Borrow / Return")
            print("4) Exit")
            choice = input("Choose: ")

            if choice == "1":
                self._items_menu()
            elif choice == "2":
                self._members_menu()
            elif choice == "3":
                self._borrow_menu()
            elif choice == "4":
                self.sys.save()
                print("Goodbye! Data saved ✅")
                break
            else:
                print("Invalid choice.")

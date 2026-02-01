from LibrarySystem import LibrarySystem
from ConsoleUI import ConsoleUI

def run_app():
    sys = LibrarySystem()
    sys.load()  # AUTOLOAD
    ui = ConsoleUI(sys)
    ui.run()

class BotState:
    def __init__(self):
        self.first_scan = False  # Initialize the scanned state.
        self.active_scanning =False

    def start_scanning(self):
        self.active_scanning = True
        self.first_scan = True

    def stop_scanning(self):
        self.active_scanning = False

    def failed_scanning(self):
        self.active_scanning = False
        self.first_scan = False

    def scanned(self):
        self.first_scan = True

    def not_scanned(self):
        self.first_scan = False


# You can create a singleton instance here or instantiate it in your main bot setup.
bot_state = BotState()

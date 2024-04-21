class BotState:
    def __init__(self):
        self.first_scan = {}  # Initialize the scanned state.
        self.active_scanning = {}

    def start_scanning(self, guild_id):
        self.active_scanning[guild_id] = True
        self.first_scan[guild_id] = True

    def stop_scanning(self, guild_id):
        self.active_scanning[guild_id] = False

    def failed_scanning(self, guild_id):
        self.active_scanning[guild_id] = False
        self.first_scan[guild_id] = False

    def scanned(self, guild_id):
        self.first_scan[guild_id] = True

    def not_scanned(self, guild_id):
        self.first_scan[guild_id] = False


# You can create a singleton instance here or instantiate it in your main bot setup.
bot_state = BotState()

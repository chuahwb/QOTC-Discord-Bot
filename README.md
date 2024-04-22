# QOTC Bot

QOTC Bot is a Discord bot designed to manage and visualize over-the-counter (OTC) trading data within designated Discord channels. It allows channel participants to input their buy or sell orders, which the bot then processes to generate and display histograms of the trading data.

## Installation

Follow these steps to set up the QOTC Bot in your local environment:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/chuahwb/QOTC-Discord-Bot.git
   cd QOTC-Discord-Bot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the root directory and populate it with the necessary environment variables:
   ```plaintext
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

## Configuration

Before running the bot, ensure that you have the following configurations set:

- **Discord Token**: Your bot's token must be set in the `.env` file as `DISCORD_TOKEN`.
- **Permissions**: The bot requires permissions to manage roles, read messages, send messages, read message history, attach files, manage messages, use slash commands and manage channels in your Discord server.

## Usage

To run the bot:
```bash
python main.py
```

### Commands
- **/qotc_scan [type] [number]**: Initiates a scan of the channel's message history based on the specified type (`count`, `days`, `months`) and number.
- **/qotc_reset**: Resets the collected trade data.
- **/qotc_dist**: Displays the distribution histograms for the buy and sell orders.

## User Guide

### Initial Activation
To activate the bot and start using its features, you must first use the `/qotc_scan` command. This command initiates a scan of the channel's historical messages to capture and analyze past trading data. It is essential to run this command whenever you start the bot for the first time or in a new server.

### Scanning Process
During the scanning process:
- The bot temporarily sets the channel to read-only mode for members with basic roles to prevent new messages from affecting the scan.
- Only members with higher privileges can type in the channel during the scan.

### Continuous Data Capture
Once the initial scan is complete:
- The bot will continuously listen to and store new user entries in the database.
- All commands and trade entries are logged and will be included in the data visualization when the `/qotc_dist` command is called.

### Visualizing Data
- Use the `/qotc_dist` command to generate and view histograms showing the distribution of buy and sell orders. This visualization will include both historically scanned data and any new data captured after the scan.

### Resetting the Bot
- If you need to clear the database and stop the bot from listening to new entries, use the `/qotc_reset` command.
- After using `/qotc_reset`, you must run `/qotc_scan` again to reactivate the bot's listening and data storage capabilities.

### Important Notes
- Ensure that you perform the initial scan (`/qotc_scan`) each time the bot is added to a new server or restarted to ensure accurate data handling.
- The bot is designed to handle server-specific data securely, maintaining data isolation across different servers.

## Support

For support, feature requests, or bug reporting, you can contact Jae Chuah at chuahwb@gmail.com.

## Contributing

Contributions to the QOTC Bot are welcome! Please read the CONTRIBUTING.md file for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

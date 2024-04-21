# QOTC Bot

QOTC Bot is a Discord bot designed to manage and visualize over-the-counter (OTC) trading data within designated Discord channels. It allows channel participants to input their buy or sell orders, which the bot then processes to generate and display histograms of the trading data.

## Installation

Follow these steps to set up the QOTC Bot in your local environment:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/chuahwb/QOTC-Discord-Bot.git
   cd qotc-bot
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

## Support

For support, feature requests, or bug reporting, you can contact Jae Chuah at chuahwb@gmail.com.

## Contributing

Contributions to the QOTC Bot are welcome! Please read the CONTRIBUTING.md file for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

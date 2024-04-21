import re


def update_trade_data(trade_data, action, quantity, price):
    """
    Updates the trading data dictionary based on the action, quantity, and price provided.

    Args:
        trade_data (dict): A dictionary holding buy and sell data.
        action (str): Specifies whether the action is 'wts' (want to sell) or 'wtb' (want to buy).
        quantity (int): The amount of the item being traded.
        price (float): The price per item in the trade.
    """
    key = 'sell' if action.lower() == 'wts' else 'buy'
    if price not in trade_data[key]:
        trade_data[key][price] = 0
    trade_data[key][price] += quantity
    print(
        f"Updated trade data after {action} operation: \nBuy data: {trade_data['buy']}, \nSell data: {trade_data['sell']}")


def parse_quantity(qty_str, unit):
    """
    Parses a quantity string with a unit and converts it into an integer.

    Args:
        qty_str (str): The quantity string, e.g., '1.5K', '2m'.
        unit (str): A single character denoting the unit ('k', 'm', 'b').

    Returns:
        int: The quantity in integer form, taking into account the unit.
    """
    # Normalize the string by removing spaces and handling commas and periods
    qty_str = qty_str.replace(',', '')  # Remove commas first

    # Check if the unit is used, which indicates the dot should be a decimal point
    if unit in 'kKmMbB' and unit != "":
        base = float(qty_str)  # Treat dot as a decimal point
    else:
        # If no unit and the string has dots (potentially as thousand separators), handle accordingly
        base = float(qty_str.replace('.', ''))

    # Apply the appropriate multiplier based on the unit
    if unit.lower() == 'k':
        return base * 1000
    elif unit.lower() == 'm':
        return base * 1000000
    elif unit.lower() == 'b':
        return base * 1000000000
    return base


# Regular expression to parse various message formats
# Updated to be case-insensitive and ignore "@" and "$" more flexibly
message_pattern = re.compile(
    r"(wts|wtb)\s+(\d{1,3}(?:[.,]\d{3})*|\d*\.?\d+)\s*([kKmMbB]?)\s*[^0-9.]*?(\d+(?:\.\d+)?)\$?", re.IGNORECASE)


def process_message(message):
    """
    Processes a single message to extract trading commands and updates the trade data accordingly.

    Args:
        message (discord.Message): The message object to process.
    """
    from data.storage import trade_data

    if message.author != message.author.bot:  # Check that the message is not from the bot itself
        # Skip command messages when scanned is True
        content = message.content
        match = message_pattern.search(content)
        if match:
            action = match.group(1).upper()
            quantity_string = match.group(2)
            unit = match.group(3).lower()
            price = float(match.group(4))
            if price != 0.0:
                quantity = parse_quantity(quantity_string, unit)
                update_trade_data(trade_data, action, quantity, price)
                print(
                    f"Action: {action}, Quantity: {quantity}, Price: {price}")

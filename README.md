# Telegram Python Bot - Expense Tracker

This is a Telegram bot that helps you track your expenses by allowing you to register transactions via text.

## Getting Started

To use the bot, follow these steps:

1. Open Telegram and search for the bot with the username: `https://t.me/accountantInvoiceRecordingBot`.
2. To register an expense, use the following format: `<amount>, <description>`. For example: `50, Restaurante`.

## Features

- **Expense Registration**: Register your expenses with the bot using simple text commands.
- **Expense Listing**: View a list of your registered expenses with the bot.
- **Total Expenses**: Check the total amount of expenses you have registered.

## How It Works

The bot is built using Python and relies on the Telegram Bot API to handle user interactions. It uses a simple text-based command system to register expenses. When you send a command like `50, Restaurante`, the bot will parse the text, extract the amount and description, and then store the transaction in a database.

The project structure is as follows:


## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip3`:

3. Configure the bot by editing the `config.py` file and adding your Telegram Bot API token.

## Running the Bot

To run the bot, simply execute the `main.py` script:

```
python3 main.py
```

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of the `python-telegram-bot` library for making it easy to build Telegram bots in Python.

---

# Trading Bot (Binance Futures Testnet)

##  Overview

This project is a simple Python-based trading bot that simulates placing MARKET and LIMIT orders on Binance Futures Testnet.

It is designed with clean structure, CLI input, logging, and error handling.

---

##  Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input (argparse)
* Input validation
* Logging of requests, responses, and errors
* Structured and modular code

---

##  Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── README.md
├── requirements.txt
├── .env
├── bot.log
```

---

##  Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/trading_bot.git
cd trading_bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

##  How to Run

### MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000
```

---

##  Sample Output

```
Order Result:
{
  'orderId': 123456,
  'symbol': 'BTCUSDT',
  'status': 'FILLED'
}
```

---

## Logging

Logs are saved in:

```
bot.log
```

Includes:

* API errors
* Order responses
* Execution details

---

##  Note

Due to API access limitations, order responses are simulated for demonstration purposes.

---

##  Author

Avinash

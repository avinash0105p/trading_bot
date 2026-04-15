import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
import logging
from bot.logging_config import *

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("Order Result:")
        print(order)

        logging.info(order)

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))

if __name__ == "__main__":
    main()
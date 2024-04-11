from __future__ import annotations

from argparse import ArgumentParser, Namespace

from currency_converter import ECB_URL, CurrencyConverter


def profit_split(split: str) -> float:
    "Take `split` as a string and convert to percentage."
    converted = float(split)
    if converted < 0 or converted > 100:
        raise ValueError

    return converted / 100


def print_args(args: Namespace) -> None:
    "Print all the command line arguments."
    print(f"Amount: {args.amount}")
    print(f"Profit split: {round(args.split * 100, 2)}")
    print(f"Convert from: {args.convert_from}")
    print(f"Convert to: {args.convert_to}")


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("-a", "--amount", type=float, required=True, help="The amount before the profit split.")
    parser.add_argument(
        "-s", "--split", type=profit_split, default="80", help="The profit split as a value between 0-100."
    )
    parser.add_argument("-f", "--convert-from", type=str, default="USD", help="The account currency.")
    parser.add_argument("-t", "--convert-to", type=str, default="GBP", help="The currency to convert to.")

    args = parser.parse_args()

    c = CurrencyConverter(ECB_URL)
    if args.convert_from not in c.currencies:
        raise ValueError(f"'{args.convert_from}' is not a valid currency.")

    if args.convert_to not in c.currencies:
        raise ValueError(f"'{args.convert_to}' is not a valid currency.")

    print_args(args)

    after_profit_split = args.amount * args.split
    print(f"After split: {after_profit_split}")

    if args.convert_from != args.convert_to:
        final = c.convert(after_profit_split, args.convert_from, args.convert_to)
    else:
        final = after_profit_split

    final = round(final, 2)
    print(f"Payout: {final}")


if __name__ == "__main__":
    main()

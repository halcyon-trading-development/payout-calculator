# Payout Calculator

Calculate your final take-home amount for prop firm withdrawals.

## Usage

```
pip install .
payout-calc -a 4000 -s 80 -f USD -t GBP
# or...
payout-calc --amount 4000 --split 80 --convert-from USD --convert-to GBP

Amount: 4000
Profit split: 80
Convert from: USD
Convert to: GBP
Payout: 2522.51
```

Help can be found by running: `payout-calc -h`.

## Development

The package manager `uv` is recommended.

```
brew install uv
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
pre-commit install
```

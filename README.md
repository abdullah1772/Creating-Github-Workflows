# Creating-Github-Workflows
# Wallet Balance Management System

This project contains a simple Python implementation of a Wallet Balance Management System. The `Wallet` class allows you to manage a wallet's balance by providing functionality to set, get, and remove balance.

## Files in this Repository

1. `wallet.py`: Contains the `Wallet` class that manages a wallet's balance.
2. `test.py`: Contains the unit tests for the `Wallet` class.
3. `.github/workflows/update.yaml`: GitHub Actions workflow for running the unit tests upon every push to the repository.

## Usage

Create an instance of the `Wallet` class and call its methods to manage the wallet's balance.

```python
from wallet import Wallet

# Initialize wallet with balance 0
wallet = Wallet(0)

# Set balance
wallet.set_balance(20)

# Get balance
print(wallet.get_balance())  # Outputs: 20

# Remove balance
wallet.remove_balance(10)
print(wallet.get_balance())  # Outputs: 10
```

## Running Tests

This repository uses `pytest` for unit testing. Tests are defined in `test.py`.

To run tests locally, first install `pytest` using pip:

```bash
pip install pytest
```

Then run the tests with the `pytest` command:

```bash
pytest test.py
```

## Continuous Integration

This repository uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/update.yaml`. The workflow runs the unit tests every time a new commit is pushed to the repository.

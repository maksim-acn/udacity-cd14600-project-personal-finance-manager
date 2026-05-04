# Personal Finance Manager — Design Patterns Project

This project is a hands-on exercise in applying Object-Oriented Design Patterns to build a simplified personal finance manager.
You will implement and extend starter code to add functionality such as tracking transactions, adapting external data, observing balance changes, and ensuring proper architectural patterns.

## Getting Started

### Dependencies

Make sure you have python version >= 3.10.x installed on your computer. 


### Installation

1. Clone the repo:

```
bash
git clone https://github.com/udacity/cd14600-project-starter.git
cd cd14600-project-starter/starter
```

2. Run the Program: 
```
python main.py
```

## Testing

This project uses Python’s built-in unittest framework.

To run all tests:

```
python -m unittest discover
```

To run a single test file:
```
python -m unittest balance/test_balance_observer.py
```

### Break Down Tests

- test_balance.py → Verifies correct implementation of the Singleton Balance class.
- test_transaction.py → Confirms transactions update balances correctly.
- test_transaction_adapter.py → Ensures external income data is correctly adapted into Transaction objects.
- test_balance_observer.py → Validates that low-balance alerts are triggered at the correct threshold.

## Project Instructions

1. Implement Singleton Balance Class – Ensure only one balance object exists throughout the app.
2. Complete Transaction Class – Handle income and expense transactions.
3. Implement Adapter Pattern – Adapt external freelance income data into internal Transaction objects.
4. Implement Observer Pattern – Create a low balance observer that triggers an alert when funds drop too low.
5. Add Unit Tests – Write tests for all implemented functionality.
6. Choose and Implement a Fourth Pattern – Pick one additional design pattern (e.g., Strategy, Command, Decorator, etc.) and integrate it into your project.
7. Provide a Reflection – Add a short write-up in your repo (README or separate file) explaining your design choices.

## Design Pattern Reflection

This implementation uses four object-oriented design patterns to keep the finance manager small, testable, and easy to extend.

The `Balance` class uses the Singleton pattern so all parts of the application share one source of truth for the current balance. This fits the project because a personal finance manager should not accidentally maintain competing balances. The trade-off is that singleton state must be reset carefully in tests.

The `TransactionAdapter` uses the Adapter pattern to convert `ExternalFreelanceIncome` objects into standard `Transaction` objects. This keeps third-party data shape separate from the internal transaction model, making it easier to support more external income sources later without changing balance logic.

The balance observers use the Observer pattern. `PrintObserver` reports each balance update, while `LowBalanceAlertObserver` watches for threshold crossings and alerts when the balance becomes too low. This keeps notification behavior outside the `Balance` class, though it means tests need to verify both state changes and notification side effects.

The fourth pattern is Command. `TransactionCommand` wraps applying and undoing one transaction, and `TransactionCommandManager` keeps a small history of executed commands. This makes undo behavior explicit and testable. The current version intentionally keeps the command history in memory only; persistence and redo support would be natural future extensions.

## Built With

* [Python](https://www.python.org/) – Main programming language
* [unittest](https://docs.python.org/3/library/unittest.html) – Testing framework
* [PEP8](https://peps.python.org/pep-0008/) – Style guide for Python code

## License

[License](LICENSE.txt)

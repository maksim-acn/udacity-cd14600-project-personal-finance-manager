# Personal Finance Manager Rubric Completion Plan

## Summary
Complete the Udacity design-patterns project in the existing `starter` app, using the required Singleton, Adapter, and Observer patterns plus Command as the fourth pattern.

## Key Changes
- Make `starter/balance` and `starter/transaction` importable packages by adding `__init__.py` files so `unittest` discovery works cleanly.
- Complete `Balance` as a real Singleton with balance mutation, transaction application, observer registration, observer removal, and notification.
- Complete `Transaction` with enum-backed category behavior, stable string output, and equality by amount/category.
- Complete `TransactionAdapter` so external freelance income converts to an internal income `Transaction`.
- Complete Observer behavior with printed balance updates and low-balance threshold alerts.
- Add the Command pattern with transaction command objects and a small history manager for apply/undo.
- Update `starter/main.py` to demonstrate singleton setup, observers, standard transactions, adapted freelance income, command-based application, undo, and final summary.
- Add reflection documentation explaining Singleton, Adapter, Observer, and Command with trade-offs.

## Tests
- Run tests from `starter` with standard library `unittest`.
- Cover Singleton identity/reset, income/expense handling, invalid categories, transaction formatting/equality, adapter conversion, observer notifications, low-balance alert reset, and command apply/undo/history behavior.
- Acceptance command: `python3 -m unittest discover -s . -p "test*.py"` from `starter`.
- Demo acceptance command: `python3 main.py` from `starter`.

## Assumptions
- Use only Python standard library, compatible with Python 3.8+.
- Keep implementation inside the existing `starter` structure.
- Use Command as the fourth pattern because it directly enhances transaction processing and matches the rubric suggestion.
- Treat generated `__pycache__` directories as incidental local artifacts that should not be committed.

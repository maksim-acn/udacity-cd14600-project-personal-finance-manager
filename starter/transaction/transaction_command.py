from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TransactionCommand:
    """Command object that applies and undoes one transaction."""

    def __init__(self, balance, transaction: Transaction):
        self.balance = balance
        self.transaction = transaction
        self.executed = False

    def execute(self):
        """Apply the transaction to the balance."""
        self.balance.apply_transaction(self.transaction)
        self.executed = True

    def undo(self):
        """Reverse a previously applied transaction."""
        if not self.executed:
            raise RuntimeError("Cannot undo a transaction that was not executed.")

        if self.transaction.category == TransactionCategory.INCOME:
            inverse = Transaction(self.transaction.amount, TransactionCategory.EXPENSE)
        elif self.transaction.category == TransactionCategory.EXPENSE:
            inverse = Transaction(self.transaction.amount, TransactionCategory.INCOME)
        else:
            raise ValueError("Unsupported transaction category.")

        self.balance.apply_transaction(inverse)
        self.executed = False


class TransactionCommandManager:
    """Keeps a history of executed transaction commands."""

    def __init__(self):
        self._history = []

    def execute(self, command):
        """Execute a command and store it for possible undo."""
        command.execute()
        self._history.append(command)

    def undo_last(self):
        """Undo the most recent command."""
        if not self._history:
            raise RuntimeError("No transactions to undo.")

        command = self._history.pop()
        command.undo()

    def history_count(self):
        """Return the number of commands available to undo."""
        return len(self._history)

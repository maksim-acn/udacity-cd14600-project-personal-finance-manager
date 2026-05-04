# balance.py

from transaction.transaction_category import TransactionCategory


class Balance:
    """Singleton to track the balance."""

    _instance = None

    def __new__(cls):
        """Create or return the single Balance instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Return the single Balance instance used by the application."""
        return cls()

    def __init__(self):
        """Initialize the balance. Prevent direct instantiation."""
        if getattr(self, "_initialized", False):
            return
        self._net_balance = 0.0
        self._observers = []
        self._initialized = True

    def reset(self):
        """Reset the net balance to zero."""
        self._net_balance = 0.0
        self._observers = []

    def add_income(self, amount):
        """Add income to the balance."""
        self._net_balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._net_balance -= amount

    def register_observer(self, observer):
        """Register an observer for balance changes."""
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """Remove a previously registered observer."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, transaction):
        """Notify all observers after a transaction is applied."""
        for observer in self._observers:
            observer.update(self, transaction)

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError("Unsupported transaction category.")

        self.notify_observers(transaction)

    def get_balance(self):
        """Get the current net balance."""
        return self._net_balance

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Current balance: ${self._net_balance:.2f}"

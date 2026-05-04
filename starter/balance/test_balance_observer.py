import unittest
from contextlib import redirect_stdout
from io import StringIO
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintBalance
from balance.balance_observer import PrintBalanace
from balance.balance_observer import PrintObserver

class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        self.balance.apply_transaction(Transaction(100, TransactionCategory.INCOME))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(Transaction(60, TransactionCategory.EXPENSE))
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(Transaction(100, TransactionCategory.INCOME))
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(Transaction(60, TransactionCategory.EXPENSE))
        self.assertFalse(observer.alert_triggered)
        
        self.balance.apply_transaction(Transaction(60, TransactionCategory.EXPENSE))
        self.assertTrue(observer.alert_triggered)

    def test_print_observer_prints_balance_change(self):
        observer = PrintObserver()
        self.balance.register_observer(observer)

        output = StringIO()
        with redirect_stdout(output):
            self.balance.apply_transaction(Transaction(25, TransactionCategory.INCOME))

        self.assertIn("Applied Transaction($25", output.getvalue())
        self.assertIn("Current balance: $25.00", output.getvalue())

    def test_print_balance_aliases_are_available(self):
        self.assertTrue(issubclass(PrintBalance, PrintObserver))
        self.assertTrue(issubclass(PrintBalanace, PrintBalance))

    def test_remove_observer_stops_notifications(self):
        observer = PrintObserver()
        self.balance.register_observer(observer)
        self.balance.remove_observer(observer)

        output = StringIO()
        with redirect_stdout(output):
            self.balance.apply_transaction(Transaction(25, TransactionCategory.INCOME))

        self.assertEqual(output.getvalue(), "")

if __name__ == "__main__":
    unittest.main()

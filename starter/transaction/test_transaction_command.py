import unittest

from balance.balance import Balance
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_command import TransactionCommand
from transaction.transaction_command import TransactionCommandManager


class TestTransactionCommand(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_command_executes_transaction(self):
        command = TransactionCommand(
            self.balance,
            Transaction(100, TransactionCategory.INCOME),
        )
        command.execute()

        self.assertTrue(command.executed)
        self.assertEqual(self.balance.get_balance(), 100)

    def test_command_undo_reverses_income(self):
        command = TransactionCommand(
            self.balance,
            Transaction(100, TransactionCategory.INCOME),
        )
        command.execute()
        command.undo()

        self.assertFalse(command.executed)
        self.assertEqual(self.balance.get_balance(), 0)

    def test_command_undo_reverses_expense(self):
        command = TransactionCommand(
            self.balance,
            Transaction(40, TransactionCategory.EXPENSE),
        )
        command.execute()
        command.undo()

        self.assertEqual(self.balance.get_balance(), 0)

    def test_command_manager_tracks_history_and_undoes_last(self):
        manager = TransactionCommandManager()
        manager.execute(
            TransactionCommand(
                self.balance,
                Transaction(100, TransactionCategory.INCOME),
            )
        )
        manager.execute(
            TransactionCommand(
                self.balance,
                Transaction(30, TransactionCategory.EXPENSE),
            )
        )

        self.assertEqual(manager.history_count(), 2)
        self.assertEqual(self.balance.get_balance(), 70)

        manager.undo_last()

        self.assertEqual(manager.history_count(), 1)
        self.assertEqual(self.balance.get_balance(), 100)

    def test_undo_without_execute_raises_error(self):
        command = TransactionCommand(
            self.balance,
            Transaction(25, TransactionCategory.INCOME),
        )

        with self.assertRaises(RuntimeError):
            command.undo()

    def test_manager_undo_without_history_raises_error(self):
        manager = TransactionCommandManager()

        with self.assertRaises(RuntimeError):
            manager.undo_last()


if __name__ == "__main__":
    unittest.main()

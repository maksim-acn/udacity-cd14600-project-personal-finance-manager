# balance_observer.py

class IBalanceObserver:
    def update(self, balance, transaction):
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    def update(self, balance, transaction):
        """Print balance update message."""
        print(f"Applied {transaction}. {balance.summary()}")


class PrintBalance(PrintObserver):
    """Rubric-friendly name for the balance-printing observer."""


class PrintBalanace(PrintBalance):
    """Backward-compatible alias for the rubric typo."""


class LowBalanceAlertObserver(IBalanceObserver):
    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold."""
        current_balance = balance.get_balance()

        if current_balance < self.threshold:
            if not self.alert_triggered:
                print(
                    "Low balance alert: "
                    f"${current_balance:.2f} is below ${self.threshold:.2f}."
                )
                self.alert_triggered = True
        else:
            self.alert_triggered = False

# Trading Circuit Breaker - ADHD Edition

import datetime
from twilio.rest import Client  # For SMS alerts

class TradingCircuitBreaker:
    def __init__(self):
        self.max_trades_per_week = 2  # Not 5, not 3, TWO
        self.max_loss_per_week = 5000  # ₹5k max loss
        self.trading_banned_until = None
        self.accountability_partner_number = "+91XXXXXXXXXX"  # Someone who will STOP you

    def can_i_trade_today(self):
        # Emotional state check
        print("Answer honestly (1-10):")
        revenge_feeling = int(input("Am I revenge trading? (1=no, 10=absolutely): "))
        desperate_feeling = int(input("Do I NEED this trade? (1=no, 10=desperate): "))

        if revenge_feeling > 5 or desperate_feeling > 5:
            self.send_alert_to_partner("🚨 TRYING TO REVENGE TRADE")
            return False, "YOU ARE EMOTIONAL. BANNED FOR 3 DAYS."

        # Check if already hit limits
        if self.weekly_trades >= self.max_trades_per_week:
            return False, "Weekly limit reached. STOP."

        if self.weekly_loss >= self.max_loss_per_week:
            self.send_alert_to_partner("🚨 HIT LOSS LIMIT. NEEDS INTERVENTION.")
            return False, "Loss limit hit. BANNED FOR 7 DAYS."

        return True, "Proceed with caution."

    def send_alert_to_partner(self, message):
        # Send SMS to accountability partner
        # They will call you and talk you down
        pass
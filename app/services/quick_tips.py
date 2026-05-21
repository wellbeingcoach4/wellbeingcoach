import random

class QuickTips:

    tips = [
        "Drink water.",
        "Take a short walk.",
        "Practice deep breathing.",
        "Listen to calming music."
    ]

    @staticmethod
    def get_tip():
        return random.choice(QuickTips.tips)
import random


class QuickTips:

    tips = [
        "Drink a glass of water.",
        "Take 5 deep breaths.",
        "Stretch your shoulders and neck.",
        "Step outside for fresh air.",
        "Listen to calming music for 2 minutes.",
        "Write down one positive thought.",
        "Close your eyes and relax your muscles.",
        "Take a short mindful walk."
    ]

    @staticmethod
    def get_tip():

        return random.choice(
            QuickTips.tips
        )
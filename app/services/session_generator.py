class SessionGenerator:

    @staticmethod
    def generate(mood: str):

        sessions = {
            "sad": "Take 5 deep breaths and write one positive thought.",
            "anxious": "Close your eyes and focus on breathing slowly.",
            "neutral": "Stretch your body and drink water."
        }

        return sessions.get(
            mood,
            "Take a short mindful break."
        )
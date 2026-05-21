class MoodClassifier:

    @staticmethod
    def analyze(text: str):

        text = text.lower()

        if "sad" in text:
            return {
                "mood": "sad",
                "confidence": 0.91
            }

        if "anxious" in text:
            return {
                "mood": "anxious",
                "confidence": 0.88
            }

        return {
            "mood": "neutral",
            "confidence": 0.75
        }
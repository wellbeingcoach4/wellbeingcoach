from datetime import datetime


class BehavioralMemory:

    @staticmethod
    def detect_time_of_day():

        hour = datetime.now().hour

        if 5 <= hour < 12:
            return "morning"

        elif 12 <= hour < 17:
            return "afternoon"

        elif 17 <= hour < 21:
            return "evening"

        return "night"

    @staticmethod
    def detect_stressor(text: str):

        text = text.lower()

        stressors = {
            "work": ["meeting", "deadline", "office"],
            "relationships": ["partner", "family", "friend"],
            "health": ["sick", "pain", "tired"],
            "finance": ["money", "bills", "debt"]
        }

        for category, keywords in stressors.items():

            for keyword in keywords:

                if keyword in text:
                    return category

        return "unknown"
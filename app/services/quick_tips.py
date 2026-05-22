import random
from app.core.config import settings
from app.llm.cloud_service import GeminiService
from app.llm.local_service import OllamaService


class QuickTips:

    TIPS = {

        "anxious": [
            {
                "category": "calming",
                "tip": "Try box breathing for 60 seconds.",
                "duration": "1 minute",
                "difficulty": "easy"
            },
            {
                "category": "mindfulness",
                "tip": "Close your eyes and focus only on your breathing.",
                "duration": "2 minutes",
                "difficulty": "easy"
            }
        ],

        "sad": [
            {
                "category": "uplifting",
                "tip": "Write down one thing you're grateful for.",
                "duration": "2 minutes",
                "difficulty": "easy"
            },
            {
                "category": "movement",
                "tip": "Take a short walk outside.",
                "duration": "5 minutes",
                "difficulty": "medium"
            }
        ],

        "stressed": [
            {
                "category": "relaxation",
                "tip": "Relax your shoulders and jaw consciously.",
                "duration": "1 minute",
                "difficulty": "easy"
            }
        ],

        "neutral": [
            {
                "category": "wellness",
                "tip": "Drink a glass of water slowly.",
                "duration": "1 minute",
                "difficulty": "easy"
            }
        ]
    }

    # @staticmethod
    # def get_tip(mood: str):

    #     mood = mood.lower()

    #     tips = QuickTips.TIPS.get(
    #         mood,
    #         QuickTips.TIPS[mood] if mood in QuickTips.TIPS else QuickTips.TIPS["neutral"]
    #     )

    #     return random.choice(tips)
    
    @staticmethod
    def get_tip(mood: str):

        provider = settings.LLM_PROVIDER.lower()

        if provider == "gemini":

            service = GeminiService()

            tip = service.generate_tip(mood)

        else:

            service = OllamaService()

            tip = service.generate_tip(mood)

        return {
            "mood": mood,
            "category": QuickTips.get_category(mood),
            "tip": tip
        }

    @staticmethod
    def get_category(mood: str):
        categories = {
            "anxious": "calming",
            "sad": "uplifting",
            "stressed": "relaxation",
            "neutral": "wellness"
        }

        return categories.get(mood.lower(), "general")

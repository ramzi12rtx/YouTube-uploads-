import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # إعدادات OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # إعدادات توليد الصور
    IMAGE_STYLE = "digital art"
    IMAGE_SIZE = "1024x1024"
    
    # مواضيع الفيديوهات
    VIDEO_TOPICS = [
        "تأثير الذكاء الاصطناعي على التعليم",
        "أحدث تطورات التكنولوجيا الطبية",
        "مستقبل السيارات الكهربائية",
        "نصائح لريادة الأعمال الناجحة"
    ]
    
    # إعدادات الفيديو
    VIDEO_RESOLUTION = (1080, 1920)  # دقة الـ Shorts
    VIDEO_FPS = 30

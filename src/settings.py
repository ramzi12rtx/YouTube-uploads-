import os
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()

class Settings:
    # إعدادات OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # إعدادات توليد الصور
    IMAGE_STYLE = "digital art"
    IMAGE_SIZE = "1024x1024"
    IMAGE_OUTPUT_DIR = "outputs/images"
    
    # إعدادات الصوت
    AUDIO_OUTPUT_DIR = "outputs/audio"
    
    # إعدادات الفيديو
    VIDEO_RESOLUTION = (1080, 1920)  # دقة الـ Shorts
    VIDEO_FPS = 30
    VIDEO_OUTPUT_DIR = "outputs/videos"
    
    # مواضيع الفيديوهات
    VIDEO_TOPICS = [
        "تأثير الذكاء الاصطناعي على التعليم",
        "أحدث تطورات التكنولوجيا الطبية",
        "مستقبل السيارات الكهربائية",
        "نصائح لريادة الأعمال الناجحة"
    ]
    
    # إعدادات التوليد التلقائي
    DAILY_GENERATION_COUNT = 3  # عدد الفيديوهات التي يتم توليدها يومياً

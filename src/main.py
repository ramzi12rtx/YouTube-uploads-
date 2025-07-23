import os
from video_generator import generate_video
from audio_generator import text_to_speech
from image_generator import generate_images
from config import settings
import openai

def generate_script(topic):
    """توليد نص الفيديو باستخدام الذكاء الاصطناعي"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "أنت كاتب محترف لمقاطع يوتيوب قصيرة. اكتب نصًا جذابًا لمدة 60 ثانية."},
            {"role": "user", "content": f"اكتب نص فيديو عن: {topic}"}
        ]
    )
    return response.choices[0].message['content']

def main():
    # الحصول على مواضيع من البيئة أو ملف إعدادات
    topics = settings.VIDEO_TOPICS
    
    for topic in topics:
        try:
            print(f"جاري إنشاء فيديو عن: {topic}")
            
            # توليد النص
            script = generate_script(topic)
            print(f"تم توليد النص: {script[:50]}...")
            
            # توليد الصوت
            audio_path = text_to_speech(script, "ar")
            
            # توليد الصور
            image_paths = generate_images(script, count=5)
            
            # توليد الفيديو
            output_path = os.path.join("outputs", f"{topic.replace(' ', '_')}.mp4")
            generate_video(image_paths, audio_path, output_path)
            
            print(f"تم إنشاء الفيديو: {output_path}")
            
        except Exception as e:
            print(f"خطأ في إنشاء فيديو عن {topic}: {str(e)}")

if __name__ == "__main__":
    main()

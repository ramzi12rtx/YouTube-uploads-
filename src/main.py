from audio_generator import text_to_speech, generate_script
from video_generator import generate_video
from image_generator import generate_images
from utils import create_output_dirs
import os

def main():
    create_output_dirs()
    
    topics = [
        "تأثير الذكاء الاصطناعي على التعليم",
        "أحدث تطورات التكنولوجيا الطبية"
    ]
    
    for topic in topics:
        try:
            print(f"جارٍ إنشاء فيديو عن: {topic}")
            script = generate_script(topic)
            audio_path = text_to_speech(script, "ar")
            image_paths = generate_images(topic, count=3)
            output_path = os.path.join("outputs", f"{topic.replace(' ', '_')}.mp4")
            generate_video(image_paths, audio_path, output_path)
            print(f"تم إنشاء الفيديو: {output_path}")
        except Exception as e:
            print(f"خطأ: {str(e)}")

if __name__ == "__main__":
    main()

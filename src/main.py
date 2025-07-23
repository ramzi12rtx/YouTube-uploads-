import os
from src.audio_generator import text_to_speech, generate_script
from src.image_generator import generate_images
from src.video_generator import generate_video
from src.utils import create_output_dirs, get_timestamp
from config.settings import Settings

def main():
    create_output_dirs()
    
    for topic in Settings.VIDEO_TOPICS:
        try:
            print(f"جاري إنشاء فيديو عن: {topic}")
            
            # توليد النص
            script = generate_script(topic)
            print(f"تم توليد النص: {script[:50]}...")
            
            # توليد الصوت
            audio_path = text_to_speech(script, "ar")
            print(f"تم توليد الصوت: {audio_path}")
            
            # توليد الصور
            image_paths = generate_images(topic, count=5)
            print(f"تم توليد {len(image_paths)} صور")
            
            # توليد الفيديو
            timestamp = get_timestamp()
            output_path = os.path.join(Settings.VIDEO_OUTPUT_DIR, f"{topic.replace(' ', '_')}_{timestamp}.mp4")
            video_path = generate_video(image_paths, audio_path, output_path)
            print(f"تم إنشاء الفيديو: {video_path}")
            
        except Exception as e:
            print(f"خطأ في إنشاء فيديو عن {topic}: {str(e)}")

if __name__ == "__main__":
    main()

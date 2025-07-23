import os
import shutil
import datetime

def clean_directory(directory):
    """ينظف مجلد عن طريق حذف جميع محتوياته"""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"فشل في حذف {file_path}: {e}")

def create_output_dirs():
    """ينشئ مجلدات المخرجات إذا لم تكن موجودة"""
    dirs = [
        Settings.IMAGE_OUTPUT_DIR,
        Settings.AUDIO_OUTPUT_DIR,
        Settings.VIDEO_OUTPUT_DIR
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        # تنظيف المجلد في بداية كل عملية
        clean_directory(dir_path)

def get_timestamp():
    """يعيد طابع زمني للاستخدام في أسماء الملفات"""
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

import openai
import requests
import os
from PIL import Image
from io import BytesIO
from config.settings import Settings

def generate_images(prompt, count=5):
    """
    يولد صورًا باستخدام DALL-E بناءً على النص
    """
    openai.api_key = Settings.OPENAI_API_KEY
    
    # إنشاء مجلد المخرجات إذا لم يكن موجوداً
    os.makedirs(Settings.IMAGE_OUTPUT_DIR, exist_ok=True)
    
    image_paths = []
    
    for i in range(count):
        try:
            # طلب توليد الصورة من DALL-E
            response = openai.images.generate(
                model="dall-e-3",
                prompt=f"{prompt} - Style: {Settings.IMAGE_STYLE}",
                size=Settings.IMAGE_SIZE,
                n=1,
                quality="standard"
            )
            
            # تحميل الصورة من الرابط
            image_url = response.data[0].url
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            
            # حفظ الصورة
            filename = f"image_{i+1}.png"
            image_path = os.path.join(Settings.IMAGE_OUTPUT_DIR, filename)
            image.save(image_path)
            image_paths.append(image_path)
            
        except Exception as e:
            print(f"خطأ في توليد الصورة: {str(e)}")
            continue
    
    return image_paths

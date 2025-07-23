from gtts import gTTS
import os
from config.settings import Settings
import openai

def text_to_speech(text, lang='ar'):
    """
    يحول النص إلى كلام باستخدام gTTS
    """
    # إنشاء مجلد المخرجات إذا لم يكن موجوداً
    os.makedirs(Settings.AUDIO_OUTPUT_DIR, exist_ok=True)
    
    # إنشاء اسم ملف فريد
    filename = f"audio_{hash(text)}.mp3"
    output_path = os.path.join(Settings.AUDIO_OUTPUT_DIR, filename)
    
    # توليد الصوت
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_path)
    
    return output_path

def generate_script(topic):
    """
    يولد نص فيديو باستخدام GPT
    """
    openai.api_key = Settings.OPENAI_API_KEY
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "أنت كاتب محترف لمقاطع يوتيوب قصيرة. اكتب نصًا جذابًا لمدة 60 ثانية."
            },
            {
                "role": "user",
                "content": f"اكتب نص فيديو عن: {topic}"
            }
        ],
        max_tokens=500,
        temperature=0.7
    )
    
    return response.choices[0].message['content']

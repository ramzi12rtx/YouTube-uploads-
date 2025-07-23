from moviepy.editor import *
from moviepy.video.fx.all import resize
import os
import random
from config.settings import Settings

def generate_video(image_paths, audio_path, output_path):
    """
    يدمج الصور والصوت لإنشاء فيديو نهائي
    """
    # تحميل الصوت
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    
    # إنشاء مقاطع الصور
    clips = []
    for img_path in image_paths:
        # إنشاء مقطع صورة مع مدة عشوائية بين 3-7 ثواني
        duration = random.uniform(3, 7)
        clip = ImageClip(img_path).set_duration(duration)
        clips.append(clip)
    
    # دمج جميع مقاطع الصور
    video_clip = concatenate_videoclips(clips)
    
    # تعديل طول الفيديو ليتناسب مع طول الصوت
    if video_clip.duration > audio_duration:
        video_clip = video_clip.subclip(0, audio_duration)
    else:
        # إضافة صورة خلفية إذا كان الفيديو أقصر من الصوت
        extra_duration = audio_duration - video_clip.duration
        last_clip = ImageClip(image_paths[-1]).set_duration(extra_duration)
        video_clip = concatenate_videoclips([video_clip, last_clip])
    
    # تغيير حجم الفيديو لدقة الـ YouTube Shorts
    video_clip = resize(video_clip, newsize=Settings.VIDEO_RESOLUTION)
    
    # إضافة الصوت
    final_clip = video_clip.set_audio(audio_clip)
    
    # كتابة الفيديو النهائي
    final_clip.write_videofile(
        output_path,
        codec='libx264',
        audio_codec='aac',
        fps=Settings.VIDEO_FPS
    )
    
    # إغلاق المقاطع لتجنب مشاكل الذاكرة
    video_clip.close()
    audio_clip.close()
    final_clip.close()
    
    return output_path

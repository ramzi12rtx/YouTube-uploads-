import os

def create_output_dirs():
    """ينشئ مجلدات المخرجات"""
    os.makedirs("outputs/images", exist_ok=True)
    os.makedirs("outputs/audio", exist_ok=True)
    os.makedirs("outputs/videos", exist_ok=True)

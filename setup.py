from setuptools import setup, find_packages

setup(
    name="yt_shorts_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'moviepy',
        'gtts',
        'requests',
        'Pillow'
    ],
)

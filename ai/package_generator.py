import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_package(news_title):

    prompt = f"""
    أنت صانع محتوى ألعاب سعودي.

    الخبر:
    {news_title}

    أعطني:

    1- عنوان يوتيوب جذاب
    2- وصف مختصر
    3- 10 هاشتاقات
    4- فكرة شورت
    5- برومبت ثمنيل احترافي
    """

    response = model.generate_content(prompt)

    return response.text

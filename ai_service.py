import os
import google.generativeai as genai

SYSTEM_PROMPT = """أنت مساعد أكاديمي ذكي متخصص حصراً في التوجيه المهني لطلاب تقنية المعلومات والحاسوب.
مهمتك:
- الإجابة على أسئلة التخصصات التقنية (برمجة، ذكاء اصطناعي، أمن سيبراني، إلخ)
- مساعدة الطلاب في اختيار مساراتهم المهنية
- شرح المفاهيم التقنية بشكل مبسط
- تقديم نصائح للتعلم والتطوير المهني

قواعد صارمة:
- لا تجيب على أي سؤال خارج نطاق التقنية والتوجيه الأكاديمي
- إذا سألك المستخدم عن موضوع غير تقني، قل: "أنا متخصص فقط في التوجيه الأكاديمي التقني"
- أجب دائماً باللغة العربية
- اجعل إجاباتك مختصرة وعملية"""


class GeminiService:
    def __init__(self):
        self.model = None
        self.chat  = None
        self.available = False
        self._init_model()

    def _load_api_key(self):
        # أولاً: من متغيرات البيئة
        key = os.environ.get("GEMINI_API_KEY", "")
        if key and key != "YOUR_API_KEY_HERE":
            return key
        # ثانياً: من ملف .env يدوياً
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("GEMINI_API_KEY="):
                        val = line.split("=", 1)[1].strip()
                        if val and val != "YOUR_API_KEY_HERE":
                            return val
        return None

    def _init_model(self):
        try:
            key = self._load_api_key()
            if not key:
                return
            genai.configure(api_key=key)
            self.model = genai.GenerativeModel(
                model_name="gemini-flash-latest",
                system_instruction=SYSTEM_PROMPT
            )
            self.chat = self.model.start_chat(history=[])
            self.available = True
        except Exception:
            self.available = False

    def ask(self, question):
        if not self.available:
            return None
        try:
            response = self.chat.send_message(question)
            return response.text
        except Exception as e:
            return f"⚠️ خطأ في الاتصال: {e}"

    def is_available(self):
        return self.available

import json
import os

class AcademicInferenceEngine:
    def __init__(self):
        self.knowledge_base = {
            "خبير ذكاء اصطناعي": {
                "skills": ["برمجة", "رياضيات", "بيانات", "إحصاء", "تعلم الآلة"],
                "roadmap": ["أساسيات بايثون", "الجبر الخطي والإحصاء", "تعلم الآلة", "الشبكات العصبية العميقة", "مشاريع تطبيقية"],
                "cost": 90,
                "emoji": "🤖",
                "desc": "تصميم وبناء أنظمة ذكاء اصطناعي وتعلم آلة",
                "duration": "3-4 سنوات",
                "salary": "8,000 - 20,000 ريال"
            },
            "مهندس أمن سيبراني": {
                "skills": ["شبكات", "تشفير", "لينكس", "برمجة", "اختبار اختراق"],
                "roadmap": ["أساسيات الشبكات", "نظام لينكس", "تشفير البيانات", "اختبار الاختراق", "الاستجابة للحوادث"],
                "cost": 75,
                "emoji": "🔐",
                "desc": "حماية الأنظمة والشبكات من الهجمات الإلكترونية",
                "duration": "2-3 سنوات",
                "salary": "7,000 - 18,000 ريال"
            },
            "محلل بيانات ضخمة": {
                "skills": ["إحصاء", "قواعد بيانات", "رياضيات", "برمجة", "تحليل"],
                "roadmap": ["لغة Python أو R", "SQL وقواعد البيانات", "تحليل إحصائي", "تصوير البيانات", "تكنولوجيا Big Data"],
                "cost": 65,
                "emoji": "📊",
                "desc": "تحليل واستخراج الأنماط من البيانات الضخمة",
                "duration": "2-3 سنوات",
                "salary": "6,000 - 15,000 ريال"
            },
            "مطور تطبيقات موبايل": {
                "skills": ["برمجة", "تصميم", "جافا", "سويفت", "واجهات مستخدم"],
                "roadmap": ["أساسيات البرمجة", "Flutter أو React Native", "تصميم UI/UX", "قواعد البيانات المحلية", "نشر التطبيقات"],
                "cost": 60,
                "emoji": "📱",
                "desc": "بناء تطبيقات الهاتف الذكي لنظامي iOS وAndroid",
                "duration": "1-2 سنة",
                "salary": "5,000 - 14,000 ريال"
            },
            "مهندس حوسبة سحابية": {
                "skills": ["شبكات", "برمجة", "لينكس", "قواعد بيانات", "DevOps"],
                "roadmap": ["أساسيات الشبكات", "خدمات AWS أو Azure", "Docker وKubernetes", "CI/CD Pipeline", "أمن السحابة"],
                "cost": 80,
                "emoji": "☁️",
                "desc": "تصميم وإدارة البنية التحتية السحابية",
                "duration": "2-3 سنوات",
                "salary": "8,000 - 22,000 ريال"
            },
            "مصمم UX/UI": {
                "skills": ["تصميم", "إبداع", "واجهات مستخدم", "فوتوشوب", "تجربة مستخدم"],
                "roadmap": ["مبادئ التصميم", "Figma وAdobe XD", "أبحاث المستخدم", "النماذج الأولية", "اختبار قابلية الاستخدام"],
                "cost": 50,
                "emoji": "🎨",
                "desc": "تصميم تجارب وواجهات مستخدم جذابة وسهلة الاستخدام",
                "duration": "1-2 سنة",
                "salary": "5,000 - 12,000 ريال"
            },
            "مطور ويب متكامل": {
                "skills": ["برمجة", "HTML", "CSS", "جافاسكريبت", "قواعد بيانات"],
                "roadmap": ["HTML وCSS", "JavaScript وReact", "Node.js أو Django", "قواعد البيانات", "نشر المواقع"],
                "cost": 55,
                "emoji": "🌐",
                "desc": "بناء مواقع وتطبيقات ويب من الواجهة للخادم",
                "duration": "1-2 سنة",
                "salary": "5,000 - 13,000 ريال"
            },
            "مهندس روبوتات": {
                "skills": ["رياضيات", "برمجة", "إلكترونيات", "ميكانيكا", "تعلم الآلة"],
                "roadmap": ["الرياضيات والفيزياء", "برمجة C++ وPython", "أنظمة التحكم", "ROS Framework", "مشاريع روبوتية"],
                "cost": 95,
                "emoji": "🦾",
                "desc": "تصميم وبرمجة الروبوتات والأنظمة الآلية",
                "duration": "4-5 سنوات",
                "salary": "9,000 - 25,000 ريال"
            }
        }

        # Graph متفرع لكل تخصص — كل عقدة تحتوي قائمة بالعقد التالية
        self.memory_file = os.path.join(os.path.dirname(__file__), "user_memory.json")
        self.user_memory = self._load_memory()
        self.career_graphs = {
            "خبير ذكاء اصطناعي": {
                "أساسيات بايثون":            ["الجبر الخطي والإحصاء", "مكتبات بايثون العلمية"],
                "الجبر الخطي والإحصاء":      ["تعلم الآلة"],
                "مكتبات بايثون العلمية":     ["تعلم الآلة", "تحليل البيانات"],
                "تعلم الآلة":                ["الشبكات العصبية العميقة"],
                "تحليل البيانات":            ["الشبكات العصبية العميقة"],
                "الشبكات العصبية العميقة":   ["مشاريع تطبيقية"],
                "مشاريع تطبيقية":            [],
            },
            "مهندس أمن سيبراني": {
                "أساسيات الشبكات":           ["نظام لينكس", "بروتوكولات الإنترنت"],
                "نظام لينكس":               ["تشفير البيانات"],
                "بروتوكولات الإنترنت":       ["تشفير البيانات", "أمن الشبكات"],
                "تشفير البيانات":            ["اختبار الاختراق"],
                "أمن الشبكات":              ["اختبار الاختراق"],
                "اختبار الاختراق":           ["الاستجابة للحوادث"],
                "الاستجابة للحوادث":         [],
            },
            "محلل بيانات ضخمة": {
                "لغة Python أو R":           ["SQL وقواعد البيانات", "الإحصاء الوصفي"],
                "SQL وقواعد البيانات":        ["تحليل إحصائي"],
                "الإحصاء الوصفي":            ["تحليل إحصائي", "تصوير البيانات"],
                "تحليل إحصائي":             ["تصوير البيانات"],
                "تصوير البيانات":            ["تكنولوجيا Big Data"],
                "تكنولوجيا Big Data":        [],
            },
            "مطور تطبيقات موبايل": {
                "أساسيات البرمجة":           ["Flutter أو React Native", "Java للأندرويد"],
                "Flutter أو React Native":   ["تصميم UI/UX"],
                "Java للأندرويد":            ["تصميم UI/UX", "قواعد البيانات المحلية"],
                "تصميم UI/UX":              ["قواعد البيانات المحلية"],
                "قواعد البيانات المحلية":    ["نشر التطبيقات"],
                "نشر التطبيقات":             [],
            },
            "مهندس حوسبة سحابية": {
                "أساسيات الشبكات":           ["خدمات AWS أو Azure", "نظام لينكس المتقدم"],
                "خدمات AWS أو Azure":        ["Docker وKubernetes"],
                "نظام لينكس المتقدم":        ["Docker وKubernetes", "CI/CD Pipeline"],
                "Docker وKubernetes":        ["CI/CD Pipeline"],
                "CI/CD Pipeline":            ["أمن السحابة"],
                "أمن السحابة":              [],
            },
            "مصمم UX/UI": {
                "مبادئ التصميم":             ["Figma وAdobe XD", "نظرية الألوان"],
                "Figma وAdobe XD":           ["أبحاث المستخدم"],
                "نظرية الألوان":             ["أبحاث المستخدم", "التصميم التفاعلي"],
                "أبحاث المستخدم":            ["النماذج الأولية"],
                "التصميم التفاعلي":          ["النماذج الأولية"],
                "النماذج الأولية":           ["اختبار قابلية الاستخدام"],
                "اختبار قابلية الاستخدام":   [],
            },
            "مطور ويب متكامل": {
                "HTML وCSS":                 ["JavaScript وReact", "تصميم متجاوب"],
                "JavaScript وReact":         ["Node.js أو Django"],
                "تصميم متجاوب":             ["Node.js أو Django", "قواعد البيانات"],
                "Node.js أو Django":         ["قواعد البيانات"],
                "قواعد البيانات":            ["نشر المواقع"],
                "نشر المواقع":              [],
            },
            "مهندس روبوتات": {
                "الرياضيات والفيزياء":       ["برمجة C++ وPython", "الإلكترونيات التطبيقية"],
                "برمجة C++ وPython":         ["أنظمة التحكم"],
                "الإلكترونيات التطبيقية":    ["أنظمة التحكم", "المستشعرات والمحركات"],
                "أنظمة التحكم":             ["ROS Framework"],
                "المستشعرات والمحركات":      ["ROS Framework"],
                "ROS Framework":             ["مشاريع روبوتية"],
                "مشاريع روبوتية":            [],
            },
        }

        self.skills_aliases = {
            "python": "برمجة", "بايثون": "برمجة", "كود": "برمجة", "coding": "برمجة",
            "math": "رياضيات", "حساب": "رياضيات",
            "data": "بيانات", "داتا": "بيانات",
            "network": "شبكات", "نتورك": "شبكات",
            "linux": "لينكس", "ubuntu": "لينكس",
            "design": "تصميم", "ديزاين": "تصميم",
            "java": "جافا", "swift": "سويفت",
            "statistics": "إحصاء", "احصاء": "إحصاء",
            "database": "قواعد بيانات", "sql": "قواعد بيانات", "db": "قواعد بيانات",
            "html": "HTML", "css": "CSS", "js": "جافاسكريبت", "javascript": "جافاسكريبت",
            "devops": "DevOps", "cloud": "شبكات",
            "security": "تشفير", "hack": "اختبار اختراق", "hacking": "اختبار اختراق",
            "ml": "تعلم الآلة", "ai": "تعلم الآلة", "deep learning": "تعلم الآلة",
            "analysis": "تحليل", "تحليل بيانات": "تحليل",
            "electronics": "إلكترونيات", "الكترونيات": "إلكترونيات",
            "mechanic": "ميكانيكا", "ميكانيك": "ميكانيكا",
            "ux": "تجربة مستخدم", "ui": "واجهات مستخدم", "figma": "تصميم",
            "photoshop": "فوتوشوب", "creative": "إبداع", "إبداعي": "إبداع",
        }

    def normalize_skills(self, skills):
        normalized = []
        for s in skills:
            s_lower = s.strip().lower()
            normalized.append(self.skills_aliases.get(s_lower, s.strip()))
        return normalized

    def forward_chaining(self, user_skills):
        user_skills = self.normalize_skills(user_skills)
        results = []
        for career, data in self.knowledge_base.items():
            matches = set(user_skills) & set(data["skills"])
            if matches:
                confidence = round((len(matches) / len(data["skills"])) * 100, 1)
                results.append((career, confidence, list(matches), data["emoji"], data["desc"], data["salary"]))
        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def backward_chaining(self, target_career):
        target_career = target_career.strip()
        # بحث جزئي
        found_key = None
        for key in self.knowledge_base:
            if target_career in key or key in target_career:
                found_key = key
                break
        if not found_key:
            found_key = target_career if target_career in self.knowledge_base else None

        if found_key:
            data = self.knowledge_base[found_key]
            steps = data["roadmap"]
            numbered = "\n".join([f"  {i+1}. {s}" for i, s in enumerate(steps)])
            skills_needed = "، ".join(data["skills"])
            return (
                f"{data['emoji']} المسار المطلوب لـ ({found_key}):\n\n"
                f"📋 المهارات المطلوبة: {skills_needed}\n\n"
                f"🗺️ خطوات المسار:\n{numbered}\n\n"
                f"⏱️ المدة التقديرية: {data['duration']}\n"
                f"💰 الراتب المتوقع: {data['salary']}"
            )
        # اقتراح أقرب تخصص
        suggestions = "، ".join(list(self.knowledge_base.keys())[:4])
        return f"❌ لم أجد تخصص '{target_career}' في قاعدة المعرفة.\n\n💡 جرب أحد هذه التخصصات:\n{suggestions}"

    def heuristic_analysis(self, target_career):
        found_key = None
        for key in self.knowledge_base:
            if target_career in key or key in target_career:
                found_key = key
                break
        if not found_key:
            found_key = target_career if target_career in self.knowledge_base else None

        if found_key:
            h = self.knowledge_base[found_key]["cost"]
            bar = "█" * (h // 10) + "░" * (10 - h // 10)
            if h >= 85:
                level = "🔴 صعب جداً - يتطلب تفرغاً كاملاً والتزاماً عالياً"
            elif h >= 70:
                level = "🟠 صعب - يحتاج جهداً كبيراً ووقتاً طويلاً"
            elif h >= 55:
                level = "🟡 متوسط - مناسب للدراسة الجانبية مع العمل"
            else:
                level = "🟢 سهل نسبياً - يمكن إتقانه بسرعة"
            return f"📈 مستوى الصعوبة: {h}/100\n[{bar}]\n{level}"
        return None

    def _load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"career_counts": {}, "last_career": None}

    def _save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.user_memory, f, ensure_ascii=False, indent=2)

    def record_interest(self, career_name):
        key = self._find_career_key(career_name)
        if not key:
            return
        counts = self.user_memory["career_counts"]
        counts[key] = counts.get(key, 0) + 1
        self.user_memory["last_career"] = key
        self._save_memory()

    def get_top_career(self):
        counts = self.user_memory["career_counts"]
        if not counts:
            return None
        return max(counts, key=counts.get)

    def get_missing_skills(self, user_skills, career_name):
        key = self._find_career_key(career_name)
        if not key:
            return []
        normalized = set(self.normalize_skills(user_skills))
        required   = set(self.knowledge_base[key]["skills"])
        return list(required - normalized)

    def get_boosted_results(self, results):
        # رفع نسبة الثقة للتخصصات التي بحث عنها المستخدم سابقاً
        counts = self.user_memory["career_counts"]
        if not counts:
            return results
        boosted = []
        for item in results:
            career, conf, matches, emoji, desc, salary = item
            boost = min(counts.get(career, 0) * 5, 20)  # حد أقصى 20%
            boosted.append((career, min(conf + boost, 100), matches, emoji, desc, salary))
        boosted.sort(key=lambda x: x[1], reverse=True)
        return boosted

    def _find_career_key(self, name):
        name = name.strip()
        for key in self.knowledge_base:
            if name in key or key in name:
                return key
        return None

    def build_graph(self, career_name):
        key = self._find_career_key(career_name)
        if not key:
            return None, None
        return self.career_graphs[key], list(self.career_graphs[key].keys())

    def bfs_search(self, career_name, target_step):
        graph, all_nodes = self.build_graph(career_name)
        if not graph:
            return None, []
        start = all_nodes[0]
        target = next((n for n in all_nodes if target_step in n or n in target_step), None)
        if not target:
            return None, all_nodes
        from collections import deque
        queue = deque([[start]])
        visited = set()
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == target:
                return path, all_nodes
            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, []):
                    queue.append(path + [neighbor])
        return None, all_nodes

    def dfs_search(self, career_name, target_step):
        graph, all_nodes = self.build_graph(career_name)
        if not graph:
            return None, []
        start = all_nodes[0]
        target = next((n for n in all_nodes if target_step in n or n in target_step), None)
        if not target:
            return None, all_nodes
        stack = [[start]]
        visited = set()
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == target:
                return path, all_nodes
            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, []):
                    stack.append(path + [neighbor])
        return None, all_nodes

    def get_all_careers(self):
        return [(k, v["emoji"], v["desc"]) for k, v in self.knowledge_base.items()]

    def get_all_skills(self):
        skills = set()
        for data in self.knowledge_base.values():
            skills.update(data["skills"])
        return sorted(skills)

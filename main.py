import customtkinter as ctk
from logic import AcademicInferenceEngine
from ai_service import GeminiService
import threading
import time
import tkinter as tk

ctk.set_appearance_mode("dark")

# ─────────── CONSTANTS ───────────
COLORS = {
    "bg":        "#0F0F0F",
    "sidebar":   "#1A1A1B",
    "card":      "#1E1E1F",
    "accent":    "#1f6aa5",
    "accent2":   "#2980b9",
    "bot_bubble":"#2b2b2b",
    "text":      "#FFFFFF",
    "subtext":   "#AAAAAA",
    "green":     "#27ae60",
    "border":    "#2a2a2a",
}
BASE_FONT_SIZE = 13
FONT_TITLE  = ("Arial", 20, "bold")
FONT_BTN    = ("Arial", 13, "bold")
FONT_LABEL  = ("Arial", 13)
FONT_SMALL  = ("Arial", 11)
FONT_BUBBLE = ("Arial", 13)


class AcademicAIApp(ctk.CTk):
    # ─────────── INIT ───────────
    def __init__(self):
        super().__init__()
        self.title("Academic Path Finder AI - نظام التوجيه الأكاديمي الذكي")
        self.geometry("900x700")
        self.resizable(True, True)
        self.engine = AcademicInferenceEngine()
        self.gemini = GeminiService()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._font_size = BASE_FONT_SIZE

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # PanedWindow — الشريط الجانبي والمحتوى قابلان للسحب
        self.paned = tk.PanedWindow(self, orient=tk.HORIZONTAL,
                                    bg=COLORS["accent"], sashwidth=4,
                                    sashrelief="flat", sashpad=0,
                                    handlesize=0, opaqueresize=True)
        self.paned.grid(row=0, column=0, sticky="nsew")

        self._build_sidebar()
        self._build_main_area()
        self.paned.add(self.sidebar,  minsize=160, width=230)
        self.paned.add(self.main,     minsize=400)
        self._switch_tab("chat")
        self.bind_all("<Control-MouseWheel>", self._on_zoom)

    # ─────────── ZOOM ───────────
    def _on_zoom(self, event):
        if event.delta > 0:
            self._font_size = min(self._font_size + 1, 26)
        else:
            self._font_size = max(self._font_size - 1, 8)
        self._apply_fonts()

    def _apply_fonts(self):
        s = self._font_size
        fonts = {
            "title":  ("Arial", s + 7, "bold"),
            "btn":    ("Arial", s,     "bold"),
            "label":  ("Arial", s),
            "small":  ("Arial", s - 2),
            "bubble": ("Arial", s),
        }
        self._update_widgets(self, fonts)
        scale = s / BASE_FONT_SIZE
        for w in self.chat_scroll.winfo_children():
            if isinstance(w, (ctk.CTkLabel, ctk.CTkTextbox)):
                if isinstance(w, ctk.CTkLabel) and hasattr(w, 'cget'):
                    try:
                        w.configure(wraplength=int(520 * scale))
                    except:
                        pass

    def _update_widgets(self, parent, fonts):
        for w in parent.winfo_children():
            if isinstance(w, ctk.CTkLabel):
                current = w.cget("font")
                if isinstance(current, tuple) and len(current) >= 2:
                    size = current[1]
                    bold = len(current) > 2 and current[2] == "bold"
                    if size >= 18:   w.configure(font=fonts["title"])
                    elif bold:       w.configure(font=fonts["btn"])
                    elif size <= 11: w.configure(font=fonts["small"])
                    else:            w.configure(font=fonts["label"])
            elif isinstance(w, ctk.CTkTextbox):
                w.configure(font=fonts["bubble"])
            elif isinstance(w, (ctk.CTkButton, ctk.CTkOptionMenu, ctk.CTkEntry)):
                w.configure(font=fonts["btn"])
            self._update_widgets(w, fonts)

    # ─────────── SIDEBAR ───────────
    def _build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self.paned, width=230, corner_radius=0, fg_color=COLORS["sidebar"])
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_rowconfigure(6, weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.sidebar, text="🎓 Academic AI", font=FONT_TITLE,
                     text_color=COLORS["text"]).grid(row=0, column=0, pady=(30, 20), padx=20)

        self.nav_btns = {}
        tabs = [("chat", "💬  المحادثة"), ("careers", "🎓  التخصصات"),
                ("skills", "🛠️  المهارات"), ("search", "🔍  البحث"), ("help", "❓  المساعدة")]
        for i, (key, label) in enumerate(tabs, start=1):
            btn = self._nav_btn(label, lambda k=key: self._switch_tab(k))
            btn.grid(row=i, column=0, padx=15, pady=4, sticky="ew")
            self.nav_btns[key] = btn

        ctk.CTkButton(self.sidebar, text="🗑️  مسح المحادثة", font=FONT_BTN,
                      fg_color="transparent", hover_color="#3a1a1a",
                      text_color="#e74c3c", corner_radius=8,
                      command=self._clear_chat).grid(row=6, column=0, padx=15, pady=(0, 20), sticky="sew")

    def _nav_btn(self, label, cmd):
        return ctk.CTkButton(self.sidebar, text=label, font=FONT_BTN,
                             fg_color="transparent", hover_color=COLORS["accent"],
                             anchor="e", corner_radius=8, command=cmd)

    # ─────────── MAIN AREA ───────────
    def _build_main_area(self):
        self.main = ctk.CTkFrame(self.paned, fg_color=COLORS["bg"], corner_radius=0)
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        # Header
        header = ctk.CTkFrame(self.main, height=60, fg_color=COLORS["sidebar"], corner_radius=0)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)
        header.grid_columnconfigure(0, weight=1)
        self.header_label = ctk.CTkLabel(header, text="💬 المحادثة", font=FONT_TITLE,
                                          text_color=COLORS["text"], anchor="e")
        self.header_label.grid(row=0, column=0, padx=20, sticky="e")
        # مؤشر الاتصال
        status = "🟢 متصل بـ Gemini AI" if self.gemini.is_available() else "🔴 غير متصل"
        self.status_label = ctk.CTkLabel(header, text=status, font=FONT_SMALL,
                                          text_color=COLORS["subtext"], anchor="w")
        self.status_label.grid(row=0, column=1, padx=20, sticky="w")

        # Content frames
        self.frame_chat    = self._build_chat_frame()
        self.frame_careers = self._build_careers_frame()
        self.frame_skills  = self._build_skills_frame()
        self.frame_search  = self._build_search_frame()
        self.frame_help    = self._build_help_frame()

    # ─────────── TAB: CHAT ───────────
    def _build_chat_frame(self):
        frame = ctk.CTkFrame(self.main, fg_color=COLORS["bg"], corner_radius=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        self.chat_scroll = ctk.CTkScrollableFrame(frame, fg_color=COLORS["bg"], corner_radius=0)
        self.chat_scroll.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        self.chat_scroll.grid_columnconfigure(0, weight=1)

        # ─── Input area ───
        input_frame = ctk.CTkFrame(frame, fg_color=COLORS["sidebar"], corner_radius=12)
        input_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        input_frame.grid_columnconfigure(0, weight=1)

        # صف الأول: شرح الوضع الحالي
        self.mode_hint = ctk.CTkLabel(input_frame,
            text="🔵 استدلال أمامي: اكتب مهاراتك مفصولة بفاصلة — مثال: برمجة، رياضيات",
            font=FONT_SMALL, text_color=COLORS["subtext"], anchor="e")
        self.mode_hint.grid(row=0, column=0, padx=12, pady=(8, 0), sticky="e")

        # صف الثاني: القائمة + حقل الكتابة + زر الإرسال
        row2 = ctk.CTkFrame(input_frame, fg_color="transparent")
        row2.grid(row=1, column=0, sticky="ew", padx=8, pady=(4, 8))
        row2.grid_columnconfigure(1, weight=1)

        self.mode_menu = ctk.CTkOptionMenu(
            row2,
            values=["استدلال أمامي", "استدلال خلفي", "سؤال حر 🤖"],
            font=FONT_BTN, width=160, corner_radius=8,
            fg_color=COLORS["accent"], button_color=COLORS["accent2"],
            command=self._on_mode_change)
        self.mode_menu.grid(row=0, column=0, padx=(0, 6))

        self.entry = ctk.CTkEntry(
            row2,
            placeholder_text="",
            height=44, font=FONT_LABEL, justify="right", corner_radius=8)
        self.entry.grid(row=0, column=1, padx=(0, 6), sticky="ew")
        self.entry.bind("<Return>", lambda e: self._send())

        self.send_btn = ctk.CTkButton(
            row2, text="إرسال ➤", font=FONT_BTN,
            width=90, height=44, corner_radius=8,
            fg_color=COLORS["accent"], command=self._send)
        self.send_btn.grid(row=0, column=2)

        self._add_bot_message(
            "مرحباً! 👋 أنا نظام خبير أكاديمي ذكي.\n\n"
            "🔵 استدلال أمامي: اكتب مهاراتك → يعطيك التخصصات المناسبة\n"
            "🟠 استدلال خلفي: اكتب اسم تخصص → يعطيك خارطة الطريق\n"
            "🤖 سؤال حر: اسألني أي سؤال تقني")
        return frame

    # ─────────── TAB: CAREERS ───────────
    def _build_careers_frame(self):
        frame = ctk.CTkFrame(self.main, fg_color=COLORS["bg"], corner_radius=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="التخصصات المتاحة", font=FONT_TITLE,
                     text_color=COLORS["text"], anchor="e").grid(row=0, column=0, pady=(15, 5), padx=20, sticky="e")

        scroll = ctk.CTkScrollableFrame(frame, fg_color=COLORS["bg"], corner_radius=0)
        scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        scroll.grid_columnconfigure((0, 1), weight=1)

        for i, (name, data) in enumerate(self.engine.knowledge_base.items()):
            h = data["cost"]
            bar = "█" * (h // 10) + "░" * (10 - h // 10)
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=12)
            card.grid(row=i // 2, column=i % 2, padx=8, pady=8, sticky="nsew")
            card.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(card, text=f"{data['emoji']} {name}", font=FONT_BTN,
                         text_color=COLORS["text"], anchor="e").grid(row=0, column=0, padx=15, pady=(12, 2), sticky="e")
            ctk.CTkLabel(card, text=data["desc"], font=FONT_SMALL,
                         text_color=COLORS["subtext"], anchor="e", wraplength=280).grid(row=1, column=0, padx=15, pady=2, sticky="e")
            ctk.CTkLabel(card, text=f"⏱️ {data['duration']}   💰 {data['salary']}", font=FONT_SMALL,
                         text_color=COLORS["subtext"], anchor="e").grid(row=2, column=0, padx=15, pady=2, sticky="e")
            ctk.CTkLabel(card, text=f"الصعوبة: {h}/100  [{bar}]", font=FONT_SMALL,
                         text_color=COLORS["accent2"], anchor="e").grid(row=3, column=0, padx=15, pady=(2, 12), sticky="e")

        return frame

    # ─────────── TAB: SKILLS ───────────
    def _build_skills_frame(self):
        frame = ctk.CTkFrame(self.main, fg_color=COLORS["bg"], corner_radius=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="المهارات المطلوبة لكل تخصص", font=FONT_TITLE,
                     text_color=COLORS["text"], anchor="e").grid(row=0, column=0, pady=(15, 5), padx=20, sticky="e")

        scroll = ctk.CTkScrollableFrame(frame, fg_color=COLORS["bg"], corner_radius=0)
        scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        scroll.grid_columnconfigure(0, weight=1)

        for name, data in self.engine.knowledge_base.items():
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=12)
            card.grid(sticky="ew", padx=8, pady=6)
            card.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(card, text=f"{data['emoji']} {name}", font=FONT_BTN,
                         text_color=COLORS["text"], anchor="e").grid(row=0, column=0, padx=15, pady=(10, 4), sticky="e")

            chips_frame = ctk.CTkFrame(card, fg_color="transparent")
            chips_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="e")

            row_frame = None
            for i, skill in enumerate(data["skills"]):
                if i % 5 == 0:
                    row_frame = ctk.CTkFrame(chips_frame, fg_color="transparent")
                    row_frame.pack(anchor="e", pady=3, fill="x")
                chip = ctk.CTkLabel(row_frame, text=skill, font=FONT_SMALL,
                                    fg_color=COLORS["accent"], text_color=COLORS["text"],
                                    corner_radius=8, padx=10, pady=4)
                chip.pack(side="right", padx=4)

        return frame

    # ─────────── TAB: SEARCH ───────────
    def _build_search_frame(self):
        frame = ctk.CTkFrame(self.main, fg_color=COLORS["bg"], corner_radius=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="البحث في خارطة الطريق", font=FONT_TITLE,
                     text_color=COLORS["text"], anchor="e").grid(row=0, column=0, pady=(15, 5), padx=20, sticky="e")

        # Controls
        ctrl = ctk.CTkFrame(frame, fg_color=COLORS["sidebar"], corner_radius=12)
        ctrl.grid(row=1, column=0, sticky="new", padx=10, pady=(0, 8))
        ctrl.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(ctrl, text="اختر التخصص:", font=FONT_LABEL,
                     text_color=COLORS["subtext"], anchor="e").grid(row=0, column=2, padx=(10, 5), pady=(12, 4), sticky="e")
        self.search_career_menu = ctk.CTkOptionMenu(
            ctrl, font=FONT_BTN, corner_radius=8,
            fg_color=COLORS["accent"], button_color=COLORS["accent2"],
            values=list(self.engine.knowledge_base.keys()))
        self.search_career_menu.grid(row=1, column=2, padx=(10, 5), pady=(0, 12), sticky="ew")

        ctk.CTkLabel(ctrl, text="الخطوة المستهدفة:", font=FONT_LABEL,
                     text_color=COLORS["subtext"], anchor="e").grid(row=0, column=1, padx=5, pady=(12, 4), sticky="e")
        self.search_target_entry = ctk.CTkEntry(ctrl, placeholder_text="مثال: تعلم الآلة",
                                                font=FONT_LABEL, justify="right", corner_radius=8)
        self.search_target_entry.grid(row=1, column=1, padx=5, pady=(0, 12), sticky="ew")

        btn_frame = ctk.CTkFrame(ctrl, fg_color="transparent")
        btn_frame.grid(row=1, column=0, padx=(5, 10), pady=(0, 12), sticky="ew")
        ctk.CTkButton(btn_frame, text="BFS 🔵", font=FONT_BTN, corner_radius=8,
                      fg_color="#1a6b3a", hover_color="#27ae60",
                      command=lambda: self._run_graph_search("bfs")).pack(side="right", padx=4)
        ctk.CTkButton(btn_frame, text="DFS 🟠", font=FONT_BTN, corner_radius=8,
                      fg_color="#7d4e00", hover_color="#e67e22",
                      command=lambda: self._run_graph_search("dfs")).pack(side="right", padx=4)
        ctk.CTkButton(btn_frame, text="💡 تلميح", font=FONT_BTN, corner_radius=8,
                      fg_color=COLORS["sidebar"], hover_color=COLORS["accent"],
                      command=self._show_hint).pack(side="right", padx=4)

        # Result area
        self.search_result = ctk.CTkScrollableFrame(frame, fg_color=COLORS["bg"], corner_radius=0)
        self.search_result.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.search_result.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        self._show_graph_placeholder()
        return frame

    def _show_graph_placeholder(self):
        ctk.CTkLabel(self.search_result,
                     text="اختر تخصصاً وأدخل الخطوة المستهدفة ثم اضغط BFS أو DFS",
                     font=FONT_LABEL, text_color=COLORS["subtext"], anchor="e").grid(
                     row=0, column=0, pady=40, padx=20, sticky="e")

    def _show_hint(self):
        career = self.search_career_menu.get()
        graph_data, all_nodes = self.engine.build_graph(career)
        for w in self.search_result.winfo_children():
            w.destroy()
        card = ctk.CTkFrame(self.search_result, fg_color=COLORS["card"], corner_radius=12)
        card.grid(row=0, column=0, sticky="ew", padx=8, pady=6)
        card.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(card, text=f"💡 عقد الـ Graph لـ {career}",
                     font=FONT_BTN, text_color=COLORS["accent2"], anchor="e").grid(
                     padx=15, pady=(12, 6), sticky="e")
        for node, neighbors in graph_data.items():
            row = ctk.CTkFrame(card, fg_color="transparent")
            row.grid(padx=20, pady=2, sticky="e")
            row.grid_columnconfigure(0, weight=1)
            txt = f"● {node}"
            if neighbors:
                txt += f"  →  {'  |  '.join(neighbors)}"
            ctk.CTkLabel(row, text=txt, font=FONT_SMALL,
                         text_color=COLORS["text"], anchor="e").grid(sticky="e")
        ctk.CTkLabel(card, text="✅ اكتب أي جزء من اسم العقدة في حقل البحث",
                     font=FONT_SMALL, text_color=COLORS["subtext"], anchor="e").grid(
                     padx=15, pady=(4, 12), sticky="e")

    def _run_graph_search(self, method):
        career = self.search_career_menu.get()
        target = self.search_target_entry.get().strip()
        if not target:
            return

        for w in self.search_result.winfo_children():
            w.destroy()

        if method == "bfs":
            path, all_steps = self.engine.bfs_search(career, target)
            algo_name, algo_color = "BFS (اتساع أولاً)", "#27ae60"
        else:
            path, all_steps = self.engine.dfs_search(career, target)
            algo_name, algo_color = "DFS (عمق أولاً)", "#e67e22"

        # عرض الـ Graph كاملاً
        graph_card = ctk.CTkFrame(self.search_result, fg_color=COLORS["card"], corner_radius=12)
        graph_card.grid(row=0, column=0, sticky="ew", padx=8, pady=6)
        graph_card.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(graph_card, text=f"🗺️ Graph كامل لـ {career}",
                     font=FONT_BTN, text_color=COLORS["text"], anchor="e").grid(
                     padx=15, pady=(12, 6), sticky="e")

        nodes_frame = ctk.CTkFrame(graph_card, fg_color="transparent")
        nodes_frame.grid(padx=15, pady=(0, 12), sticky="e")
        graph_data, _ = self.engine.build_graph(career)
        for node, neighbors in graph_data.items():
            in_path = path and node in path
            color = algo_color if in_path else COLORS["subtext"]
            icon  = "🔵" if in_path else "⚪"
            row = ctk.CTkFrame(nodes_frame, fg_color="transparent")
            row.pack(anchor="e", pady=1)
            # عرض التفرعات
            if neighbors:
                branches = " → ".join(neighbors)
                ctk.CTkLabel(row, text=f"└→ {branches}",
                             font=FONT_SMALL, text_color="#555", anchor="e").pack(side="left", padx=(0, 8))
            ctk.CTkLabel(row, text=f"{icon} {node}",
                         font=FONT_LABEL, text_color=color, anchor="e").pack(side="right")

        # عرض نتيجة البحث
        result_card = ctk.CTkFrame(self.search_result, fg_color=COLORS["card"], corner_radius=12)
        result_card.grid(row=1, column=0, sticky="ew", padx=8, pady=6)
        result_card.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(result_card, text=f"نتيجة {algo_name}",
                     font=FONT_BTN, text_color=algo_color, anchor="e").grid(
                     padx=15, pady=(12, 6), sticky="e")

        if path:
            path_text = "  ←  ".join(reversed(path))
            ctk.CTkLabel(result_card, text=f"✅ المسار: {path_text}",
                         font=FONT_LABEL, text_color=COLORS["text"],
                         anchor="e", wraplength=600).grid(padx=15, pady=(0, 6), sticky="e")
            ctk.CTkLabel(result_card, text=f"📏 عدد الخطوات: {len(path)}",
                         font=FONT_SMALL, text_color=COLORS["subtext"], anchor="e").grid(
                         padx=15, pady=(0, 12), sticky="e")
        else:
            ctk.CTkLabel(result_card,
                         text=f"❌ لم يتم العثور على '{target}' في خارطة {career}",
                         font=FONT_LABEL, text_color="#e74c3c", anchor="e").grid(
                         padx=15, pady=(0, 6), sticky="e")
            ctk.CTkLabel(result_card, text="💡 اضغط 'تلميح' لرؤية الخطوات المتاحة",
                         font=FONT_SMALL, text_color=COLORS["subtext"], anchor="e").grid(
                         padx=15, pady=(0, 12), sticky="e")

    # ─────────── TAB: HELP ───────────
    def _build_help_frame(self):
        frame = ctk.CTkFrame(self.main, fg_color=COLORS["bg"], corner_radius=0)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="دليل الاستخدام", font=FONT_TITLE,
                     text_color=COLORS["text"], anchor="e").grid(row=0, column=0, pady=(15, 5), padx=20, sticky="e")

        scroll = ctk.CTkScrollableFrame(frame, fg_color=COLORS["bg"], corner_radius=0)
        scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        scroll.grid_columnconfigure(0, weight=1)

        sections = [
            ("🔵 الاستدلال الأمامي (Forward Chaining)",
             "أدخل مهاراتك مفصولة بفاصلة، وسيقترح النظام التخصصات المناسبة مع نسبة الثقة.\n"
             "مثال: برمجة، رياضيات، بيانات"),
            ("🟠 الاستدلال الخلفي (Backward Chaining)",
             "أدخل اسم التخصص الذي تريده، وسيعطيك النظام خارطة طريق كاملة.\n"
             "مثال: ذكاء اصطناعي  أو  أمن سيبراني"),
            ("📊 التحليل الاستدلالي (Heuristic)",
             "يظهر تلقائياً مع الاستدلال الخلفي، ويوضح مستوى صعوبة التخصص من 0 إلى 100."),
            ("🎓 تبويب التخصصات",
             "يعرض جميع التخصصات الـ 8 مع الوصف والراتب والمدة ومستوى الصعوبة."),
            ("🛠️ تبويب المهارات",
             "يعرض المهارات المطلوبة لكل تخصص على شكل شارات ملونة."),
            ("💡 نصائح",
             "• يمكنك الكتابة بالعربية أو الإنجليزية (python = برمجة)\n"
             "• اضغط Enter للإرسال السريع\n"
             "• استخدم زر 'مسح المحادثة' لبدء محادثة جديدة"),
        ]

        for title, body in sections:
            card = ctk.CTkFrame(scroll, fg_color=COLORS["card"], corner_radius=12)
            card.grid(sticky="ew", padx=8, pady=6)
            card.grid_columnconfigure(0, weight=1)
            ctk.CTkLabel(card, text=title, font=FONT_BTN, text_color=COLORS["accent2"],
                         anchor="e").grid(padx=15, pady=(12, 4), sticky="e")
            ctk.CTkLabel(card, text=body, font=FONT_LABEL, text_color=COLORS["subtext"],
                         anchor="e", justify="right", wraplength=580).grid(padx=15, pady=(0, 12), sticky="e")

        return frame

    # ─────────── TAB SWITCHING ───────────
    def _switch_tab(self, tab):
        titles = {"chat": "💬 المحادثة", "careers": "🎓 التخصصات",
                  "skills": "🛠️ المهارات", "search": "🔍 البحث في الـ Graph", "help": "❓ المساعدة"}
        frames = {"chat": self.frame_chat, "careers": self.frame_careers,
                  "skills": self.frame_skills, "search": self.frame_search, "help": self.frame_help}

        for f in frames.values():
            f.grid_forget()
        frames[tab].grid(row=1, column=0, sticky="nsew")
        self.main.grid_rowconfigure(1, weight=1)

        self.header_label.configure(text=titles[tab])
        for key, btn in self.nav_btns.items():
            btn.configure(fg_color=COLORS["accent"] if key == tab else "transparent")

    def _on_mode_change(self, mode):
        hints = {
            "استدلال أمامي":  "🔵 استدلال أمامي: اكتب مهاراتك مفصولة بفاصلة — مثال: برمجة، رياضيات",
            "استدلال خلفي":  "🟠 استدلال خلفي: اكتب اسم التخصص — مثال: ذكاء اصطناعي أو أمن سيبراني",
            "سؤال حر 🤖": "🤖 سؤال حر: اسألني أي سؤال تقني أو أكاديمي",
        }
        placeholders = {
            "استدلال أمامي":  "مثال: برمجة، رياضيات، بيانات",
            "استدلال خلفي":  "مثال: ذكاء اصطناعي أو أمن سيبراني",
            "سؤال حر 🤖": "مثال: ما الفرق بين Python و Java؟",
        }
        self.mode_hint.configure(text=hints.get(mode, ""))
        self.entry.configure(placeholder_text=placeholders.get(mode, ""))

    # ─────────── CHAT LOGIC ───────────
    def _send(self):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        mode = "forward" if self.mode_menu.get() == "استدلال أمامي" else (
               "backward" if self.mode_menu.get() == "استدلال خلفي" else "free")
        self._add_user_message(user_text)
        self.entry.delete(0, "end")
        self.send_btn.configure(state="disabled")
        self._add_typing_indicator()
        threading.Thread(target=self._run_ai, args=(user_text, mode), daemon=True).start()

    def _run_ai(self, text, mode):
        time.sleep(0.8)
        source = "local"
        try:
            if mode == "forward":
                skills = [s.strip() for s in text.replace(",", "،").split("،") if s.strip()]
                skills = skills or [text]
                results = self.engine.forward_chaining(skills)
                results = self.engine.get_boosted_results(results)
                if results:
                    source = "forward"
                    lines = []
                    for career, conf, matches, emoji, desc, salary in results:
                        bar_filled = int(conf // 10)
                        bar = "█" * bar_filled + "░" * (10 - bar_filled)
                        counts = self.engine.user_memory["career_counts"]
                        boost_note = f"  ⬆️ مُعزَّز (بحثت عنه {counts[career]} مرة)" if counts.get(career) else ""
                        lines.append(
                            f"{emoji} {career}{boost_note}\n"
                            f"   الثقة: {conf}%  [{bar}]\n"
                            f"   المهارات المطابقة: {'، '.join(matches)}\n"
                            f"   💰 {salary}"
                        )
                    response = "✅ التخصصات المناسبة لمهاراتك:\n\n" + "\n\n".join(lines)
                    top = self.engine.get_top_career()
                    if top:
                        missing = self.engine.get_missing_skills(skills, top)
                        if missing:
                            response += (
                                f"\n\n💡 بما أنك مهتم بـ {top}:\n"
                                f"   المهارات الناقصة: {'، '.join(missing)}"
                            )
                else:
                    response = "⚠️ لم أجد تخصصاً يطابق هذه المهارات.\n💡 جرب مهارات مثل: برمجة، رياضيات، تصميم، شبكات"
            elif mode == "backward":
                self.engine.record_interest(text)
                response = self.engine.backward_chaining(text)
                heuristic = self.engine.heuristic_analysis(text)
                if heuristic:
                    response += f"\n\n{heuristic}"
                counts = self.engine.user_memory["career_counts"]
                key = self.engine._find_career_key(text)
                if key and counts.get(key, 0) > 1:
                    response += f"\n\n🧠 بحثت عن هذا التخصص {counts[key]} مرة — يبدو أنك مهتم جداً!"
                source = "backward"
            else:
                source = "gemini"
                if self.gemini.is_available():
                    response = self.gemini.ask(text)
                else:
                    response = "⚠️ الاتصال بـ Gemini غير متاح.\n💡 أضف مفتاحك في ملف .env"
        except Exception as e:
            response = f"⚠️ حدث خطأ: {e}"
        self.after(0, self._on_response, response, source)

    def _on_response(self, response, source="local"):
        self._remove_typing_indicator()
        self._add_bot_message(response, source)
        self.send_btn.configure(state="normal")

    # ─────────── MESSAGE BUBBLES ───────────
    def _add_bot_message(self, text, source="local"):
        styles = {
            "local":    (COLORS["bot_bubble"], "🧠 النظام الخبير"),
            "forward":  ("#1a3a1a",            "🔵 استدلال أمامي"),
            "backward": ("#1a1a3a",            "🟠 استدلال خلفي"),
            "gemini":   ("#2a1a2a",            "🤖 Gemini AI"),
        }
        bg, label = styles.get(source, styles["local"])

        # شارة المصدر
        ctk.CTkLabel(self.chat_scroll, text=label, font=FONT_SMALL,
                     text_color=COLORS["subtext"], fg_color="transparent",
                     anchor="e").pack(anchor="e", padx=(60, 5), pady=(6, 0))

        bubble = ctk.CTkTextbox(self.chat_scroll, font=FONT_BUBBLE,
                                fg_color=bg, text_color=COLORS["text"],
                                corner_radius=14, wrap="word", activate_scrollbars=False,
                                padx=15, pady=10)
        bubble.insert("1.0", text)
        bubble.configure(state="disabled")
        bubble.bind("<Button-3>", lambda e: self._show_copy_menu(e, bubble))
        bubble.bind("<Control-c>", lambda e: self._copy_text(bubble))
        lines = text.count("\n") + 1
        bubble.configure(height=max(lines * 24 + 20, 60), width=520)
        bubble.pack(anchor="e", padx=(60, 5), pady=(0, 4))
        self.after(100, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))

    def _copy_text(self, textbox):
        try:
            selected = textbox.get("sel.first", "sel.last")
            self.clipboard_clear()
            self.clipboard_append(selected)
        except:
            self.clipboard_clear()
            self.clipboard_append(textbox.get("1.0", "end-1c"))

    def _copy_all(self, textbox):
        self.clipboard_clear()
        self.clipboard_append(textbox.get("1.0", "end-1c"))

    def _show_copy_menu(self, event, textbox):
        menu = tk.Menu(self, tearoff=0, bg=COLORS["card"], fg=COLORS["text"],
                       activebackground=COLORS["accent"], activeforeground=COLORS["text"])
        menu.add_command(label="نسخ المحدد", command=lambda: self._copy_text(textbox))
        menu.add_command(label="نسخ الكل",     command=lambda: self._copy_all(textbox))
        menu.post(event.x_root, event.y_root)

    def _add_user_message(self, text):
        bubble = ctk.CTkLabel(self.chat_scroll, text=text, font=FONT_BUBBLE,
                              fg_color=COLORS["accent"], text_color=COLORS["text"],
                              corner_radius=14, padx=15, pady=10,
                              wraplength=520, justify="right", anchor="e")
        bubble.pack(anchor="w", pady=6, padx=(5, 60))
        self.after(100, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))

    def _add_typing_indicator(self):
        self.typing_label = ctk.CTkLabel(self.chat_scroll, text="⏳ جاري التفكير...",
                                         font=FONT_SMALL, text_color=COLORS["subtext"],
                                         fg_color="transparent")
        self.typing_label.pack(anchor="e", pady=4, padx=10)
        self.after(100, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))

    def _remove_typing_indicator(self):
        if hasattr(self, "typing_label") and self.typing_label.winfo_exists():
            self.typing_label.destroy()

    def _clear_chat(self):
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()
        self._add_bot_message("تم مسح المحادثة. كيف يمكنني مساعدتك؟ 😊")


if __name__ == "__main__":
    app = AcademicAIApp()
    app.mainloop()

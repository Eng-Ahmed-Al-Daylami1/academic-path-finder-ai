# Contributing to Academic Path Finder AI
# المساهمة في نظام التوجيه الأكاديمي الذكي

Thank you for your interest in contributing! | شكراً لاهتمامك بالمساهمة!

## How to Contribute | كيفية المساهمة

### 1. Fork the Repository
Click the "Fork" button at the top right of this page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/academic-path-finder-ai.git
cd academic-path-finder-ai
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Follow the existing code style
- Add comments in Arabic for domain logic
- Test your changes thoroughly

### 5. Commit Your Changes
```bash
git add .
git commit -m "Add: description of your changes"
```

### 6. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request
Go to the original repository and click "New Pull Request"

---

## Areas for Contribution | مجالات المساهمة

### 🎯 High Priority | أولوية عالية
- Add more specializations to knowledge base
- Improve skill normalization (more aliases)
- Add English UI option
- Enhance graph visualization

### 🔧 Medium Priority | أولوية متوسطة
- Add unit tests
- Improve error handling
- Add export functionality (PDF reports)
- Add career comparison feature

### 💡 Ideas Welcome | أفكار مرحب بها
- Integration with other AI models
- Mobile app version
- Web version
- Database integration

---

## Code Style Guidelines | إرشادات أسلوب الكود

### Python Code
- Follow PEP 8 standards
- Use meaningful variable names
- One class per file
- Private methods prefixed with `_`

### Naming Conventions
- Classes: `PascalCase`
- Methods: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Variables: `snake_case`

### Comments
- Arabic for domain logic explanations
- English for technical implementation notes
- Use section dividers: `# ─────────── SECTION ───────────`

### UI Guidelines
- Always use RTL layout for Arabic text
- Use `COLORS` dict for all colors
- Use `FONT_*` tuples for all fonts
- Maintain consistent spacing (padx=10, pady=8)

---

## Testing | الاختبار

Before submitting a PR, ensure:
- [ ] Code runs without errors
- [ ] All features work as expected
- [ ] No breaking changes to existing functionality
- [ ] Arabic text displays correctly (RTL)

---

## Adding New Specializations | إضافة تخصصات جديدة

To add a new specialization to the knowledge base:

```python
"اسم التخصص": {
    "skills": ["مهارة 1", "مهارة 2", ...],
    "roadmap": ["خطوة 1", "خطوة 2", ...],
    "cost": 75,  # Difficulty score 0-100
    "emoji": "🎯",
    "desc": "وصف مختصر",
    "duration": "2-3 سنوات",
    "salary": "$50,000 - $90,000"
}
```

---

## Questions? | أسئلة؟

Open an issue or contact the maintainer.

---

## Code of Conduct | قواعد السلوك

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Focus on what is best for the community

---

Thank you for contributing! | شكراً لمساهمتك! 🎉

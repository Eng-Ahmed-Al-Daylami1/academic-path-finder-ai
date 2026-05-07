# 🎓 Academic Path Finder AI
### AI-Powered Career Guidance Expert System | Smart Career Counseling | Tech Career Advisor

> **An intelligent career guidance system using Expert Systems, Forward/Backward Chaining, BFS/DFS algorithms, and Google Gemini AI for personalized tech career recommendations.**

> 🎓 **Note**: This is a simple university assignment developed for the Artificial Intelligence course (4th Year IT, 2024-2025).

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AI](https://img.shields.io/badge/AI-Expert%20System-red.svg)]()
[![Arabic](https://img.shields.io/badge/Language-Arabic%20%2B%20English-green.svg)]()

[العربية](README_AR.md) | **English**

---

## 🔍 Keywords

`expert system` `career guidance` `artificial intelligence` `forward chaining` `backward chaining` `BFS algorithm` `DFS algorithm` `career counseling` `academic advisor` `tech careers` `python AI` `gemini AI` `machine learning` `knowledge base` `inference engine` `career path finder` `student guidance` `job recommendation` `skill matching` `educational AI` `arabic AI` `university project`

---

## 📋 Overview

An **intelligent career guidance and academic counseling system** powered by **Artificial Intelligence** and **Expert System** techniques. This project helps **students**, **job seekers**, and **career changers** make informed decisions about their **tech career path** using advanced AI reasoning methods.

### What Makes This Unique?

This is a **complete AI-powered career advisor** that combines:
- 🎓 **Classical AI**: Expert Systems with Forward/Backward Chaining inference
- 🤖 **Modern AI**: Google Gemini LLM integration for natural conversations
- 📊 **Data Science**: Graph algorithms (BFS/DFS) for optimal learning paths
- 🧠 **Machine Learning**: Adaptive learning from user behavior
- 🌐 **Bilingual**: Full Arabic and English support

**Perfect for**: University AI projects, career counseling applications, educational technology, student guidance systems, tech career planning tools.

### 🎯 Key Features

- **🔄 Forward Chaining**: Input your skills → Get ranked matching specializations with confidence scores
- **🔙 Backward Chaining**: Input desired career → Get complete roadmap, required skills, duration, and salary
- **📊 Heuristic Analysis**: Difficulty scoring (0-100) with visual progress bars for each career path
- **🔍 BFS & DFS Search**: Graph-based pathfinding through learning roadmaps
- **🧠 Adaptive Learning**: System learns from user behavior and adjusts recommendations
- **🤖 Gemini AI Integration**: Natural language Q&A for free-form questions
- **🌐 Bilingual Support**: Accepts both Arabic and English skill inputs via synonym normalization

---

## 🎯 Use Cases | Who Can Benefit?

### 🎓 Students
- **High school graduates** choosing university majors
- **University students** exploring career options
- **Computer science students** learning AI concepts

### 💼 Professionals
- **Career changers** transitioning to tech
- **Job seekers** identifying skill gaps
- **HR professionals** for employee development

### 🏫 Educators
- **Academic advisors** guiding students
- **Career counselors** providing data-driven advice
- **AI instructors** teaching expert systems

### 👨💻 Developers
- Learning **expert system** implementation
- Understanding **AI reasoning** techniques
- Building **knowledge-based systems**

---

## 🎓 Academic Value

This project demonstrates:
- ✅ **Expert System Architecture** (Knowledge Base + Inference Engine)
- ✅ **Forward Chaining** (Data-Driven Reasoning)
- ✅ **Backward Chaining** (Goal-Driven Reasoning)
- ✅ **Graph Search Algorithms** (BFS & DFS)
- ✅ **Heuristic Evaluation** (Difficulty Scoring)
- ✅ **Adaptive Learning** (User Behavior Analysis)
- ✅ **LLM Integration** (Gemini AI)
- ✅ **MVC Architecture** (Clean Code Design)

**Perfect for**: AI course projects, machine learning portfolios, software engineering capstone projects.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Eng-Ahmed-Al-Daylami1/academic-path-finder-ai.git
cd academic-path-finder-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Gemini API key
GEMINI_API_KEY=your_actual_api_key_here
```

4. **Run the application**
```bash
python main.py
```

---

## 🏗️ Architecture

### Project Structure
```
am/
├── main.py              # GUI layer (View + Controller)
├── logic.py             # AI engine (Model - inference + knowledge base)
├── ai_service.py        # Gemini AI integration
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── .gitignore          # Git ignore rules
```

### Design Pattern
**Simplified MVC Architecture**:
- **Model** (`logic.py`): Knowledge base, inference algorithms, data processing
- **View + Controller** (`main.py`): GUI rendering, user interaction, event handling
- **External AI** (`ai_service.py`): LLM integration for natural language queries

---

## 🧠 AI Techniques Used

### 1. Forward Chaining (Data-Driven Reasoning)
```
User Skills: [Programming, Math]
         ↓
System checks all specializations
         ↓
Calculates intersection: {Programming, Math} ∩ {Programming, Math, Data, Statistics, ML}
         ↓
Result: 2/5 = 40% confidence
         ↓
Ranks all specializations by confidence
```

### 2. Backward Chaining (Goal-Driven Reasoning)
```
User Goal: "AI Expert"
         ↓
System searches knowledge base
         ↓
Finds: "خبير ذكاء اصطناعي"
         ↓
Extracts: Skills + Roadmap + Duration + Salary
         ↓
Displays complete learning path
```

### 3. Graph Search Algorithms

**BFS (Breadth-First Search)**:
- Uses Queue (FIFO)
- Guarantees shortest path
- Level-by-level exploration

**DFS (Depth-First Search)**:
- Uses Stack (LIFO)
- Finds first available path
- Deep exploration first

### 4. Adaptive Learning
```python
# System remembers user interests
career_counts["AI Expert"] += 1

# Boosts confidence in future recommendations
boost = min(counts.get(career, 0) * 5, 20)  # Max 20%
confidence = min(confidence + boost, 100)
```

### 5. Heuristic Analysis
- Difficulty scoring based on expert knowledge
- Threshold-based classification (85/70/55)
- Visual feedback with progress bars

### 6. LLM Integration (Gemini AI)
- **Constrained prompting** for domain-specific responses
- Fallback mechanism for unmatched queries
- Natural language understanding

---

## 📚 Supported Specializations

| Specialization | Difficulty | Duration |
|---|---|---|
| 🤖 AI Expert | 90/100 | 3-4 years |
| 🔒 Cybersecurity Engineer | 75/100 | 2-3 years |
| 📊 Big Data Analyst | 65/100 | 2 years |
| 📱 Mobile Developer | 60/100 | 1.5-2 years |
| ☁️ Cloud Engineer | 80/100 | 2-3 years |
| 🎨 UX/UI Designer | 50/100 | 1-1.5 years |
| 🌐 Full-Stack Web Developer | 55/100 | 1.5-2 years |
| 🦾 Robotics Engineer | 95/100 | 4-5 years |

---

## 🎮 Usage Examples

### Example 1: Forward Chaining
```
Input: برمجة، رياضيات، تعلم الآلة
Output: 
  1. خبير ذكاء اصطناعي - 60% ████████░░
  2. محلل بيانات ضخمة - 45% ████░░░░░░
  3. مطور ويب متكامل - 30% ███░░░░░░░
```

### Example 2: Backward Chaining
```
Input: ذكاء اصطناعي
Output:
  📚 المهارات المطلوبة: برمجة، رياضيات، تعلم الآلة، ...
  🗺️ خارطة الطريق: [10 steps]
  ⏱️ المدة: 3-4 سنوات
  💰 الراتب: $80,000 - $150,000
```

### Example 3: BFS vs DFS
```
Goal: Find path to "Neural Networks"

BFS: Python Basics → Linear Algebra → Machine Learning → Neural Networks
DFS: Python Basics → Python Libraries → Machine Learning → Neural Networks
```

---

## 🛠️ Technologies

- **Language**: Python 3.8+
- **GUI Framework**: CustomTkinter (modern themed widgets)
- **AI/LLM**: Google Gemini API
- **Architecture**: MVC pattern
- **Search Algorithms**: BFS, DFS, Forward/Backward Chaining
- **Learning**: Adaptive reinforcement-style learning

---

## 📖 Documentation

- [Arabic Documentation](توثيق_المشروع.txt)
- [Technical Details](توثيق%20جديد.txt)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨💻 Author

**Ahmed Al-Daylami**
- 🎓 **Simple University Assignment** - Artificial Intelligence Course
- 📚 4th Year IT Student
- 🏫 Community College - Sana'a
- 📅 Academic Year: 2024-2025
- 📍 Yemen

---

## 🙏 Acknowledgments

- Google Gemini AI for natural language processing
- CustomTkinter for the modern GUI framework
- Academic advisors and domain experts for knowledge base validation

---

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

**⭐ If you find this project helpful, please give it a star!**

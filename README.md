# ✨ AI StoryTeller: Transforming Images into Magic 📖

AI StoryTeller is a premium web application that breathes life into your photos. By leveraging the power of **BLIP (Image Captioning)** and **Google Gemini 2.0**, it transforms visual moments into enchanting, human-like stories with just a few clicks.

## 🚀 Features

- **🎨 Premium Dark UI**: A modern, immersive interface featuring glassmorphism, smooth animations, and a "Magic" aesthetic.
- **🖼️ Instant Image Preview**: See your moments immediately before they are transformed.
- **🤖 Gemini 2.0 Powered**: Utilizes the latest `gemini-2.0-flash` model for intelligent and creative storytelling.
- **🎭 Genre & Mood Control**: Guide the AI's creativity by selecting specific genres (Fantasy, Sci-Fi, Mystery) and moods (Whimsical, Cinematic, Tense).
- **⚡ Real-time Feedback**: Engaging loading states and refined error handling ("Magic Interrupted") for a seamless experience.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **AI Models**:
  - Image Captioning: Salesforce BLIP
  - Storytelling: Google Gemini 2.0 Flash
- **Frontend**: Vanilla HTML5, CSS3 (Modern Glassmorphism Design), JavaScript (ES6+)
- **Environment**: Python Dotenv for secure key management.

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-StoryTeller.git
cd AI-StoryTeller
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Create a `.env` file in the root directory and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application

```bash
python -m app.main
```

Head over to `http://127.0.0.1:8000` to start crafting your stories!

## 🛡️ Security & Privacy

- **Secure Keys**: The `.env` file is protected and ignored by Git.
- **Private Media**: The `uploads/` directory and temporary image files are excluded from commits to ensure your privacy.

## 📜 License

This project is licensed under the MIT License.

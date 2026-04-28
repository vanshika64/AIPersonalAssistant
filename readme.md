# 🤖 AI Personal Assistant (Flask + OpenAI)

An intelligent web-based assistant that can **answer user queries** and **summarize emails** using OpenAI API. Built with Flask for backend and Jinja + JavaScript for dynamic frontend interaction.

---

## 🚀 Features

* 💬 Ask anything (AI-powered responses)
* 📧 Email summarization (2–3 line concise output)
* ⚡ Real-time responses using Fetch API (no page reload)
* 🎯 Clean and responsive UI Interface
* 🔒 Secure API key handling using environment variables

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Templating:** Jinja2
* **API:** OpenAI API
* **Environment:** python-dotenv

---

## 📂 Project Structure

```
project/
│
├── main.py
├── .env
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── __pycache__/
```

---

## ⚙️ How It Works

1. User enters a question or email input
2. JavaScript captures form data and sends it via `fetch()`
3. Flask backend receives request
4. OpenAI API processes input
5. Response is returned as JSON
6. Frontend dynamically updates UI

---

## ▶️ Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file:

```
OPEN_AI_API=your_api_key_here
```

### 4. Run the app

```
python main.py
```

Visit:

```
http://127.0.0.1:5000/
```

## 🎯 Learning Outcomes

* Built full-stack AI application using Flask
* Integrated OpenAI API for real-time responses
* Implemented asynchronous frontend using JavaScript
* Understood request-response cycle in web apps
* Practiced clean UI + structured backend design

---

## 🚀 Future Improvements

* Add authentication system
* Deploy using Render / Railway
* Add chat history
* Improve UI/UX
* Add rate limiting for API usage

---

## 🙌 Author

**Vanshika Dhull**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

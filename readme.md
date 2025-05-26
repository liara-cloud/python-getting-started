# 🌤️ Weather Assistant using LiaraAI + wttr.in API

This Python script demonstrates how to use **OpenAI's function calling** capabilities to dynamically fetch real-time weather information from the free and public [wttr.in](https://wttr.in) weather API.

---

## 🚀 Features

- Integrates with Liara API via **function calling** (tool calls).
- Fetches **real-time weather** using the free `wttr.in` API.
- Supports both **Celsius** and **Fahrenheit** units.
- Auto-extracts relevant arguments from user messages via LLM.
- Simple, readable output in the terminal.

---


## 🧰 Running the app

```
git clone https://github.com/liara-cloud/python-getting-started.git
```

```
cd python-getting-started
```


```
git checkout ai
```


```bash
pip install -r requirements.txt
```

```
mv .env.example .env
```

- set ENVs on `.env`

```
python main.py
```



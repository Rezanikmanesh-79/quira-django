# 🧠 Quira Django Blog Project

**Quira** is a blog-style web application built with the Django web framework. It includes features like publishing posts, filtering, search, and an admin panel – ideal for practicing core Django concepts.

---

## 🚀 Features

- 📬 Create, publish, and manage blog posts
- 🔍 Post filtering by author or status
- 🔎 Full-text search in titles and content
- 🧑‍💼 Admin panel with advanced customization
- 🗓 Jalali calendar support via `django-jalali`
- 🌐 Persian (Farsi) language interface

---

## 🧰 Stack

- Python 3.11+
- Django 5.x
- HTML/CSS (via templates)
- SQLite (default for development)
- `django-jalali` for Jalali date filters

---

## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/Rezanikmanesh-79/quira-django.git
cd quira-django
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
---
📁 Project Structure
```bash
quira-django/
├── blog/               # Main blog app
├── core/               # Django project settings
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS)
├── media/              # Uploaded media files
├── manage.py
└── requirements.txt
```
پ

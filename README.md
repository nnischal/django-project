
# 📬 Django Contact Form

A simple "Contact Us" web page built with Django. The form captures user information such as name, email, phone number, and a message, and stores it in a database. The UI is styled using Tailwind CSS.

---

## 🚀 Features

- User-friendly contact form
- Data saved to database via Django ORM
- CSRF-protected form submission
- Minimal styling with Tailwind CSS
- Dynamic success and error messages

---

## 🧱 Tech Stack

- Django (Python Web Framework)
- Tailwind CSS (via CDN)
- SQLite (default Django database)

---

## 📁 Project Structure (Relevant Files)

```
myproject/
├── contact/
│   ├── models.py        # Contact model
│   ├── views.py         # View handling form logic
│   ├── urls.py          # URL routing for contact page
│   └── templates/
│       └── contact.html # Frontend template
├── db.sqlite3
└── manage.py
```

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/django-contact-form.git
cd django-contact-form
```

2. **Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Django**

```bash
pip install django
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

6. **Access the form**

Open your browser and go to:  
`http://127.0.0.1:8000/contact/`

---

## 📌 Contact Model

```python
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
```

---

## 📥 Example Form Submission

- **POST to:** `/contact/`
- **Fields:** `name`, `email`, `phone`, `message`

---

## 📸 Screenshot
![Contact us](https://github.com/user-attachments/assets/b140f58d-e999-497a-8c44-fb17ef20653b)



---



## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Credits

Created by [Nischal Niraula](https://github.com/yourusername)

# Django QRCode Generator

[![PyPI version](https://img.shields.io/pypi/v/django-qrcode.svg?style=flat-square)](https://pypi.org/project/django-qrcode/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/DadaNanjesha/TagGenerator/python-publish.yml?branch=main&style=flat-square)](https://github.com/DadaNanjesha/TagGenerator/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

Welcome to **Django QRCode Generator** : A sleek, reusable Django app that creates stunning, customizable QR codes on the fly. With advanced styling options like rounded modules and radial gradients, you can generate QR codes that are not only functional but also visually appealing.

---

## ✨ Features

- **Dynamic Generation:** Instantly generate QR codes for any text or URL.
- **Advanced Styling:** Beautiful QR codes with rounded modules and gradient colors.
- **Plug-and-Play:** Seamlessly integrate with any Django project.
- **Custom Template Tag:** Easily embed QR codes in your templates using `{% qrcode_url %}`.
- **Responsive UI:** A simple frontend interface for quick testing and demos.

---

## 🚀 Installation

Install the package directly from PyPI:

```bash
pip install django-qrcode
```

---

## ⚡ Quick Start

### 1. Add to Installed Apps

In your Django project's `settings.py`, add **QrCode** to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ... your other apps
    "QrCode",
]
```

### 2. Include URL Configuration

Update your main `urls.py` file to include the QRCode app URLs:

```python
from django.urls import include, path

urlpatterns = [
    # ... your other URL patterns
    path("qrcode/", include("QrCode.urls", namespace="qrcode")),
]
```

### 3. Embed QR Code in Templates

Use the custom template tag to render a QR code in your template:

```django
{% load qrcode_tags %}
<img src="{% qrcode_url 'https://example.com' %}" alt="QR Code">
```

### 4. Try the Demo Frontend

Navigate to the QRCode app’s homepage to see a live demo:

```
http://<your-domain>/qrcode/
```

---

## 🛠 Development & Testing

Clone the repository and set up your development environment:

```bash
git clone https://github.com/yourusername/TagGenerator.git
cd TagGenerator
pip install -r requirements.txt
pip install -e .
```

Run tests with:

```bash
python manage.py test
```

And enjoy continuous integration with our GitHub Actions workflow!

---

## 🚢 Publishing to PyPI

To release a new version:

1. **Tag the Release:**

   ```bash
   git tag v1.0.0
   git push --tags
   ```

2. **Build the Distribution:**

   ```bash
   python setup.py sdist bdist_wheel
   ```

3. **Upload with Twine:**

   ```bash
   twine upload dist/*
   ```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance this project, please check the [issues](https://github.com/yourusername/TagGenerator/issues) and submit a pull request.

---

## 🙏 Acknowledgements

- Built with [Django](https://www.djangoproject.com/) and [qrcode](https://pypi.org/project/qrcode/).
- Inspired by the need for beautiful and integrated QR code solutions in Django.

---

Happy Coding! 🎉
```


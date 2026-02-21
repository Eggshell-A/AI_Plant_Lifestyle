# 植悟 Plantlighten

> 結合 AI 辨識與古老智慧，探索植物的中醫、風水與節慶之美

---

## Project Overview

**Plantlighten** (植悟) is a web application that bridges **artificial intelligence** with **Traditional Chinese Medicine (TCM)** and **Feng Shui** wisdom. Users upload a photo of a plant; the app identifies it and returns:

- **AI plant identification** — Species name and confidence score via the Plant.id API  
- **中醫藥性 (TCM)** — Traditional Chinese medicine properties and usage notes  
- **風水佈局 (Feng Shui)** — Placement and layout suggestions  
- **節慶寓意 (Festive)** — Cultural and festive symbolism  

The project aims to make plant knowledge accessible and to connect modern technology with traditional practices in a single, user-friendly experience.

---

## Tech Stack

| Layer        | Technology |
|-------------|------------|
| **Backend** | Django 4.2 (Python) |
| **Frontend**| HTML5, Bootstrap 5, Bootstrap Icons |
| **Plant ID**| [Plant.id API](https://web.plant.id/) (v3, multipart upload) |
| **Env / HTTP** | python-dotenv, requests |

- **Django** — Routing, views, templates, media handling, admin for plant data  
- **Bootstrap 5** — Responsive UI, cards, forms, navbar, loading overlay  
- **Plant.id API** — Image-based plant identification (scientific name + probability)

---

## Installation Guide

### Prerequisites

- Python 3.10+ (recommended)
- pip (or pip3)

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI_Plant_Lifestyle
```

### 2. Create and activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# or: venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install django python-dotenv requests
```

Optional: create a `requirements.txt` and use:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
Django>=4.2
python-dotenv>=1.0
requests>=2.28
```

### 4. Environment variables

Create a `.env` file in the project root (same level as `manage.py`):

```env
PLANT_ID_API_KEY=your_plant_id_api_key_here
```

Get your API key from [Plant.id](https://web.plant.id/). Do not commit `.env` to version control (it is listed in `.gitignore`).

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. (Optional) Create a superuser for the admin

```bash
python manage.py createsuperuser
```

Use the admin at `/admin/` to add or edit plants (scientific name, common name, TCM / Feng Shui / festive info, and reference images).

### 7. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser. Upload a plant image to see identification and (if the plant exists in your database) TCM, Feng Shui, and festive content.

### 8. Media files (optional)

Reference images for plants are stored under `media/`. For local development, Django serves them when `DEBUG=True` and `core/urls.py` includes the `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` pattern.

---

## Team Members

| Role | Name | Responsibility |
|------|------|----------------|
| *TBD* | *Add names* | *e.g. Backend, Frontend, TCM content, Feng Shui content* |

*Update this section with your team members and roles.*

---

## License

*Add your preferred license (e.g. MIT, proprietary).*

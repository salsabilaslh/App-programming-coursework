# Quotes Analysis Dashboard

## Project Overview

Quotes Analysis Dashboard is an interactive web application for exploring, translating, searching, and analyzing quote data.

This project was developed using:

- Gradio
- FastAPI
- SQLite3
- Pandas
- Matplotlib
- BeautifulSoup
- Hugging Face Spaces

The system provides multilingual translation, quote analytics, visualization charts, dataset exploration, and interactive search functionality through a user-friendly dashboard interface.

---

# Main Features

- Interactive quotes dashboard
- Real-time quote translation
  - Korean 🇰🇷
  - Indonesian 🇮🇩
- Keyword-based quote search
- Word count analysis
- Top authors analysis
- Authors visualization chart
- Random quote generator
- Automatic quote dataset collection
- SQLite database integration
- FastAPI CRUD API
- Interactive Gradio web UI
- Hugging Face deployment

---

# Project Files

| File | Description |
|---|---|
| `app.py` | Main application entry point |
| `ui.py` | Gradio dashboard user interface |
| `main.py` | FastAPI CRUD API |
| `crawler.py` | Automatic quote data collection |
| `database.py` | SQLite database creation and management |
| `quotes.db` | SQLite database file |
| `requirements.txt` | Required Python packages |

---

# Dashboard Features

## Quote Exploration
Users can browse and explore quote datasets through an interactive table interface.

## Multilingual Translation
Selected quotes can be translated into:
- Korean
- Indonesian

## Analytics & Visualization
The system provides:
- Total quotes statistics
- Total authors statistics
- Average words analysis
- Longest quote analysis
- Shortest quote analysis
- Top authors ranking
- Authors visualization chart

## Random Quote Generator
Users can generate random quotes dynamically from the database.

## Search System
Users can search quotes using custom keywords.

---

# Deployment

## Live Demo
https://huggingface.co/spaces/salsabilaslh/app.project

---

# Technologies Used

- Python
- Gradio
- FastAPI
- SQLite3
- Pandas
- Matplotlib
- BeautifulSoup
- Requests

---

# Conclusion

This project successfully combines data exploration, multilingual translation, visualization, and analytics into a single interactive dashboard platform.

By integrating database management, web scraping, translation APIs, and visualization tools, the system provides a practical and user-friendly environment for quote analysis and exploration.

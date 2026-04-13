# **Workshop Booking**

> This website is for coordinators to book a workshop(s), they can book a workshop based on instructors posts or can propose a workshop date based on their convenience.


### Features
* Statistics
    1. Instructors Only
        * Monthly Workshop Count
        * Instructor/Coordinator Profile stats
        * Upcoming Workshops
        * View/Post comments on Coordinator's Profile
    2. Open to All
        * Workshops taken over Map of India
        * Pie chart based on Total Workshops taken to Type of Workshops.

* Workshop Related Features
    > Instructors can Accept, Reject or Delete workshops based on their preference, also they can postpone a workshop based on coordinators request.

__NOTE__: Check docs/Getting_Started.md for more info.

<div align="center">

<img src="workshop_booking_banner.png" width="100%" alt="Workshop Booking Banner">

# 🗓️ Workshop Booking System
### *Modernize. Coordinate. Accelerate.*

[![Django](https://img.shields.io/badge/Django-3.0.7-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4.19-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

**A high-performance coordination platform built for instructors and coordinators to seamlessly manage educational workshops.**

[Key Features](#-key-features) • [Tech Stack](#-tech-stack) • [Installation](#-getting-started) • [Visual Experience](#-visual-experience)

</div>

---

## ✨ Key Features

### 👨‍🏫 For Instructors
- **Dynamic Scheduling:** Post your availability and manage upcoming sessions effortlessly.
- **Advanced Dashboard:** Real-time statistics including monthly workshop counts and performance tracking.
- **Engagement Tools:** View and post comments on coordinator profiles to build strong partnerships.
- **Workflow Management:** Accept, reject, or postpone requests with a single click.

### 🤝 For Coordinators
- **Intelligent Booking:** Book workshops based on instructor availability or propose custom dates.
- **Centralized Proposal System:** Propose workshop dates that suit your organization's schedule.
- **Interactive Profiles:** Manage your reputation and feedback within the community.

### 📊 Open Analytics
- **Geospatial Insights:** Track workshop distribution across the **Map of India**.
- **Data Visualization:** Intuitive pie charts and bar graphs for workshop categories and total engagement.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Backend** | Python / Django (v3.0.7) |
| **Styling** | Tailwind CSS 3.0 (with "Corporate Trust" design system) |
| **Database** | SQLite3 (Default) / Compatible with PostgreSQL/MySQL |
| **Typography** | Plus Jakarta Sans |
| **Data Viz** | Pandas / Plotly / Matplotlib (Integrated) |

---

## 🚀 Getting Started

Follow these steps to deploy the application on your local machine:

### 1️⃣ Prerequisites
- Python 3.x installed.
- Git installed.

### 2️⃣ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/FOSSEE/workshop_booking.git
cd workshop_booking

# Set up virtual environment
python -m venv venv
# On Windows use: venv\Scripts\activate
source venv/bin/activate  

# Install dependencies
pip install -r requirements.txt

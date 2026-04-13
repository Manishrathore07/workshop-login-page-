<div align="center">

<img src="workshop_booking_banner.png" width="100%" alt="Workshop Booking Banner">

# 🗓️ Workshop Booking & Management System
### *Bridging the gap between Educational Expertise and Institutional Coordination.*

[![Django](https://img.shields.io/badge/Django-3.0.7-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4.19-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SQLite/Postgres-blue?style=for-the-badge&logo=sqlite&logoColor=white)]()
[![License](https://img.shields.io/badge/License-ISC-9333ea?style=for-the-badge)]()

**Workshop Booking** is a premium coordination ecosystem designed for large-scale educational initiatives. It enables instructors to showcase expertise and coordinators to organize high-impact learning sessions with architectural precision.

---

[📖 Overview](#-overview) • [🚀 Features](#-key-features) • [🏗️ Architecture](#%EF%B8%8F-architecture) • [🎨 Design System](#-design-system) • [⚙️ Setup](#-installation--getting-started) • [📊 Analytics](#-advanced-analytics)

---

</div>

## 📖 Project Overview

Managing workshops across multiple states and departments requires more than just a calendar—it requires a robust workflow. This platform provides:
- **Scalability:** Handle hundreds of instructors and institutional coordinators simultaneously.
- **Trust:** A role-based verification system ensures only qualified instructors conduct sessions.
- **Insights:** Data-driven dashboards showing regional trends and workshop demographics.

---

## 🚀 Key Features

### 🏢 Institutional Coordinators
*   **Intelligent Proposals:** Propose custom workshop dates based on institutional availability.
*   **Instructor Discovery:** Browse available workshops posted by subject matter experts.
*   **Profile Management:** Build institutional reputation through history and feedback.
*   **Communication:** Direct commenting system on workshop instances for logistical clarity.

### 👨‍🏫 Subject Matter Instructors
*   **Course Catalog:** Create "Workshop Types" with specific durations, prerequisites, and materials.
*   **Request Management:** Intuitive **Accept/Reject/Postpone** dashboard for handling coordinator proposals.
*   **Impact Tracking:** Stats on workshop counts and demographic reach.
*   **Resource Distribution:** Upload schedules and instructional materials directly to workshop types.

### 🌐 Global Features
*   **Interactive Maps:** Visualise workshop distribution across India using geospatial data.
*   **Testimonial Engine:** Showcase impact through participant and coordinator feedback.
*   **Email Verification:** Secure activation flow for new users.

---

## 🏗️ Architecture

The project is built on a modular Django architecture, ensuring separation of concerns:

| App | Responsibility |
| :--- | :--- |
| **`workshop_app`** | Core engine: User profiles, Workshop logic, Commenting, and Banner management. |
| **`statistics_app`** | Data processing: Generates monthly trends and regional heatmaps. |
| **`workshop_portal`** | Project configuration, routing, and global settings. |
| **`teams`** | Management of internal organizational roles and permissions. |
| **`cms`** | Content management for informational pages and dynamic components. |

---

## 🎨 Design System: "Atmospheric Trust"

We have transitioned from legacy Bootstrap to a custom-built **Tailwind CSS 3.0** design system optimized for professional credibility.

### 💠 Visual Tokens
- **Palette:** `Indigo-600` (Primary), `Violet-600` (Secondary), and `Emerald-500` (Accent).
- **Aesthetics:** High-level glassmorphism, glowing button cues, and subtle card shadows (`box-shadow: soft`).
- **Typography:** **Plus Jakarta Sans**—a modern geometric sans-serif for maximum readability.
- **Motion:** Implementation of `fade-in-up` keyframes for page-reveal animations and interactive hover scaling.

---

## ⚙️ Installation & Getting Started

### 1️⃣ Environment Preparation
Ensure you have **Python 3.8+** and **Node.js** (for Tailwind processing) installed.

```bash
# Clone and Enter
git clone https://github.com/FOSSEE/workshop_booking.git
cd workshop_booking

# Virtual Environment Setup
python -m venv venv
# Windows: venv\Scripts\activate | Unix: source venv/bin/activate
source venv/bin/activate

# Core Dependencies
pip install -r requirements.txt

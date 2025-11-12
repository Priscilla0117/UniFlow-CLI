# UniFlow CLI — Role-Based University Ops System

A clean, menu-driven **Python CLI** that streamlines common university operations across **five roles**:
**Administrator, Registrar, Lecturer, Student, Accountant**. Users perform tasks such as student enrolment,
module assignment, grade recording, attendance tracking, and tuition management—persisted in lightweight
**text (CSV-like) files** with strong input validation and robust error handling.

> Why it’s interesting: no external dependencies, no ORM, no OOP—just solid functional design, modular
menus, and careful file I/O for reliability and portability.

---

## ✨ Features (by role)

**Administrator**
- Manage modules (create/update), lecturers, and students
- View all data and generate summary reports

**Registrar**
- Register/update student records
- Manage module enrolments and issue transcript summaries

**Lecturer**
- View assigned modules
- Record grades, track attendance, and view student lists

**Student**
- Browse available modules, enrol/unenrol
- View grades and attendance

**Accountant**
- Record payments, list outstanding fees
- Issue fee receipts and view financial summaries

> All data is stored in `.txt` files using simple comma-separated lines for portability.

---

## 🏗️ Architecture & Design

- **Language:** Python 3.x (standard library only)
- **Paradigm:** Functional, menu-driven 
- **Storage:** Text files (CSV-like lines), read/write via `open()`
- **Menus:** Role-based navigation via `while` loops + `if/elif` routes
- **Validation:** Strict input checks for IDs, duplicates, numeric values, ranges
- **Error Handling:** `try/except` for file I/O and input parsing
- **Reports:** Aggregations (counts, summaries, fee totals, outstanding balances)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ installed and on your PATH

### Setup
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python src/main.py

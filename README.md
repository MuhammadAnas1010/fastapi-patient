# 🏥 FastAPI Patient Management System

This is a simple FastAPI project that demonstrates basic CRUD operations, file upload functionality, and JSON storage using Python. It simulates a small patient database and allows interaction through HTTP endpoints.

---

## 📁 Project Structure

fastapi_git/
├── main.py # Main FastAPI application
├── patients.json # Mock database (JSON file)
├── README.md # Documentation
├── requirements.txt # Python dependencies
└── uploads/ # Folder to store uploaded files (auto-created)

---

## 🚀 Features

- ✅ Get patient by ID (path param)
- ✅ Get selected patient details (query param)
- ✅ Add a new patient using JSON + Pydantic validation
- ✅ Upload a file (image or document)
- ✅ Error handling with proper HTTP status codes

---

## 🧪 API Endpoints

### 1. `GET /patients/{patient_id}`

Returns full patient record by ID.

**Example:**  
`GET /patients/2`

---

### 2. `GET /patient_detail?patient_id=2&detail=name&detail=age`

Returns only selected patient fields.

**Example:**  
`GET /patient_detail?patient_id=2&detail=name&detail=gender`

---

### 3. `POST /new_patient`

Add a new patient with JSON body:
```json
{
  "id": 11,
  "name": "John Doe",
  "age": 30,
  "gender": "male",
  "diagnosis": "Flu"
}
---
🧰 Setup Instructions
🔧 Prerequisites
Python 3.8+

pip

Virtual environment (recommended)

Install Dependencies

python -m venv venv
venv/Scripts/activate

pip install -r requirements.txt

▶️ Run the Server
uvicorn main:app --reload

🗃️ Git and GitHub Basics
What is Git?
Git is a version control system that lets you track changes to your code, collaborate with others, and roll back to previous versions.

What is GitHub?
GitHub is a cloud-based platform to host Git repositories online, allowing others to view, clone, and contribute.

| Concept          | What it Means                                           |
| ---------------- | ------------------------------------------------------- |
| **Commit**       | Save a snapshot of changes to your project              |
| **Push**         | Upload your commits to GitHub                           |
| **Pull**         | Download latest changes from GitHub                     |
| **Branch**       | A separate version of your code for testing or features |
| **Merge**        | Combine changes from one branch into another            |
| **Pull Request** | Ask to merge your branch into main project              |
| **Stash**        | Temporarily save changes without committing             |


🖥️ GitHub Desktop Instructions
Open GitHub Desktop.

Clone your GitHub repo or create a new one.

Use "Fetch origin" to pull latest updates.

Make changes locally and commit.

Click "Push origin" to sync with GitHub.

Create branches for new features.

Use pull requests to merge them.

📁 .gitignore
__pycache__/
venv/
*.pyc
.env
uploads/
---
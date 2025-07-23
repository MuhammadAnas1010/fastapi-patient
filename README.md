# 🏥 FastAPI Patient Management System

This is a simple **FastAPI** project that demonstrates:

- Basic CRUD operations  
- File upload functionality  
- JSON-based storage  
- Pydantic validation  
- Error handling

It simulates a small patient database using a `patients.json` file and allows interaction through HTTP endpoints via Swagger UI.

---

## 🗂 Project Structure

fastapi_git/
│
├── main.py # Main FastAPI application
├── patients.json # Mock patient database
├── requirements.txt # Python dependencies
├── README.md # Documentation (you are here)
└── uploads/ # Folder to store uploaded files (auto-created)
---


## 🚀 Features

- ✅ Get full patient record by ID  
- ✅ Get selected patient fields using query parameters  
- ✅ Add a new patient using JSON + Pydantic validation  
- ✅ Upload a file (image or document)  
- ✅ Proper error handling with HTTPException  

---

## 🔗 API Endpoints

### 📘 Get Patient by ID
GET /patients/{patient_id}
Description: Returns full patient record by ID
Example: /patients/2

📘 Get Selected Patient Details
GET /patient_detail?patient_id=2&detail=name&detail=gender
Description: Returns selected fields of a patient
Query Params: patient_id, detail (can be multiple)

📘 Add New Patient
POST /new_patient

📘 Upload File
POST /uploadfile/

🧰 Setup Instructions
📦 Prerequisites
Python 3.8+

pip

💻 Install & Run

python -m venv venv


# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn main:app --reload

🧠 Git & GitHub Basics
| Term         | Meaning                                                           |
| ------------ | ----------------------------------------------------------------- |
| Commit       | Save a snapshot of your project                                   |
| Push         | Upload your local commits to GitHub                               |
| Pull         | Download latest commits from GitHub                               |
| Branch       | Create a separate version of your project for new features        |
| Merge        | Combine different branches together                               |
| Pull Request | Propose changes from one branch to another (often to main/master) |
| Stash        | Temporarily save uncommitted changes                              |

🖥️ GitHub Desktop Instructions
Open GitHub Desktop

Clone or create your GitHub repo

Add your local files

Make changes → Commit → Push origin

Create branches for new features and merge using pull requests

⚠️ .gitignore Suggestions
Add these to your .gitignore file to avoid uploading sensitive or unnecessary files:

__pycache__/
venv/
*.pyc
.env
uploads/

Made by Muhammad Anas
🔗 GitHub: @MuhammadAnas1010



---

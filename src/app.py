"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["alex@mergington.edu", "chris@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join the school basketball team and compete in matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["jordan@mergington.edu", "taylor@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various forms of art and create your own masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["lily@mergington.edu", "james@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in plays and improve your acting skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["sarah@mergington.edu", "david@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop your public speaking and argumentation skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    # Validar se o aluno já está inscrito
    if email in activity["participants"]:
        return {"message": f"{email} is already signed up for {activity_name}"}
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

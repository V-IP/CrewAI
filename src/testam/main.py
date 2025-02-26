#!/usr/bin/env python
# import sys
import json
import os
from testam.crew import (
    TestamCrew,
)

# import warnings

# from datetime import datetime

# from testam.crew import TestamCrew

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

ROOMS_FILE = "rooms.json"
DORMS_FILE = "dorms.json"

def load_data(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def update_rooms(rooms, assigned_room, student):
    if assigned_room in rooms and len(rooms[assigned_room]) < 2:
        rooms[assigned_room].append(student)
    return rooms
def run():
    """
    Run the crew.
    """
    dorms = load_data(DORMS_FILE)
    rooms = load_data(ROOMS_FILE)

    student_profile = "Eve is very social and loves to party late at night."

    inputs = {
        "dorm_list": dorms,
        "room_assignments": rooms,
        "student_profile": student_profile 
    }
    
    TestamCrew().crew().kickoff(inputs=inputs)
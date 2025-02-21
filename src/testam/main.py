#!/usr/bin/env python
import sys
import warnings
import json
import os

from datetime import datetime

from testam.crew import Testam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
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
    
    try:
        Testam().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Testam().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Testam().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Testam().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

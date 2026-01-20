import sys
import os

# MANDATORY: Tells Python to look for modules in the current folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.junction import Junction
from engine import SmartEngine

def start_system():
    # Initialize OOP Objects
    my_junction = Junction("Main St & 5th Ave")
    brain = SmartEngine(my_junction)
    
    # Simulate 3 cycles of traffic
    for i in range(1, 4):
        print(f"\n--- CYCLE {i} ---")
        brain.process()

if __name__ == "__main__":
    start_system()
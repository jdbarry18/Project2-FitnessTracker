import os
from project2gui import FitnessTrackerGUI
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_name = 'FitnessTracker.txt'
file_path = os.path.join(desktop_path, file_name)
workout_data = {}
class WorkoutTracker:
    def __init__(self):
        self.workouts = []


def save_data_to_file(data):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass
    with open(file_path, 'a') as file:
        if 'day' in data:
            file.write(f"Day: {data['day']}\n")
        file.write(str(data) + '\n')

def add_separator_to_file():
    with open(file_path, 'a') as file:
        file.write('================================================\n')

def main():
    app = FitnessTrackerGUI(workout_data, save_data_to_file, add_separator_to_file)
    app.run()

if __name__ == '__main__':
    main()
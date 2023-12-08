import tkinter as tk
from tkinter import messagebox

class FitnessTrackerGUI:
    def __init__(self, workout_data: dict, save_data_callback, add_separator_callback):
        self.workout_data = workout_data
        self.save_data_callback = save_data_callback
        self.add_separator_callback = add_separator_callback
        self.root = tk.Tk()
        self.root.geometry('320x360')
        self.root.title('FitnessTracker')
        self.create_first_page()

    def create_first_page(self):
        welcome_label = tk.Label(self.root, text="Welcome to FitnessTracker.\nPlease enter the day of your workout.")
        welcome_label.pack(side='top', fill='x', pady=10)

        self.day_entry = tk.Entry(self.root)
        self.day_entry.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(side='bottom', pady=10)

        exit_button = tk.Button(button_frame, text='Exit', command=self.exit_application)
        exit_button.pack(side='left')

        next_button = tk.Button(button_frame, text='Next', command=self.validate_day)
        next_button.pack(side='right')

    def validate_day(self):
        try:
            day = int(self.day_entry.get())
            self.workout_data['day'] = day
            self.save_data_callback({'day': day})
            self.create_second_page()
        except ValueError:
            messagebox.showerror('Error', 'Please enter a number.')

    def create_second_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        button_frame = tk.Frame(self.root)
        button_frame.pack(side='bottom', pady=10)

        exit_button = tk.Button(button_frame, text='Exit', command=self.exit_application)
        exit_button.pack(side='left')

        view_button = tk.Button(button_frame, text='View', command=self.view_workout_day)
        view_button.pack(side='right')

        weigh_in_button = tk.Button(self.root, text='Weigh In', command=self.weigh_in_page)
        workouts_button = tk.Button(self.root, text='Workouts', command=self.workouts_page)
        nutrition_button = tk.Button(self.root, text='Nutrition', command=self.nutrition_page)

        weigh_in_button.pack(fill='x', pady=5)
        workouts_button.pack(fill='x', pady=5)
        nutrition_button.pack(fill='x', pady=5)

    def view_workout_day(self):
        content = '\n'.join(f'{key}: {value}' for key, value in self.workout_data.items())
        messagebox.showinfo('Workout Day', content)

    def weigh_in_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        weigh_in_label = tk.Label(self.root, text="Enter your weight")
        weigh_in_label.pack(side='top', fill='x', pady=10)

        morning_weight_label = tk.Label(self.root, text="Morning weight:")
        morning_weight_label.pack()
        self.morning_weight_entry = tk.Entry(self.root)
        self.morning_weight_entry.pack()

        evening_weight_label = tk.Label(self.root, text="Evening weight:")
        evening_weight_label.pack()
        self.evening_weight_entry = tk.Entry(self.root)
        self.evening_weight_entry.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(side='bottom', pady=10)

        back_button = tk.Button(button_frame, text='Back', command=self.create_second_page)
        back_button.pack(side='left')

        save_button = tk.Button(button_frame, text='Save', command=self.save_weights)
        save_button.pack(side='right')

    def save_weights(self):
        try:
            morning_weight = float(self.morning_weight_entry.get())
            evening_weight = float(self.evening_weight_entry.get())
            self.workout_data['morning_weight'] = morning_weight
            self.workout_data['evening_weight'] = evening_weight
            self.save_data_callback({'morning_weight': morning_weight, 'evening_weight': evening_weight})
            messagebox.showinfo('Success', 'Weights saved successfully.')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a number.')

    def workouts_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        workout_label = tk.Label(self.root, text="Enter your workout")
        workout_label.pack(side='top', fill='x', pady=10)

        exercise_label = tk.Label(self.root, text="Exercise:")
        exercise_label.pack()
        self.exercise_entry = tk.Entry(self.root)
        self.exercise_entry.pack()

        sets_label = tk.Label(self.root, text="Sets:")
        sets_label.pack()
        self.sets_entry = tk.Entry(self.root)
        self.sets_entry.pack()

        reps_label = tk.Label(self.root, text="Reps:")
        reps_label.pack()
        self.reps_entry = tk.Entry(self.root)
        self.reps_entry.pack()

        weight_label = tk.Label(self.root, text="Weight:")
        weight_label.pack()
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(side='bottom', pady=10)

        back_button = tk.Button(button_frame, text='Back', command=self.create_second_page)
        back_button.pack(side='left')

        save_button = tk.Button(button_frame, text='Save', command=self.save_workout)
        save_button.pack(side='right')

    def save_workout(self):
        try:
            exercise = self.exercise_entry.get()
            sets = int(self.sets_entry.get())
            reps = int(self.reps_entry.get())
            weight = float(self.weight_entry.get())
            self.workout_data['exercise'] = {
                'exercise': exercise,
                'sets': sets,
                'reps': reps,
                'weight': weight
            }
            self.save_data_callback(self.workout_data['exercise'])
            messagebox.showinfo('Success', 'Workout saved successfully.')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers for sets, reps, and weight.')

    def nutrition_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        nutrition_label = tk.Label(self.root, text="Enter your meal's nutritional information")
        nutrition_label.pack(side='top', fill='x', pady=10)

        meal_number_label = tk.Label(self.root, text="Meal#:")
        meal_number_label.pack()
        self.meal_number_entry = tk.Entry(self.root)
        self.meal_number_entry.pack()

        meal_label = tk.Label(self.root, text="Meal:")
        meal_label.pack()
        self.meal_entry = tk.Entry(self.root)
        self.meal_entry.pack()

        protein_label = tk.Label(self.root, text="Protein:")
        protein_label.pack()
        self.protein_entry = tk.Entry(self.root)
        self.protein_entry.pack()

        carbs_label = tk.Label(self.root, text="Carbohydrates:")
        carbs_label.pack()
        self.carbs_entry = tk.Entry(self.root)
        self.carbs_entry.pack()

        fat_label = tk.Label(self.root, text="Fat:")
        fat_label.pack()
        self.fat_entry = tk.Entry(self.root)
        self.fat_entry.pack()

        sugar_label = tk.Label(self.root, text="Sugar:")
        sugar_label.pack()
        self.sugar_entry = tk.Entry(self.root)
        self.sugar_entry.pack()

        calories_label = tk.Label(self.root, text="Calories:")
        calories_label.pack()
        self.calories_entry = tk.Entry(self.root)
        self.calories_entry.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack(side='bottom', pady=10)

        back_button = tk.Button(button_frame, text='Back', command=self.create_second_page)
        back_button.pack(side='left')

        save_button = tk.Button(button_frame, text='Save', command=self.save_nutrition)
        save_button.pack(side='right')

    def save_nutrition(self):
        try:
            meal_number = int(self.meal_number_entry.get())
            meal = self.meal_entry.get()
            protein = float(self.protein_entry.get())
            carbs = float(self.carbs_entry.get())
            fat = float(self.fat_entry.get())
            sugar = float(self.sugar_entry.get())
            calories = int(self.calories_entry.get())
            self.workout_data['nutrition'] = {
                'meal_number': meal_number,
                'meal': meal,
                'protein': protein,
                'carbs': carbs,
                'fat': fat,
                'sugar': sugar,
                'calories': calories
            }
            self.save_data_callback(self.workout_data['nutrition'])
            messagebox.showinfo('Success', 'Nutritional information saved successfully.')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers for protein, carbs, fat, sugar, and calories.')

    def exit_application(self):
        self.add_separator_callback()
        self.root.quit()

    def run(self):
        self.root.mainloop()
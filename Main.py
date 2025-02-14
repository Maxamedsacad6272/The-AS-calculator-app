import tkinter as tk
from tkinter import messagebox

# Function to calculate the area of the sector
def calculate_area(theta, radius):
    try:
        theta = float(theta)
        radius = float(radius)
        area = (theta / 360) * 3.14159 * (radius ** 2)
        return round(area, 2)
    except ValueError:
        return None

# Function for the step-by-step tutorial
def tutorial(theta, radius):
    steps = f"1. Use the formula: Area = (θ / 360) * π * r²\n"
    steps += f"2. Plug in the values: θ = {theta}°, r = {radius}\n"
    steps += f"3. Calculate: Area = ({theta} / 360) * π * ({radius}²)\n"
    area = calculate_area(theta, radius)
    steps += f"4. Result: Area = {area}"
    return steps

# Main application class
class SectorCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sector Area Calculator")
        self.create_menu()

    def create_menu(self):
        self.clear_frame()
        menu_label = tk.Label(self.root, text="Sector Area Calculator", font=("Arial", 16), bg="yellow", relief="ridge")
        menu_label.pack(pady=20, ipadx=10, ipady=5)

        question_button = tk.Button(self.root, text="Questions Part", command=self.questions_part, bg="yellow")
        question_button.pack(pady=10)

        calculator_button = tk.Button(self.root, text="Calculator Part", command=self.calculator_part, bg="yellow")
        calculator_button.pack(pady=10)

    def questions_part(self):
        self.clear_frame()
        back_button = tk.Button(self.root, text="Back", command=self.create_menu)
        back_button.pack(anchor="nw", padx=10, pady=10)

        question_label = tk.Label(self.root, text="Find the area of the sector:", font=("Arial", 14), bg="yellow")
        question_label.pack(pady=20)

        # Generate a sample question
        theta = 60
        radius = 5
        answer = calculate_area(theta, radius)
        question_text = f"Given θ = {theta}°, r = {radius}"
        tk.Label(self.root, text=question_text, font=("Arial", 12)).pack(pady=10)

        self.answer_input = tk.Entry(self.root, font=("Arial", 12))
        self.answer_input.pack(pady=5)

        def check_answer():
            user_answer = self.answer_input.get()
            if not user_answer:
                messagebox.showinfo("Result", "Please enter an answer!")
            elif float(user_answer) == answer:
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", f"Incorrect! The correct answer is {answer}.")

        confirm_button = tk.Button(self.root, text="Confirm Answer", command=check_answer, bg="yellow")
        confirm_button.pack(pady=10)

    def calculator_part(self):
        self.clear_frame()
        back_button = tk.Button(self.root, text="Back", command=self.create_menu)
        back_button.pack(anchor="nw", padx=10, pady=10)

        tk.Label(self.root, text="Enter θ (in degrees):", font=("Arial", 12)).pack(pady=5)
        theta_input = tk.Entry(self.root, font=("Arial", 12))
        theta_input.pack(pady=5)

        tk.Label(self.root, text="Enter radius:", font=("Arial", 12)).pack(pady=5)
        radius_input = tk.Entry(self.root, font=("Arial", 12))
        radius_input.pack(pady=5)

        result_label = tk.Label(self.root, font=("Arial", 12), fg="blue")
        result_label.pack(pady=10)

        def calculate():
            theta = theta_input.get()
            radius = radius_input.get()
            area = calculate_area(theta, radius)
            if area is None:
                messagebox.showerror("Error", "Please enter valid numeric values!")
            else:
                result_label.config(text=f"Area: {area}")
                if tutorial_checkbox_var.get():
                    steps = tutorial(theta, radius)
                    messagebox.showinfo("Tutorial", steps)

        tutorial_checkbox_var = tk.BooleanVar()
        tutorial_checkbox = tk.Checkbutton(self.root, text="Show tutorial", variable=tutorial_checkbox_var)
        tutorial_checkbox.pack(pady=5)

        calculate_button = tk.Button(self.root, text="Calculate", command=calculate, bg="yellow")
        calculate_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the application
root = tk.Tk()
root.geometry("400x400")
app = SectorCalculatorApp(root)
root.mainloop()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')

def calculate_area(theta, radius):
    try:
        theta = float(theta)
        radius = float(radius)
        area = (theta / 360) * 3.14159 * (radius ** 2)
        return round(area, 2)
    except ValueError:
        return None

def tutorial(theta, radius):
    steps = f"1. Use the formula: Area = (θ / 360) * π * r²\n"
    steps += f"2. Plug in the values: θ = {theta}°, r = {radius}\n"
    steps += f"3. Calculate: Area = ({theta} / 360) * π * ({radius}²)\n"
    area = calculate_area(theta, radius)
    steps += f"4. Result: Area = {area}"
    return steps

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        title = Label(text='Sector Area Calculator', font_size=24, size_hint=(1, 0.2))
        layout.add_widget(title)
        
        questions_btn = Button(text='Questions Part', size_hint=(1, 0.3), 
                             background_color=(1, 1, 0, 1), background_normal='')
        questions_btn.bind(on_press=self.go_to_questions)
        layout.add_widget(questions_btn)
        
        calculator_btn = Button(text='Calculator Part', size_hint=(1, 0.3), 
                               background_color=(1, 1, 0, 1), background_normal='')
        calculator_btn.bind(on_press=self.go_to_calculator)
        layout.add_widget(calculator_btn)
        
        self.add_widget(layout)
    
    def go_to_questions(self, instance):
        self.manager.current = 'question'
    
    def go_to_calculator(self, instance):
        self.manager.current = 'calculator'

class QuestionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        back_btn = Button(text='Back', size_hint=(None, None), size=(100, 50),
                         background_normal='')
        back_btn.bind(on_press=self.go_back)
        self.layout.add_widget(back_btn)
        
        self.question_label = Label(text='Find the area of the sector:', 
                                   font_size=20, size_hint=(1, 0.2))
        self.layout.add_widget(self.question_label)
        
        self.theta = 60
        self.radius = 5
        self.correct_answer = calculate_area(self.theta, self.radius)
        
        self.question_text_label = Label(text=f"Given θ = {self.theta}°, r = {self.radius}", 
                                        font_size=16)
        self.layout.add_widget(self.question_text_label)
        
        self.answer_input = TextInput(hint_text='Enter your answer', 
                                     size_hint=(1, 0.2), font_size=20, 
                                     multiline=False)
        self.layout.add_widget(self.answer_input)
        
        confirm_btn = Button(text='Confirm Answer', size_hint=(1, 0.3), 
                            background_color=(1, 1, 0, 1), background_normal='')
        confirm_btn.bind(on_press=self.check_answer)
        self.layout.add_widget(confirm_btn)
        
        self.add_widget(self.layout)
    
    def on_pre_enter(self, *args):
        self.answer_input.text = ''
    
    def go_back(self, instance):
        self.manager.current = 'menu'
    
    def check_answer(self, instance):
        user_answer = self.answer_input.text
        if not user_answer:
            self.show_popup("Result", "Please enter an answer!")
        else:
            try:
                user_num = float(user_answer)
                if user_num == self.correct_answer:
                    msg = "Correct!"
                else:
                    msg = f"Incorrect! The correct answer is {self.correct_answer}."
                self.show_popup("Result", msg)
            except ValueError:
                self.show_popup("Error", "Please enter a valid number.")
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), 
                     size_hint=(0.8, 0.4))
        popup.open()

class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        back_btn = Button(text='Back', size_hint=(None, None), size=(100, 50),
                         background_normal='')
        back_btn.bind(on_press=self.go_back)
        self.layout.add_widget(back_btn)
        
        theta_label = Label(text="Enter θ (in degrees):", font_size=16)
        self.layout.add_widget(theta_label)
        self.theta_input = TextInput(hint_text='Theta', font_size=20, 
                                    multiline=False)
        self.layout.add_widget(self.theta_input)
        
        radius_label = Label(text="Enter radius:", font_size=16)
        self.layout.add_widget(radius_label)
        self.radius_input = TextInput(hint_text='Radius', font_size=20, 
                                     multiline=False)
        self.layout.add_widget(self.radius_input)
        
        self.tutorial_checkbox = CheckBox(size_hint=(None, None), size=(50, 50))
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        checkbox_layout.add_widget(Label(text="Show tutorial:"))
        checkbox_layout.add_widget(self.tutorial_checkbox)
        self.layout.add_widget(checkbox_layout)
        
        self.result_label = Label(text="Area: ", font_size=20, color=(0, 0, 1, 1))
        self.layout.add_widget(self.result_label)
        
        calc_btn = Button(text='Calculate', size_hint=(1, 0.3), 
                         background_color=(1, 1, 0, 1), background_normal='')
        calc_btn.bind(on_press=self.calculate)
        self.layout.add_widget(calc_btn)
        
        self.add_widget(self.layout)
    
    def go_back(self, instance):
        self.manager.current = 'menu'
    
    def calculate(self, instance):
        theta = self.theta_input.text
        radius = self.radius_input.text
        area = calculate_area(theta, radius)
        if area is None:
            self.show_popup("Error", "Please enter valid numeric values!")
        else:
            self.result_label.text = f"Area: {area}"
            if self.tutorial_checkbox.active:
                steps = tutorial(theta, radius)
                self.show_tutorial_popup(steps)
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), 
                     size_hint=(0.8, 0.4))
        popup.open()
    
    def show_tutorial_popup(self, steps):
        scroll = ScrollView()
        tutorial_label = Label(text=steps, size_hint_y=None, font_size=16)
        tutorial_label.bind(texture_size=lambda instance, size: setattr(tutorial_label, 'height', size[1]))
        scroll.add_widget(tutorial_label)
        popup = Popup(title='Tutorial', content=scroll, size_hint=(0.9, 0.9))
        popup.open()

class SectorCalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(QuestionScreen(name='question'))
        sm.add_widget(CalculatorScreen(name='calculator'))
        return sm

if __name__ == '__main__':
    SectorCalculatorApp().run()

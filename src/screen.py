import PySimpleGUI as sg


class PythonScreen:
    def __init__(self):
        # Change color layout
        sg.change_look_and_feel('Default')
        # Layout
        layout = [
            [sg.Text('Name', size=(5, 0)), sg.Input(size=(15, 0), key='name')],
            [sg.Text('Age', size=(5, 0)), sg.Input(size=(15, 0), key='age')],
            [sg.Text("Which email providers are accepted?")],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text("Accept credit card")],
            [sg.Radio('Yes', 'Cards', key='accept_credit_card'), sg.Radio('No', 'Cards', key='not_accept_credit_card')],
            [sg.Slider(range=(0, 100), default_value=0, orientation='h', size=(15, 20), key='slider_velocity')],
            [sg.Button("Send Data")],
            [sg.Output(size=(30, 20))]
        ]
        # Window
        self.window = sg.Window("User Data").layout(layout)

    def Start(self):
        while True:
            # Extract screen data
            self.button, self.values = self.window.Read()
            name = self.values['name']
            age = self.values['age']
            accept_gmail = self.values['gmail']
            accept_outlook = self.values['outlook']
            accept_yahoo = self.values['yahoo']
            accept_credit_card = self.values['accept_credit_card']
            not_accept_credit_card = self.values['not_accept_credit_card']
            script_velocity = self.values['slider_velocity']
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Accept gmail: {accept_gmail}")
            print(f"Accept outlook: {accept_outlook}")
            print(f"Accept yahoo: {accept_yahoo}")
            print(f"Accept credit card: {accept_credit_card}")
            print(f"Does not accept credit card: {not_accept_credit_card}")
            print(f"Script velocity: {script_velocity}")
            print('-' * 30)


screen = PythonScreen()
screen.Start()

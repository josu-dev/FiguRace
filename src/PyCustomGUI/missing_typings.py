import PySimpleGUI as sg

ElementLayout = list[
    list[
        sg.Element | sg.Column | sg.Text | sg.Button | sg.Input | sg.Multiline
    ]
]

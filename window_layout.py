import PySimpleGUI as sg

chord_list_combo_values = ["Major","Minor","Seventh"]
chord_count_list = [2,3,4,5]
layout = [
      [sg.Combo(values=chord_list_combo_values,default_value=chord_list_combo_values[0],readonly=True,key="CHORDLIST"),
       sg.Combo(values=chord_count_list,default_value=chord_count_list[0],readonly=True,key="COMBOCOUNT"), 
       sg.Button("Generate")],
      [sg.Image(data='', key='-IMAGE1-'),
      sg.Image(data='', key='-IMAGE2-'),
      sg.Image(data='', key='-IMAGE3-'),
      sg.Image(data='', key='-IMAGE4-'),
      sg.Image(data='', key='-IMAGE5-')]
]
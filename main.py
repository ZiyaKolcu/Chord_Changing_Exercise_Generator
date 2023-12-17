import PySimpleGUI as sg
from window_layout import layout
from window_update import window_update

def main():
   sg.theme("BluePurple")
   window = sg.Window("Chord Changing Exercise Generator", layout, finalize=True, size=(600,200))
   window_update(window, "Major", 2)
   
   while True:
      event, values = window.read()

      if event == sg.WINDOW_CLOSED:
         break
      if event == "Generate":
         dir = values["CHORDLIST"]
         count = values["COMBOCOUNT"]
         window_update(window, dir, count)

   window.close()

if __name__ == "__main__":
   main()

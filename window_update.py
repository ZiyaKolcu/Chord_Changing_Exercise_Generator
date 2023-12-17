from chord_image_loader import chord_image_loader
from chord_image_convert import convert_to_tk_image

def window_update(window,dir,count):
   for i in range(1,6):
      window[f'-IMAGE{i}-'].update("")

   chord_image_list = chord_image_loader(dir)
   for i in range(1,count+1):
      window[f'-IMAGE{i}-'].update(data=convert_to_tk_image(chord_image_list[i-1]))
   
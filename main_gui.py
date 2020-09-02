import PySimpleGUI as sg
# import PySimpleGUIQt as sg
import os.path
import PIL.Image
import io
#import imutils
import requests
import base64
import json
import base64
from detect_face_video  import main
"""

"""

plate='f'
Brand='l'
year='0'
Color='b'
def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def update_plate(filename):

        SECRET_KEY = 'sk_ed3d203bf4c9a7c2910ec0c0'

        with open(filename, 'rb') as image_file:
            img_base64 = base64.b64encode(image_file.read())

        url = 'https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
        r = requests.post(url, data = img_base64)



        try:
             global plate
             plate=r.json()['results'][0]['plate'],
             global Brand
             Brand= r.json()['results'][0]['vehicle']['make_model'][0]['name'],
             global Color
             Color=  r.json()['results'][0]['vehicle']['color'][0]['name'],
             global year
             year =  r.json()['results'][0]['vehicle']['year'][0]['name'],
             print(plate)

        except:
              print ('error')

# --------------------------------- Define Layout ---------------------------------

# First the window layout...2 columns

sg.theme('Dark Blue 3')
left_col = [[sg.Text('Folder'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
            [sg.Listbox(values=[], enable_events=True, size=(40,20),key='-FILE LIST-')],
            [sg.Text('Resize to'), sg.In(key='-W-', size=(5,1)), sg.In(key='-H-', size=(5,1))],
            [sg.Button("Resize", button_color=("white", "blue"), size=(6, 1))]]

# For now will only show the name of the file that was chosen
images_col = [[sg.Text('You choose from the list:')],
              [sg.Text(size=(40,1), key='-TOUT-')],
              [sg.Image(key='-IMAGE-')]]

# ----- Full layout -----
layout = [[sg.Column(left_col, element_justification='c'),  sg.VSeperator(),sg.Column(images_col, element_justification='c')]]


# --------------------------------- Create Window ---------------------------------
window = sg.Window('Multiple Format Image Viewer', layout,resizable=True)

# ----- Run the Event Loop -----
# --------------------------------- Event Loop ---------------------------------
while True:
    event, values = window.read()


    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-FOLDER-':                         # Folder name was filled in, make a list of files in the folder
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)         # get list of files in folder
        except:
            file_list = []
        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
        window['-FILE LIST-'].update(fnames)
    if event == 'Resize':
        window['-IMAGE-'].update(data=convert_to_bytes(filename, resize=new_size))
    elif event == '-FILE LIST-':    # A file was chosen from the listbox
        try:
            filename = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])

            window['-TOUT-'].update(filename)


            if values['-W-'] and values['-H-']:
                new_size = int(values['-W-']), int(values['-H-'])

            else:
                new_size = None

            window['-IMAGE-'].update(data=convert_to_bytes(filename, resize=new_size))

            main(filename)
            update_plate(filename)
            sg.Popup("license plate" , plate , "color " , Color , "year ",  year ,"brand " , Brand , keep_on_top=True)

            print(plate)
        except Exception as E:
            print(f'** Error {E} **')
            pass        # something weird happened making the full filename
# --------------------------------- Close & Exit ---------------------------------
window.close()

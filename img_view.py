# img_view.py

# import the PySimpleGUI and os.path modules
import PySimpleGUI as wg
import os.path

# define the layout for the window
file_list_column = [
    # add a Text widget and an Input widget for the folder name, and a FolderBrowse widget for browsing for a folder
    [
        wg.Text("Image Folder"),
        wg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        wg.FolderBrowse(),
    ],
    # add a Listbox widget to display the list of files
    [
        wg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key="-FILE LIST-"
        )
    ],
]

image_viewer_column = [
    # add a Text widget to display a prompt
    [wg.Text("Choose an image from the list on the left:")],
    # add a Text widget to display the file name
    [wg.Text(size=(40, 1),  key="-TOUT-")],
    # add an Image widget to display the image
    [wg.Image(key="-IMAGE-")],
]

# layout the window with two columns
layout = [
    [
        wg.Column(file_list_column),
        wg.VSeperator(),
        wg.Column(image_viewer_column),
    ]
]

# create the window
window = wg.Window("Image Viewer", layout)

# event loop
while True:
    # read an event and its values from the window
    event, values = window.read()
    # if the event is the "Exit" event or the window is closed, break out of the loop
    if event == "Exit" or event == wg.WIN_CLOSED:
        break
    # if the event is the "-FOLDER-" event (the folder name was filled in), make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # get the list of files in the folder
            file_list = os.listdir(folder)
        except:
            file_list = []
            
        # create a list of file names that are in the file_list and are either PNG or GIF files
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        # update the "-FILE LIST-" widget with the list of file names
        window["-FILE LIST-"].update(fnames)
    # if a file was chosen from the list
    elif event == "-FILE LIST-":
        try:
            # if "-FILE LIST-" is in the values dictionary
            if "-FILE LIST-" in values:
                # join the folder name and the file name to get the full file path
                filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
                )
            # update the "-TOUT-" widget with the file name
            window["-TOUT-"].update(filename)
            # update the "-IMAGE-" widget with the image file
            window["-IMAGE-"].update(filename=filename)

        except:
            pass
# close the window
window.close()
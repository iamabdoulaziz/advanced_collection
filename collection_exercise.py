# Collections : Lists / Tuples
# Exercise "Extract extensions"

_field = [input("file here :"), "notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacations.jpeg", "planning", "data.dat"]

extensions_definition = (
    ("doc", "Document Word"),
    ("exe", "Executable"),
    ("txt", "Document Texte"),
    ("jpeg", "Image JPEG")
)
"""
 Final result : 
 notepad.exe (Executable)
 mon.fichier.perso.doc (Document Word)
 notes.TXT (Document Texte)
 vacances.jpeg (Image JPEG)
 planing (Aucune extension)
 data.dat (Extension non connue)
"""

def extract_extensions(_list):
    extensions = []
    e_indexs = []
    for e in _list:
        extension = e.split(".")[-1]
        e_index = _field.index(e)
        e_indexs.append(e_index)
        extensions.append(extension)
    return e_indexs, extensions


"""
def find_extensions(_list):
    for element in _list:
        lower_element = element.lower()
        if "exe" in lower_element:
            print(f"{lower_element} (Executable)")
        elif "doc" in lower_element:
            print(f"{lower_element} (Document Word)")
        elif "txt" in lower_element:
            print(f"{lower_element} (Document Texte)")
        elif "jpeg" in lower_element:
            print(f"{lower_element} (Image JPEG)")
        elif not any(ext in lower_element for ext in ["exe", "doc", "txt", "jpeg"] ):
            print(f"{lower_element} (Aucune extension)")
        else:
            print(f"{lower_element} (Extension non connue)")
"""

#print(extract_extensions(_field))

def new_function(_list):
    for element in _list:
        lower_element = element.lower()
        split_element = lower_element.split(".")[-1]
        found = False

        for ext, definition in extensions_definition:
            if split_element == ext:
                print(f"{element} | {definition}")
                found = True
                break

        if not found:
            if "." not in element:
                print(f"{element} | Aucune extension")
            else:
                print(f"{element} | Extension inconnue")


new_function(_field)

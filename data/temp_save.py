import flet as fl
import json
from dataclasses import asdict
from data.resources import ClassGroup, Human, Object, Place

# ╔¤═══════¤VARIABLES TEMPORALES¤════════¤╗
projecto_name = "Nuevo Proyecto"
grupos: list[ClassGroup] = []
places: list[Place] = []
humans: list[Human] = []
objects: list[Object] = []
# ╚¤═══════¤VARIABLES TEMPORALES¤════════¤╝


# ╔¤═══════¤PROJECT NAME¤════════¤╗
def save_projecto_name(name):
    global projecto_name
    projecto_name = name


def fl_save_projecto_name(e):
    save_projecto_name(e.control.value)


# ╚¤═══════¤PROJECT NAME¤════════¤╝


# ╔¤═══════¤GRUPOS¤════════¤╗
def add_grupo(name):
    global grupos
    grupo = ClassGroup(name=name)
    grupos.append(grupo)
    return grupo


def get_grupos():
    return grupos


def clear_grupos():
    global grupos
    grupos = []


def remove_grupo(grupo_name):
    global grupos
    for g in grupos:
        if g.name == grupo_name:
            grupos.remove(g)
            break


# ╚¤═══════¤GRUPOS¤════════¤╝


# ╔¤═══════¤HUMANS¤════════¤╗
def add_human(name, type_h="", quantity=0):
    global humans
    human = Human(name=name, type=type_h, quantity=quantity)
    humans.append(human)
    return human


def get_humans():
    return humans


def clear_humans():
    global humans
    humans = []


def remove_human(human_name):
    global humans
    for h in humans:
        if h.name == human_name:
            humans.remove(h)
            break


def update_human_type(human_name, new_type):
    global humans
    for h in humans:
        if h.name == human_name:
            h.type = new_type
            break


def update_human_quantity(human_name, new_quantity):
    global humans
    for h in humans:
        if h.name == human_name:
            h.quantity = new_quantity
            break


# ╚¤═══════¤HUMANS¤════════¤╝


# ╔¤═══════¤PLACES¤════════¤╗
def add_place(name, type_p="", quantity=0):
    global places
    place = Place(name=name, type=type_p, quantity=quantity)
    places.append(place)
    return place


def get_places():
    return places


def clear_places():
    global places
    places = []


def remove_place(place_name):
    global places
    for p in places:
        if p.name == place_name:
            places.remove(p)
            break


def update_place_type(place_name, new_type):
    global places
    for p in places:
        if p.name == place_name:
            p.type = new_type
            break


def update_place_quantity(place_name, new_quantity):
    global places
    for p in places:
        if p.name == place_name:
            p.quantity = new_quantity
            break


# ╚¤═══════¤PLACES¤════════¤╝


# ╔¤═══════¤OBJECTS¤════════¤╗
def add_object(name, quantity=0):
    global objects
    obj = Object(name=name, quantity=quantity)
    objects.append(obj)
    return obj


def get_objects():
    return objects


def clear_objects():
    global objects
    objects = []


def remove_object(object_name):
    global objects
    for o in objects:
        if o.name == object_name:
            objects.remove(o)
            break


def update_object_quantity(object_name, new_quantity):
    global objects
    for o in objects:
        if o.name == object_name:
            o.quantity = new_quantity
            break


# ╚¤═══════¤OBJECTS¤════════¤╝


# ╔¤═══════¤EXPORT/IMPORT JSON¤════════¤╗
def export_to_json(filepath):
    data = {
        "projecto_name": projecto_name,
        "grupos": [asdict(g) for g in grupos],
        "places": [asdict(p) for p in places],
        "humans": [asdict(h) for h in humans],
        "objects": [asdict(o) for o in objects],
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# def import_from_json(filepath):
# ╚¤═══════¤EXPORT/IMPORT JSON¤════════¤╝


# ╔¤═══════¤SAVE BUTTON¤════════¤╗
def create_save_button(page: fl.Page):
    def on_save_result(e: fl.FilePickerResultEvent):
        if e.path:
            filepath = e.path if e.path.endswith(".json") else f"{e.path}.json"
            export_to_json(filepath)

    save_picker = fl.FilePicker(on_result=on_save_result)
    page.overlay.append(save_picker)

    def on_save_click(e):
        save_picker.save_file(
            file_name=f"{projecto_name}.json",
            file_type=fl.FilePickerFileType.CUSTOM,
            allowed_extensions=["json"],
        )

    return fl.IconButton(
        icon=fl.Icons.SAVE,
        icon_color="white",
        icon_size=20,
        on_click=on_save_click,
    )


# ╚¤═══════¤SAVE BUTTON¤════════¤╝

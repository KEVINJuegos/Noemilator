# temp_save.py
import flet as fl
import json
from dataclasses import asdict
from data.resources import ClassGroup, Human, Object, Place

# ╔¤═══════¤VARIABLES TEMPORALES¤════════¤╗
projecto_name = "Nuevo Proyecto"
grupos: list[ClassGroup] = []
lugares: list[Place] = []
humanos: list[Human] = []
objetos: list[Object] = []
# ╚¤═══════¤VARIABLES TEMPORALES¤════════¤╝


# ╔¤═══════¤PROJECTO NAME¤════════¤╗
def save_projecto_name(name):
    global projecto_name
    projecto_name = name


def fl_save_projecto_name(e):
    save_projecto_name(e.control.value)


# ╚¤═══════¤PROJECTO NAME¤════════¤╝


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


# ╔¤═══════¤HUMANOS¤════════¤╗
def add_humano(name, type_h="", quantity=0):
    global humanos
    humano = Human(name=name, type=type_h, quantity=quantity)
    humanos.append(humano)
    return humano


def get_humanos():
    return humanos


def clear_humanos():
    global humanos
    humanos = []


def remove_humano(humano_name):
    global humanos
    for h in humanos:
        if h.name == humano_name:
            humanos.remove(h)
            break


def update_humano_type(humano_name, new_type):
    global humanos
    for h in humanos:
        if h.name == humano_name:
            h.type = new_type
            break


def update_humano_quantity(humano_name, new_quantity):
    global humanos
    for h in humanos:
        if h.name == humano_name:
            h.quantity = new_quantity
            break


# ╚¤═══════¤HUMANS¤════════¤╝


# ╔¤═══════¤PLACES¤════════¤╗
def add_lugar(name, type_l="", quantity=0):
    global lugares
    lugar = Place(name=name, type=type_l, quantity=quantity)
    lugares.append(lugar)
    return lugar


def get_lugares():
    return lugares


def clear_lugares():
    global lugares
    lugares = []


def remove_lugar(lugar_name):
    global lugares
    for l in lugares:
        if l.name == lugar_name:
            lugares.remove(l)
            break


def update_lugar_type(lugar_name, new_type):
    global lugares
    for l in lugares:
        if l.name == lugar_name:
            l.type = new_type
            break


def update_lugar_quantity(lugar_name, new_quantity):
    global lugares
    for l in lugares:
        if l.name == lugar_name:
            l.quantity = new_quantity
            break


# ╚¤═══════¤PLACES¤════════¤╝


# ╔¤═══════¤OBJETOS¤════════¤╗
def add_objeto(name, quantity=0):
    global objetos
    objeto = Object(name=name, quantity=quantity)
    objetos.append(objeto)
    return objeto


def get_objetos():
    return objetos


def clear_objetos():
    global objetos
    objetos = []


def remove_objeto(objeto_name):
    global objetos
    for o in objetos:
        if o.name == objeto_name:
            objetos.remove(o)
            break


def update_objeto_quantity(objeto_name, new_quantity):
    global objetos
    for o in objetos:
        if o.name == objeto_name:
            o.quantity = new_quantity
            break


# ╚¤═══════¤OBJETOS¤════════¤╝


# ╔¤═══════¤EXPORT/IMPORT JSON¤════════¤╗
def export_to_json(filepath):
    data = {
        "projecto_name": projecto_name,
        "grupos": [asdict(g) for g in grupos],
        "lugares": [asdict(l) for l in lugares],
        "humanos": [asdict(h) for h in humanos],
        "objetos": [asdict(o) for o in objetos],
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

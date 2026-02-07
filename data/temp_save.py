# temp_save.py
import flet as fl
import json

# ╔¤═══════¤VARIABLES TEMPORALES¤════════¤╗
projecto_name = "Nuevo Proyecto"
grupos = []
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
    grupo = {
        "name": name,
    }
    grupos.append(grupo)
    return grupo


def get_grupos():
    return grupos


def clear_grupos():
    global grupos
    grupos = []


# ╚¤═══════¤GRUPOS¤════════¤╝


# ╔¤═══════¤EXPORT/IMPORT JSON¤════════¤╗
def export_to_json(filepath):
    data = {
        "projecto_name": projecto_name,
        "grupos": grupos,
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# def import_from_json(filepath):
#     global projecto_name, grupos
#     with open(filepath, "r", encoding="utf-8") as f:
#         data = json.load(f)
#     projecto_name = data.get("projecto_name", "Nuevo Proyecto")
#     grupos = data.get("grupos", [])
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

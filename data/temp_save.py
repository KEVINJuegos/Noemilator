import flet as fl
import json

# ╔¤═══════¤VARIABLES TEMPORALES¤════════¤╗
projecto_name = "Nuevo Proyecto"
# ╚¤═══════¤VARIABLES TEMPORALES¤════════¤╝


def save_projecto_name(name):
    global projecto_name
    projecto_name = name


def fl_save_projecto_name(e):
    save_projecto_name(e.control.value)


def export_to_json(filepath):
    data = {"projecto_name": projecto_name}
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


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

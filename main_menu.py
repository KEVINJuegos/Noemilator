# main_menu.py
import flet as fl


def main(page: fl.Page):
    page.title = "Eskola shuder"
    page.bgcolor = "#121212"
    page.vertical_alignment = fl.MainAxisAlignment.END
    page.horizontal_alignment = fl.CrossAxisAlignment.CENTER
    page.theme_mode = fl.ThemeMode.DARK

    principal = fl.Column(
        controls=[
            fl.Text(value="Menú Principal"),
            fl.ElevatedButton("New"),
            fl.Button("Settings"),
            fl.Button("Exit"),
        ],
        horizontal_alignment=fl.CrossAxisAlignment.CENTER,
    )
    page.add(principal)


fl.app(target=main)

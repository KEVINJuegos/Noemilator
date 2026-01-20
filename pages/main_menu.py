# main_menu.py
import flet as fl


def main_menu(page: fl.Page):
    page.title = "Main Menu - Noemilator"
    page.bgcolor = "#121212"
    page.theme_mode = fl.ThemeMode.DARK

    principal = fl.Column(
        controls=[
            fl.Text(value="Menú Principal"),
            fl.ElevatedButton("New", on_click=lambda _: page.go("/workspace")),
            fl.ElevatedButton("Settings"),
            fl.ElevatedButton("Exit", on_click=lambda _: page.window.close()),
        ],
        horizontal_alignment=fl.CrossAxisAlignment.CENTER,
    )

    return fl.View(
        route="/",
        bgcolor="#121212",
        controls=[
            fl.Container(
                content=principal,
                expand=True,
                alignment=fl.alignment.bottom_center,
            )
        ],
    )

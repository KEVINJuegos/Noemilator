# workspace.py
import flet as fl


def workspace(page: fl.Page):
    page.title = "Workspace - Noemilator"
    page.bgcolor = "#121212"
    page.theme_mode = fl.ThemeMode.DARK

    return fl.View(
        route="/workspace",
        controls=[
            fl.Text("Workspace", size=50),
            fl.ElevatedButton("Main Menu", on_click=lambda _: page.go("/")),
        ],
    )

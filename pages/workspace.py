# workspace.py
import flet as fl


def workspace(page: fl.Page):
    page.title = "Workspace - Noemilator"
    page.bgcolor = "#121212"
    page.theme_mode = fl.ThemeMode.DARK

    projecto_name = fl.TextField(
        value="Nueva planificación",
        border=fl.InputBorder.NONE,
        text_size=18,
        color="white",
        width=300,
    )

    NoemilatorTM = fl.Row(
        controls=[
            fl.Text("🚀", size=30),  # EMOJI TEMPORAL, BUSCAR LOGO
            fl.Text(
                "Noemilator",
                size=22,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
        ],
        spacing=10,
    )

    top_embed = fl.Container(
        content=fl.Row(
            controls=[
                projecto_name,
                NoemilatorTM,
            ],
            alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor="#1E1E1E",
        # padding=  # Ancho de la barra superior, pendiente a escoger
    )

    return fl.View(
        route="/workspace",
        bgcolor="#121212",
        padding=0,
        controls=[top_embed],
    )

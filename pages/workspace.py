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
        padding=fl.padding.symmetric(horizontal=20, vertical=10),
        # padding=None  # Ancho de la barra superior, pendiente a escoger
    )

    # ╔¤═══════¤SIDE-BAR BUTTONS¤════════¤╗
    button_dashboard = fl.Container(
        content=fl.Column(
            controls=[
                fl.Icon(fl.Icons.DASHBOARD, size=24, color="white"),
                fl.Text("Dashboard", size=10, color="white"),
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        padding=10,
        border=fl.border.only(left=fl.BorderSide(2, "white")),
        bgcolor="#2D2D2D",
    )

    button_events = fl.Container(
        content=fl.Column(
            controls=[
                fl.Icon(fl.Icons.EVENT, size=24, color="#858585"),
                fl.Text("Eventos", size=10, color="#858585"),
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        padding=10,
    )

    button_classesgroups = fl.Container(
        content=fl.Column(
            controls=[
                fl.Icon(fl.Icons.GROUP, size=24, color="#858585"),
                fl.Text("Grupos", size=10, color="#858585"),
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        padding=10,
    )

    button_places = fl.Container(
        content=fl.Column(
            controls=[
                fl.Icon(fl.Icons.LOCATION_ON, size=24, color="#858585"),
                fl.Text("Locales", size=10, color="#858585"),
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        padding=10,
    )

    button_humans = fl.Container(
        content=fl.Column(
            controls=[
                fl.Icon(fl.Icons.PERSON, size=24, color="#858585"),
                fl.Text("Humanos", size=10, color="#858585"),
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        padding=10,
    )

    button_objects = fl.Container(
        content=fl.Column(
            controls=[
                fl.Icon(fl.Icons.INVENTORY_2, size=24, color="#858585"),
                fl.Text("Objetos", size=10, color="#858585"),
            ],
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            spacing=2,
        ),
        padding=10,
    )

    # ╚¤═══════¤SIDE-BAR BUTTONS¤════════¤╝

    sidebar = fl.Container(
        content=fl.Column(
            controls=[
                button_dashboard,
                button_events,
                button_classesgroups,
                button_places,
                button_humans,
                button_objects,
            ],
            spacing=0,
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#252526",
        padding=fl.padding.only(top=10),
        width=75,
    )

    hud_bars = fl.Column(controls=[top_embed, sidebar])

    return fl.View(
        route="/workspace",
        bgcolor="#121212",
        padding=0,
        controls=[hud_bars],
    )

# workspace.py
import flet as fl
from .panels.dashboard import panel_creator_dashboard
from .panels.events import panel_creator_events
from .panels.grupos import panel_creator_classesgroups
from .panels.places import panel_creator_places
from .panels.humans import panel_creator_humans
from .panels.objects import panel_creator_objects


def workspace(page: fl.Page):
    page.title = "Workspace - Noemilator"
    page.bgcolor = "#121212"
    page.theme_mode = fl.ThemeMode.DARK

    # ╔¤═══════¤TOP EMBED¤════════¤╗
    from data import temp_save

    projecto_name = fl.TextField(
        value=temp_save.projecto_name,
        border=fl.InputBorder.NONE,
        text_size=18,
        color="white",
        width=300,
        on_blur=temp_save.fl_save_projecto_name,
    )

    save_button = temp_save.create_save_button(page)

    NoemilatorTM = fl.Row(
        controls=[
            fl.Text("🚀", size=30),
            fl.Text("Noemilator", size=22, weight=fl.FontWeight.BOLD, color="white"),
        ],
        spacing=10,
    )

    top_embed = fl.Container(
        content=fl.Row(
            controls=[
                fl.Row(controls=[projecto_name, save_button], spacing=5),
                NoemilatorTM,
            ],
            alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor="#1E1E1E",
        padding=fl.padding.symmetric(horizontal=20, vertical=10),
    )
    # ╚¤═══════¤TOP EMBED¤════════¤╝

    main_area = fl.Container(
        expand=True,
        padding=0,
    )

    # ╔¤═══════¤SIDE-BAR BUTTONS¤════════¤╗
    def create_sidebar_button(icono, texto, activo=False):
        icon = fl.Icon(icono, size=24, color="white" if activo else "#858585")
        text = fl.Text(texto, size=10, color="white" if activo else "#858585")
        return fl.Container(
            content=fl.Column(
                controls=[icon, text],
                horizontal_alignment=fl.CrossAxisAlignment.CENTER,
                spacing=2,
            ),
            padding=10,
            border=fl.border.only(left=fl.BorderSide(2, "white")) if activo else None,
            bgcolor="#2D2D2D" if activo else None,
        )

    # fmt: off
    button_dashboard = create_sidebar_button( fl.Icons.DASHBOARD, "Dashboard", activo=True)
    button_events = create_sidebar_button(fl.Icons.EVENT, "Eventos")
    button_classesgroups = create_sidebar_button(fl.Icons.GROUP, "Grupos")
    button_places = create_sidebar_button(fl.Icons.LOCATION_ON, "Locales")
    button_humans = create_sidebar_button(fl.Icons.PERSON, "Humanos")
    button_objects = create_sidebar_button(fl.Icons.INVENTORY_2, "Objetos")
    # fmt: on

    sidebar_buttons = [
        button_dashboard,
        button_events,
        button_classesgroups,
        button_places,
        button_humans,
        button_objects,
    ]
    # ╚¤═══════¤SIDE-BAR BUTTONS¤════════¤╝

    # ╔¤═══════¤NAVGEGACIÓN PANELS¤════════¤╗
    def unmark_buttonsidebar(sidebar_button):
        icon = sidebar_button.content.controls[0]
        text = sidebar_button.content.controls[1]
        icon.color = "#858585"
        text.color = "#858585"
        sidebar_button.bgcolor = None
        sidebar_button.border = None

    def mark_buttonsidebar(sidebar_button):
        icon = sidebar_button.content.controls[0]
        text = sidebar_button.content.controls[1]
        icon.color = "white"
        text.color = "white"
        sidebar_button.bgcolor = "#2D2D2D"
        sidebar_button.border = fl.border.only(left=fl.BorderSide(2, "white"))

    def change_panel(sidebar_button, panel_creator):
        def handler(e):
            for button in sidebar_buttons:
                unmark_buttonsidebar(button)
            mark_buttonsidebar(sidebar_button)
            main_area.content = panel_creator(page)
            page.update()

        return handler

    # fmt: off
    button_dashboard.on_click = change_panel(button_dashboard, panel_creator_dashboard)
    button_events.on_click = change_panel(button_events, panel_creator_events)
    button_classesgroups.on_click = change_panel(button_classesgroups, panel_creator_classesgroups)
    button_places.on_click = change_panel(button_places, panel_creator_places)
    button_humans.on_click = change_panel(button_humans, panel_creator_humans)
    button_objects.on_click = change_panel(button_objects, panel_creator_objects)
    # fmt: on

    # ╚¤═══════¤NAVGEGACIÓN PANELS¤════════¤╝

    # ╔¤═══════¤WORKSPACE¤════════¤╗
    sidebar = fl.Container(
        content=fl.Column(
            controls=sidebar_buttons,
            spacing=0,
            horizontal_alignment=fl.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#1E1E1E",
        padding=fl.padding.only(top=10),
        width=75,
    )

    area_trabajo = fl.Row(
        controls=[sidebar, main_area],
        spacing=0,
        expand=True,
    )

    hud_bars = fl.Column(
        controls=[top_embed, area_trabajo],
        spacing=0,
        expand=True,
    )

    main_area.content = panel_creator_dashboard(page)

    return fl.View(
        route="/workspace",
        bgcolor="#121212",
        padding=0,
        controls=[hud_bars],
    )


# ╚¤═══════¤WORKSPACE¤════════¤╝

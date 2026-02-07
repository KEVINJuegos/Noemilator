# humans.py
import flet as fl
from data import temp_save
from data.resources import HUMAN_TYPES

TYPE_COLORS = {
    "Profesor(a)": "#FF9800",
    "Secretario(a)": "#2196F3",
    "Directivo(a)": "#4CAF50",
    "Seguridad": "#F44336",
    "Otro": "#858585",
}

TYPE_ICONS = {
    "Profesor(a)": fl.Icons.SCHOOL,
    "Secretario(a)": fl.Icons.EDIT_NOTE,
    "Directivo(a)": fl.Icons.ADMIN_PANEL_SETTINGS,
    "Seguridad": fl.Icons.SHIELD,
    "Otro": fl.Icons.PERSON,
}


def panel_creator_humans(page: fl.Page):

    # ╔¤═══════¤HUMANOS AGREGADOS¤════════¤╗
    humanos_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_humano(humano_name):
        def handler(e):
            temp_save.remove_humano(humano_name)
            for control in humanos_list.controls:
                if control.data == humano_name:
                    humanos_list.controls.remove(control)
                    break
            page.update()

        return handler

    def fl_update_type(humano_name, icon_ref, badge_ref):
        def handler(e):
            new_type = e.control.value
            temp_save.update_humano_type(humano_name, new_type)
            icon_ref.color = TYPE_COLORS.get(new_type, "#858585")
            icon_ref.name = TYPE_ICONS.get(new_type, fl.Icons.PERSON)
            badge_ref.bgcolor = TYPE_COLORS.get(new_type, "#858585")
            badge_ref.content.value = new_type
            page.update()

        return handler

    def create_onlist_humano(humano):
        type_color = TYPE_COLORS.get(humano.type, "#858585")
        type_icon = TYPE_ICONS.get(humano.type, fl.Icons.PERSON)

        icon_ref = fl.Icon(type_icon, color=type_color)

        badge_ref = fl.Container(
            content=fl.Text(
                humano.type,
                size=11,
                color="white",
            ),
            bgcolor=type_color,
            border_radius=12,
            padding=fl.padding.only(left=8, right=8, top=3, bottom=3),
        )

        return fl.Container(
            data=humano.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            icon_ref,
                            fl.Text(
                                humano.name,
                                size=16,
                                weight=fl.FontWeight.W_500,
                                color="white",
                            ),
                            badge_ref,
                        ],
                        spacing=10,
                    ),
                    fl.Row(
                        controls=[
                            fl.Dropdown(
                                value=humano.type,
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=150,
                                text_size=13,
                                options=[fl.dropdown.Option(t) for t in HUMAN_TYPES],
                                on_change=fl_update_type(
                                    humano.name, icon_ref, badge_ref
                                ),
                            ),
                            fl.IconButton(
                                icon=fl.Icons.DELETE,
                                icon_color="#F44336",
                                icon_size=20,
                                tooltip="Eliminar humano",
                                on_click=fl_delete_humano(humano.name),
                            ),
                        ],
                        spacing=5,
                        vertical_alignment=fl.CrossAxisAlignment.CENTER,
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=15, top=8, bottom=8, right=8),
        )

    # ╚¤═══════¤HUMANOS AGREGADOS¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_humano_name = fl.TextField(
        label="Nombre del humano",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    dropdown_humano_type = fl.Dropdown(
        label="Tipo",
        value=None,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=150,
        text_size=13,
        options=[fl.dropdown.Option(t) for t in HUMAN_TYPES],
    )

    def fl_add_humano(e):
        if not input_humano_name.value:
            return
        if not dropdown_humano_type.value:
            return

        humano = temp_save.add_humano(
            name=input_humano_name.value,
            type_h=dropdown_humano_type.value,
        )
        humanos_list.controls.append(create_onlist_humano(humano))
        input_humano_name.value = ""
        dropdown_humano_type.value = None
        page.update()

    addhumano_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#FF9800",
        color="white",
        height=45,
        on_click=fl_add_humano,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_humanos = fl.Row(
        controls=[
            fl.Text(
                "🧑 Humanos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_humano_name,
                    dropdown_humano_type,
                    addhumano_button,
                ],
                spacing=10,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=fl.CrossAxisAlignment.CENTER,
    )
    # ╚¤═══════¤HEADER¤════════¤╝

    return fl.Container(
        content=fl.Column(
            controls=[
                header_humanos,
                fl.Divider(height=10, color="#3D3D3D"),
                humanos_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )

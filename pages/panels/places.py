# places.py
import flet as fl
from data import temp_save
from data.resources import PLACE_TYPES

TYPE_COLORS = {
    "Aula": "#4CAF50",
    "Lab. Física": "#FF9800",
    "Lab. Química": "#9C27B0",
    "Lab. Biología": "#8BC34A",
    "Lab. Informática": "#2196F3",
    "Área de Deportes": "#F44336",
    "Sala de Reuniones": "#607D8B",
    "Otro": "#858585",
}

TYPE_ICONS = {
    "Aula": fl.Icons.SCHOOL,
    "Lab. Física": fl.Icons.SCIENCE,
    "Lab. Química": fl.Icons.BIOTECH,
    "Lab. Biología": fl.Icons.PARK,
    "Lab. Informática": fl.Icons.COMPUTER,
    "Área de Deportes": fl.Icons.SPORTS_SOCCER,
    "Sala de Reuniones": fl.Icons.MEETING_ROOM,
    "Otro": fl.Icons.PLACE,
}


def panel_creator_places(page: fl.Page):

    # ╔¤═══════¤LUGARES AGREGADOS¤════════¤╗
    lugares_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_lugar(lugar_name):
        def handler(e):
            temp_save.remove_lugar(lugar_name)
            for control in lugares_list.controls:
                if control.data == lugar_name:
                    lugares_list.controls.remove(control)
                    break
            page.update()

        return handler

    def fl_update_type(lugar_name, icon_ref, badge_ref):
        def handler(e):
            new_type = e.control.value
            temp_save.update_lugar_type(lugar_name, new_type)
            icon_ref.color = TYPE_COLORS.get(new_type, "#858585")
            icon_ref.name = TYPE_ICONS.get(new_type, fl.Icons.PLACE)
            badge_ref.bgcolor = TYPE_COLORS.get(new_type, "#858585")
            badge_ref.content.value = new_type
            page.update()

        return handler

    def fl_update_quantity(lugar_name):
        def handler(e):
            new_value = e.control.value
            if new_value == "":
                new_value = 0
            temp_save.update_lugar_quantity(lugar_name, int(new_value))

        return handler

    def create_onlist_lugar(lugar):
        type_color = TYPE_COLORS.get(lugar.type, "#858585")
        type_icon = TYPE_ICONS.get(lugar.type, fl.Icons.PLACE)

        icon_ref = fl.Icon(type_icon, color=type_color)

        badge_ref = fl.Container(
            content=fl.Text(
                lugar.type,
                size=11,
                color="white",
            ),
            bgcolor=type_color,
            border_radius=12,
            padding=fl.padding.only(left=8, right=8, top=3, bottom=3),
        )

        return fl.Container(
            data=lugar.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            icon_ref,
                            fl.Text(
                                lugar.name,
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
                                value=lugar.type,
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=170,
                                text_size=13,
                                options=[fl.dropdown.Option(t) for t in PLACE_TYPES],
                                on_change=fl_update_type(
                                    lugar.name, icon_ref, badge_ref
                                ),
                            ),
                            fl.Text(
                                "Cantidad:",
                                size=13,
                                color="#B0B0B0",
                            ),
                            fl.TextField(
                                value=str(lugar.quantity),
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=70,
                                height=40,
                                text_size=13,
                                text_align=fl.TextAlign.CENTER,
                                input_filter=fl.NumbersOnlyInputFilter(),
                                on_change=fl_update_quantity(lugar.name),
                            ),
                            fl.IconButton(
                                icon=fl.Icons.DELETE,
                                icon_color="#F44336",
                                icon_size=20,
                                tooltip="Eliminar lugar",
                                on_click=fl_delete_lugar(lugar.name),
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

    # ╚¤═══════¤LUGARES AGREGADOS¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_lugar_name = fl.TextField(
        label="Nombre del lugar",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    dropdown_lugar_type = fl.Dropdown(
        label="Tipo",
        value=None,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=170,
        text_size=13,
        options=[fl.dropdown.Option(t) for t in PLACE_TYPES],
    )

    input_lugar_quantity = fl.TextField(
        label="Cantidad",
        value="0",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=80,
        height=50,
        text_size=13,
        text_align=fl.TextAlign.CENTER,
        input_filter=fl.NumbersOnlyInputFilter(),
    )

    def fl_add_lugar(e):
        if not input_lugar_name.value:
            return
        if not dropdown_lugar_type.value:
            return

        if not input_lugar_quantity.value or input_lugar_quantity.value == "":
            input_lugar_quantity.value = "0"
            quantity = 0
        else:
            quantity = int(input_lugar_quantity.value)

        lugar = temp_save.add_lugar(
            name=input_lugar_name.value,
            type_l=dropdown_lugar_type.value,
            quantity=quantity,
        )
        lugares_list.controls.append(create_onlist_lugar(lugar))
        input_lugar_name.value = ""
        dropdown_lugar_type.value = None
        input_lugar_quantity.value = "0"
        page.update()

    addlugar_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#2196F3",
        color="white",
        height=45,
        on_click=fl_add_lugar,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_lugares = fl.Row(
        controls=[
            fl.Text(
                "📍 Lugares",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_lugar_name,
                    dropdown_lugar_type,
                    input_lugar_quantity,
                    addlugar_button,
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
                header_lugares,
                fl.Divider(height=10, color="#3D3D3D"),
                lugares_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )

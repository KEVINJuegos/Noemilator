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

    # ╔¤═══════¤HUMANS LIST¤════════¤╗
    humans_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_human(human_name):
        def handler(e):
            temp_save.remove_human(human_name)
            for control in humans_list.controls:
                if control.data == human_name:
                    humans_list.controls.remove(control)
                    break
            page.update()

        return handler

    def fl_update_type(human_name, icon_ref, badge_ref):
        def handler(e):
            new_type = e.control.value
            temp_save.update_human_type(human_name, new_type)
            icon_ref.color = TYPE_COLORS.get(new_type, "#858585")
            icon_ref.name = TYPE_ICONS.get(new_type, fl.Icons.PERSON)
            badge_ref.bgcolor = TYPE_COLORS.get(new_type, "#858585")
            badge_ref.content.value = new_type
            page.update()

        return handler

    def fl_update_quantity(human_name):
        def handler(e):
            new_value = e.control.value
            if new_value == "":
                new_value = 0
            temp_save.update_human_quantity(human_name, int(new_value))

        return handler

    def create_onlist_human(human):
        type_color = TYPE_COLORS.get(human.type, "#858585")
        type_icon = TYPE_ICONS.get(human.type, fl.Icons.PERSON)

        icon_ref = fl.Icon(type_icon, color=type_color)

        badge_ref = fl.Container(
            content=fl.Text(
                human.type,
                size=11,
                color="white",
            ),
            bgcolor=type_color,
            border_radius=12,
            padding=fl.padding.only(left=8, right=8, top=3, bottom=3),
        )

        return fl.Container(
            data=human.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            icon_ref,
                            fl.Text(
                                human.name,
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
                                value=human.type,
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=150,
                                text_size=13,
                                options=[fl.dropdown.Option(t) for t in HUMAN_TYPES],
                                on_change=fl_update_type(
                                    human.name, icon_ref, badge_ref
                                ),
                            ),
                            fl.Text(
                                "Cantidad:",
                                size=13,
                                color="#B0B0B0",
                            ),
                            fl.TextField(
                                value=str(human.quantity),
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=70,
                                height=40,
                                text_size=13,
                                text_align=fl.TextAlign.CENTER,
                                input_filter=fl.NumbersOnlyInputFilter(),
                                on_change=fl_update_quantity(human.name),
                            ),
                            fl.IconButton(
                                icon=fl.Icons.DELETE,
                                icon_color="#F44336",
                                icon_size=20,
                                tooltip="Eliminar humano",
                                on_click=fl_delete_human(human.name),
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

    # ╚¤═══════¤HUMANS LIST¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_human_name = fl.TextField(
        label="Nombre del humano",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    dropdown_human_type = fl.Dropdown(
        label="Tipo",
        value=None,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=150,
        text_size=13,
        options=[fl.dropdown.Option(t) for t in HUMAN_TYPES],
    )

    input_human_quantity = fl.TextField(
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

    def fl_add_human(e):
        if not input_human_name.value:
            return
        if not dropdown_human_type.value:
            return

        if not input_human_quantity.value or input_human_quantity.value == "":
            input_human_quantity.value = "0"
            quantity = 0
        else:
            quantity = int(input_human_quantity.value)

        human = temp_save.add_human(
            name=input_human_name.value,
            type_h=dropdown_human_type.value,
            quantity=quantity,
        )
        humans_list.controls.append(create_onlist_human(human))
        input_human_name.value = ""
        dropdown_human_type.value = None
        input_human_quantity.value = "0"
        page.update()

    add_human_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#FF9800",
        color="white",
        height=45,
        on_click=fl_add_human,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_humans = fl.Row(
        controls=[
            fl.Text(
                "🧑 Humanos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_human_name,
                    dropdown_human_type,
                    input_human_quantity,
                    add_human_button,
                ],
                spacing=10,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
        ],
        alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=fl.CrossAxisAlignment.CENTER,
    )
    # ╚¤═══════¤HEADER¤════════¤╝

    # Cargar datos existentes
    [humans_list.controls.append(create_onlist_human(h)) for h in temp_save.get_humans()] # fmt: skip

    return fl.Container(
        content=fl.Column(
            controls=[
                header_humans,
                fl.Divider(height=10, color="#3D3D3D"),
                humans_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )

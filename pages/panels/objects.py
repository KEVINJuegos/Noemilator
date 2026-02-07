import flet as fl
from data import temp_save


def panel_creator_objects(page: fl.Page):

    # ╔¤═══════¤OBJECTS LIST¤════════¤╗
    objects_list = fl.Column(
        controls=[],
        spacing=10,
        scroll=fl.ScrollMode.AUTO,
        expand=True,
    )

    def fl_delete_object(object_name):
        def handler(e):
            temp_save.remove_object(object_name)
            for control in objects_list.controls:
                if control.data == object_name:
                    objects_list.controls.remove(control)
                    break
            page.update()

        return handler

    def fl_update_quantity(object_name):
        def handler(e):
            new_value = e.control.value
            if new_value == "":
                new_value = 0
            temp_save.update_object_quantity(object_name, int(new_value))

        return handler

    def create_onlist_object(obj):
        return fl.Container(
            data=obj.name,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Icon(fl.Icons.INVENTORY_2, color="#9C27B0"),
                            fl.Text(
                                obj.name,
                                size=16,
                                weight=fl.FontWeight.W_500,
                                color="white",
                            ),
                        ],
                        spacing=10,
                    ),
                    fl.Row(
                        controls=[
                            fl.Text(
                                "Cantidad:",
                                size=13,
                                color="#B0B0B0",
                            ),
                            fl.TextField(
                                value=str(obj.quantity),
                                bgcolor="#3D3D3D",
                                border_color="#858585",
                                color="white",
                                width=70,
                                height=40,
                                text_size=13,
                                text_align=fl.TextAlign.CENTER,
                                input_filter=fl.NumbersOnlyInputFilter(),
                                on_change=fl_update_quantity(obj.name),
                            ),
                            fl.IconButton(
                                icon=fl.Icons.DELETE,
                                icon_color="#F44336",
                                icon_size=20,
                                tooltip="Eliminar objeto",
                                on_click=fl_delete_object(obj.name),
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

    # ╚¤═══════¤OBJECTS LIST¤════════¤╝

    # ╔¤═══════¤INPUTS¤════════¤╗
    input_object_name = fl.TextField(
        label="Nombre del objeto",
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        width=200,
        height=50,
        text_size=13,
    )

    input_object_quantity = fl.TextField(
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

    def fl_add_object(e):
        if not input_object_name.value:
            return

        if not input_object_quantity.value or input_object_quantity.value == "":
            input_object_quantity.value = "0"
            quantity = 0
        else:
            quantity = int(input_object_quantity.value)

        obj = temp_save.add_object(
            name=input_object_name.value,
            quantity=quantity,
        )
        objects_list.controls.append(create_onlist_object(obj))
        input_object_name.value = ""
        input_object_quantity.value = "0"
        page.update()

    add_object_button = fl.ElevatedButton(
        text="Add",
        icon=fl.Icons.ADD,
        bgcolor="#9C27B0",
        color="white",
        height=45,
        on_click=fl_add_object,
    )
    # ╚¤═══════¤INPUTS¤════════¤╝

    # ╔¤═══════¤HEADER¤════════¤╗
    header_objects = fl.Row(
        controls=[
            fl.Text(
                "📦 Objetos",
                size=24,
                weight=fl.FontWeight.BOLD,
                color="white",
            ),
            fl.Row(
                controls=[
                    input_object_name,
                    input_object_quantity,
                    add_object_button,
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
    [objects_list.controls.append(create_onlist_object(o)) for o in temp_save.get_objects()]  # fmt: skip

    return fl.Container(
        content=fl.Column(
            controls=[
                header_objects,
                fl.Divider(height=10, color="#3D3D3D"),
                objects_list,
            ],
            spacing=10,
            expand=True,
        ),
        padding=20,
        expand=True,
    )

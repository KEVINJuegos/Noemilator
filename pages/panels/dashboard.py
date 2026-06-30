import flet as fl
from data import temp_save
from data.resources import DAYS, ScheduleEvent


def panel_creator_dashboard(page: fl.Page):
    schedule = temp_save.get_schedule()

    schedule_table_container = fl.Container(expand=True)
    slots_list = fl.Column(
        controls=[], spacing=10, scroll=fl.ScrollMode.AUTO, expand=True
    )

    # ╔¤═══════¤TURNOS LIST¤════════¤╗
    def create_onlist_slot(slot):
        start_field = fl.TextField(
            value=slot.start_time,
            bgcolor="#3D3D3D",
            border_color="#858585",
            color="white",
            width=70,
            height=40,
            text_size=12,
            text_align=fl.TextAlign.CENTER,
            hint_text="HH:MM",
            on_change=lambda e: [
                temp_save.update_time_slot(slot.number, start_time=e.control.value),
                rebuild_schedule_table(),
                page.update(),
            ],
        )
        end_field = fl.TextField(
            value=slot.end_time,
            bgcolor="#3D3D3D",
            border_color="#858585",
            color="white",
            width=70,
            height=40,
            text_size=12,
            text_align=fl.TextAlign.CENTER,
            hint_text="HH:MM",
            on_change=lambda e: [
                temp_save.update_time_slot(slot.number, end_time=e.control.value),
                rebuild_schedule_table(),
                page.update(),
            ],
        )

        def fl_delete_slot(e):
            temp_save.remove_time_slot(slot.number)
            rebuild_slots_list()
            rebuild_schedule_table()
            page.update()

        return fl.Container(
            data=slot.number,
            content=fl.Row(
                controls=[
                    fl.Row(
                        controls=[
                            fl.Container(
                                content=fl.Text(
                                    f"T{slot.number}",
                                    size=12,
                                    weight=fl.FontWeight.BOLD,
                                    color="white",
                                ),
                                bgcolor="#FF9800",
                                border_radius=5,
                                padding=fl.padding.symmetric(horizontal=6, vertical=4),
                                alignment=fl.alignment.center,
                            ),
                            start_field,
                            fl.Text("-", color="#858585", size=14),
                            end_field,
                        ],
                        spacing=2,
                    ),
                    fl.IconButton(
                        icon=fl.Icons.DELETE,
                        icon_color="#F44336",
                        icon_size=18,
                        tooltip="Eliminar turno",
                        on_click=fl_delete_slot,
                    ),
                ],
                alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=fl.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#2D2D2D",
            border_radius=8,
            padding=fl.padding.only(left=8, top=4, bottom=4, right=4),
        )

    def rebuild_slots_list():
        slots_list.controls.clear()
        for slot in temp_save.get_schedule().time_slots:
            slots_list.controls.append(create_onlist_slot(slot))

    # ╚¤═══════¤TURNOS LIST¤════════¤╝

    # ╔¤═══════¤INPUTS DÍAS-TURNOS¤════════¤╗
    dropdown_start_day = fl.Dropdown(
        label="Inicio",
        value=schedule.start_day,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        text_size=12,
        options=[fl.dropdown.Option(d) for d in DAYS],
        expand=True,
    )
    dropdown_end_day = fl.Dropdown(
        label="Fin",
        value=schedule.end_day,
        bgcolor="#2D2D2D",
        border_color="#858585",
        color="white",
        text_size=12,
        options=[fl.dropdown.Option(d) for d in DAYS],
        expand=True,
    )

    def fl_apply_days(e):
        temp_save.set_schedule_days(dropdown_start_day.value, dropdown_end_day.value)
        rebuild_schedule_table()
        page.update()

    apply_days_button = fl.ElevatedButton(
        text="Aplicar",
        icon=fl.Icons.CHECK,
        bgcolor="#4CAF50",
        color="white",
        height=35,
        on_click=fl_apply_days,
    )

    def fl_add_slot(e):
        temp_save.add_time_slot()
        rebuild_slots_list()
        rebuild_schedule_table()
        page.update()

    add_slot_button = fl.ElevatedButton(
        text="+ Turno",
        bgcolor="#FF9800",
        color="white",
        height=35,
        on_click=fl_add_slot,
        expand=True,
    )
    # ╚¤═══════¤INPUTS DÍAS-TURNOS¤════════¤╝

    # ╔¤═══════¤CREACION EVENTOS¤════════¤╗
    def create_resource_checkboxes(items, label_fn, fill_color):
        return fl.Column(
            controls=[
                fl.Checkbox(
                    label=label_fn(item),
                    data=item.name,
                    value=False,
                    fill_color=fill_color,
                    check_color="white",
                )
                for item in items
            ],
            spacing=2,
            scroll=fl.ScrollMode.AUTO,
            height=100,
        )

    def create_resource_block(icon, title, color, available, selected_names):
        checkboxes = create_resource_checkboxes(
            available,
            lambda item, t=title: (
                f"{item.name} ({item.type})"
                if hasattr(item, "type")
                else (
                    f"{item.name} (x{item.quantity})"
                    if hasattr(item, "quantity")
                    else item.name
                )
            ),
            color,
        )
        for cb in checkboxes.controls:
            cb.value = cb.data in selected_names

        return (
            fl.Container(
                content=fl.Column(
                    controls=[
                        fl.Row(
                            controls=[
                                fl.Icon(icon, color=color, size=18),
                                fl.Text(
                                    title,
                                    size=14,
                                    weight=fl.FontWeight.BOLD,
                                    color=color,
                                ),
                            ]
                        ),
                        (
                            checkboxes
                            if available
                            else fl.Text(
                                f"Sin {title.lower()}", size=12, color="#858585"
                            )
                        ),
                    ],
                    spacing=5,
                ),
                bgcolor="#1E1E1E",
                border_radius=8,
                padding=10,
                width=180,
            ),
            checkboxes,
        )

    def open_event_dialog(day: str, slot_number: int):
        event = temp_save.get_schedule_event(day, slot_number)
        if event is None:
            event = ScheduleEvent(day=day, slot_number=slot_number)

        name_field = fl.TextField(
            value=event.name,
            label="Nombre del Evento",
            bgcolor="#2D2D2D",
            border_color="#858585",
            color="white",
            width=300,
            text_size=14,
        )

        grupos_block, grupos_checkboxes = create_resource_block(
            fl.Icons.GROUP, "Grupos", "#4CAF50", temp_save.get_grupos(), event.groups
        )
        humans_block, humans_checkboxes = create_resource_block(
            fl.Icons.PERSON, "Humanos", "#FF9800", temp_save.get_humans(), event.humans
        )
        places_block, places_checkboxes = create_resource_block(
            fl.Icons.LOCATION_ON,
            "Lugares",
            "#2196F3",
            temp_save.get_places(),
            event.places,
        )
        objects_block, objects_checkboxes = create_resource_block(
            fl.Icons.INVENTORY_2,
            "Objetos",
            "#9C27B0",
            temp_save.get_objects(),
            event.objects,
        )

        def close_dialog(e):
            dialog.open = False
            page.update()

        def save_event(e):
            new_event = ScheduleEvent(
                day=day,
                slot_number=slot_number,
                name=name_field.value,
                groups=[cb.data for cb in grupos_checkboxes.controls if cb.value],
                humans=[cb.data for cb in humans_checkboxes.controls if cb.value],
                places=[cb.data for cb in places_checkboxes.controls if cb.value],
                objects=[cb.data for cb in objects_checkboxes.controls if cb.value],
            )
            temp_save.set_schedule_event(new_event)
            dialog.open = False
            rebuild_schedule_table()
            page.update()

        def delete_event(e):
            temp_save.remove_schedule_event(day, slot_number)
            dialog.open = False
            rebuild_schedule_table()
            page.update()

        slot_info = ""
        for slot in temp_save.get_schedule().time_slots:
            if slot.number == slot_number:
                slot_info = f"{slot.start_time} - {slot.end_time}"
                break

        dialog = fl.AlertDialog(
            modal=True,
            title=fl.Text(
                f"📅 {day} - Turno {slot_number}", size=18, weight=fl.FontWeight.BOLD
            ),
            content=fl.Container(
                content=fl.Column(
                    controls=[
                        fl.Text(f"⏰ {slot_info}", size=13, color="#B0B0B0"),
                        fl.Divider(height=10, color="#3D3D3D"),
                        name_field,
                        fl.Divider(height=10, color="#3D3D3D"),
                        fl.Row(controls=[grupos_block, humans_block], spacing=10),
                        fl.Row(controls=[places_block, objects_block], spacing=10),
                    ],
                    spacing=10,
                    scroll=fl.ScrollMode.AUTO,
                ),
                width=400,
                height=450,
            ),
            actions=[
                fl.TextButton(
                    "Eliminar",
                    on_click=delete_event,
                    style=fl.ButtonStyle(color="#F44336"),
                ),
                fl.TextButton("Cancelar", on_click=close_dialog),
                fl.ElevatedButton(
                    "Guardar", on_click=save_event, bgcolor="#4CAF50", color="white"
                ),
            ],
            actions_alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
            bgcolor="#2D2D2D",
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    # ╚¤═══════¤CREACION EVENTOS¤════════¤╝

    # ╔¤═══════¤TABLA¤════════¤╗
    def create_event_cell(day: str, slot_number: int):
        event = temp_save.get_schedule_event(day, slot_number)
        if event and not event.is_empty():
            chips = []
            if event.name:
                chips.append(
                    fl.Text(
                        event.name, size=11, weight=fl.FontWeight.BOLD, color="white"
                    )
                )
            resource_data = [
                (event.groups, "👥", "#4CAF50"),
                (event.humans, "🧑", "#FF9800"),
                (event.places, "📍", "#2196F3"),
                (event.objects, "📦", "#9C27B0"),
            ]
            resource_row = [
                fl.Container(
                    content=fl.Text(f"{emoji}{len(items)}", size=9),
                    bgcolor=color,
                    border_radius=3,
                    padding=2,
                )
                for items, emoji, color in resource_data
                if items
            ]
            if resource_row:
                chips.append(fl.Row(controls=resource_row, spacing=2, wrap=True))
            cell_content = fl.Column(
                controls=chips,
                spacing=3,
                horizontal_alignment=fl.CrossAxisAlignment.CENTER,
            )
            cell_bgcolor = "#3D3D3D"
            cell_border = fl.border.all(2, "#4CAF50")
        else:
            cell_content = fl.Icon(fl.Icons.ADD, color="#858585", size=20)
            cell_bgcolor = "#252525"
            cell_border = fl.border.all(1, "#3D3D3D")

        return fl.Container(
            content=cell_content,
            bgcolor=cell_bgcolor,
            border=cell_border,
            border_radius=8,
            width=110,
            height=70,
            alignment=fl.alignment.center,
            on_click=lambda e: open_event_dialog(day, slot_number),
            ink=True,
        )

    def create_header_cell(text: str, is_time=False):
        return fl.Container(
            content=fl.Text(
                text,
                size=12 if is_time else 14,
                weight=fl.FontWeight.BOLD,
                color="white" if not is_time else "#B0B0B0",
                text_align=fl.TextAlign.CENTER,
            ),
            bgcolor="#1E1E1E",
            border=fl.border.all(1, "#3D3D3D"),
            border_radius=8,
            width=100 if is_time else 110,
            height=50,
            alignment=fl.alignment.center,
        )

    def create_slot_header(slot):
        return fl.Container(
            content=fl.Column(
                controls=[
                    fl.Text(
                        f"Turno {slot.number}",
                        size=12,
                        weight=fl.FontWeight.BOLD,
                        color="#FF9800",
                    ),
                    fl.Text(f"{slot.start_time}", size=10, color="#B0B0B0"),
                    fl.Text(f"{slot.end_time}", size=10, color="#B0B0B0"),
                ],
                horizontal_alignment=fl.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
            bgcolor="#1E1E1E",
            border=fl.border.all(1, "#3D3D3D"),
            border_radius=8,
            width=100,
            height=70,
            alignment=fl.alignment.center,
        )

    def empty_state(icon, text, size=60):
        return fl.Container(
            content=fl.Column(
                controls=[
                    fl.Icon(icon, size=size, color="#858585"),
                    fl.Text(
                        text, size=16, color="#858585", text_align=fl.TextAlign.CENTER
                    ),
                ],
                horizontal_alignment=fl.CrossAxisAlignment.CENTER,
                alignment=fl.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            expand=True,
            alignment=fl.alignment.center,
        )

    def rebuild_schedule_table():
        schedule = temp_save.get_schedule()
        days = schedule.get_days()
        slots = schedule.time_slots

        if not days:
            schedule_table_container.content = empty_state(
                fl.Icons.CALENDAR_TODAY, "Configura los días para ver el horario"
            )
            return

        rows = [
            fl.Row(
                controls=[create_header_cell("Turno / Hora", is_time=True)]
                + [create_header_cell(day) for day in days],
                spacing=5,
            )
        ]

        if not slots:
            rows.append(
                fl.Row(
                    controls=[
                        empty_state(
                            fl.Icons.HOURGLASS_TOP,
                            "Agrega turnos en el panel izquierdo",
                            size=40,
                        )
                    ],
                    expand=True,
                )
            )
        else:
            for slot in slots:
                rows.append(
                    fl.Row(
                        controls=[create_slot_header(slot)]
                        + [create_event_cell(day, slot.number) for day in days],
                        spacing=5,
                    )
                )

        schedule_table_container.content = fl.Container(
            content=fl.Column(controls=rows, spacing=5, scroll=fl.ScrollMode.AUTO),
            padding=10,
        )

    # ╚¤═══════¤TABLA¤════════¤╝

    # ╔¤═══════¤LAYOUT¤════════¤╗
    left_panel = fl.Container(
        content=fl.Column(
            controls=[
                fl.Row(
                    controls=[
                        fl.Text(
                            "📅 Rango de Días",
                            size=16,
                            weight=fl.FontWeight.BOLD,
                            color="white",
                            expand=True,
                        ),
                        apply_days_button,
                    ],
                    alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=fl.CrossAxisAlignment.CENTER,
                ),
                fl.Row(
                    controls=[
                        dropdown_start_day,
                        fl.Text("→", size=16, color="white"),
                        dropdown_end_day,
                    ],
                    spacing=5,
                    vertical_alignment=fl.CrossAxisAlignment.CENTER,
                ),
                fl.Divider(height=15, color="#3D3D3D"),
                fl.Row(
                    controls=[
                        fl.Text(
                            "⏰ Turnos",
                            size=16,
                            weight=fl.FontWeight.BOLD,
                            color="white",
                        ),
                        add_slot_button,
                    ],
                    alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                ),
                fl.Container(
                    content=slots_list,
                    expand=True,
                    border=fl.border.all(1, "#3D3D3D"),
                    border_radius=8,
                    padding=5,
                ),
            ],
            spacing=10,
            expand=True,
        ),
        width=280,
        padding=10,
        bgcolor="#1E1E1E",
        border_radius=8,
    )

    legend_chip = lambda text, color: fl.Container(  # noqa: E731
        content=fl.Text(text, size=10), bgcolor=color, border_radius=5, padding=5
    )

    right_panel = fl.Container(
        content=fl.Column(
            controls=[
                fl.Row(
                    controls=[
                        fl.Text(
                            "📋 Horario de Eventos",
                            size=20,
                            weight=fl.FontWeight.BOLD,
                            color="white",
                        ),
                        fl.Row(
                            controls=[
                                legend_chip("👥 Grupos", "#4CAF50"),
                                legend_chip("🧑 Humanos", "#FF9800"),
                                legend_chip("📍 Lugares", "#2196F3"),
                                legend_chip("📦 Objetos", "#9C27B0"),
                            ],
                            spacing=5,
                        ),
                    ],
                    alignment=fl.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=fl.CrossAxisAlignment.CENTER,
                ),
                fl.Divider(height=10, color="#3D3D3D"),
                schedule_table_container,
            ],
            spacing=10,
            expand=True,
        ),
        padding=15,
        expand=True,
        bgcolor="#1E1E1E",
        border_radius=8,
    )
    # ╚¤═══════¤LAYOUT¤════════¤╝

    rebuild_slots_list()
    rebuild_schedule_table()

    return fl.Row(controls=[left_panel, right_panel], spacing=10, expand=True)

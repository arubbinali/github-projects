import flet as ft

def main(page: ft.Page):
    page.title = "Flet Software"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#1e1e2e"

    def on_tab_change(e):
        page.controls.clear()
        page.controls.append(nav_bar)
        if tabs.selected_index == 0:
            page.controls.append(ft.Text("🏠 Home Tab", size=30, color="white"))
        elif tabs.selected_index == 1:
            page.controls.append(ft.Text("⚙️ Settings Tab", size=30, color="white"))
        elif tabs.selected_index == 2:
            page.controls.append(ft.Text("📄 About Tab", size=30, color="white"))
        page.update()

    tabs = ft.Tabs(
        selected_index=0,
        on_change=on_tab_change,
        tabs=[
            ft.Tab(text="Home"),
            ft.Tab(text="Settings"),
            ft.Tab(text="About"),
        ],
        indicator_color="blue",
        label_color="white",
    )

    nav_bar = ft.Row([tabs], alignment=ft.MainAxisAlignment.CENTER)
    page.add(nav_bar, ft.Text("🏠 Home Tab", size=30, color="white"))

ft.app(target=main)

import flet as ft

# Fallback for ft.colors and ft.icons for older Flet versions
if not hasattr(ft, "colors"):
    class _FallbackColors:
        def __getattr__(self, name):
            # Return a default color or raise AttributeError
            if name == "with_opacity":
                # with_opacity(opacity, color) just returns the base color in this fallback
                return lambda opacity, color: color
            return "#FFFFFF"
    ft.colors = _FallbackColors()

# Fallback for icons
if not hasattr(ft, "icons"):
    class _FallbackIcons:
        def __getattr__(self, name):
            return ""  # return empty string or default icon name
    ft.icons = _FallbackIcons()

# Patch ft.Tab to ignore unsupported parameters like 'selected_icon'
if hasattr(ft, "Tab"):
    _OriginalTab = ft.Tab
    def _PatchedTab(*args, **kwargs):
        kwargs.pop("selected_icon", None)
        return _OriginalTab(*args, **kwargs)
    ft.Tab = _PatchedTab

# Fallback for ft.Expanded
if not hasattr(ft, "Expanded"):
    class _FallbackExpanded(ft.Container):
        def __init__(self, child=None, *args, **kwargs):
            super().__init__(content=child, *args, **kwargs)
    ft.Expanded = _FallbackExpanded

# Patch GridView to map 'children' to 'controls'
if hasattr(ft, "GridView"):
    _OriginalGridView = ft.GridView
    def _PatchedGridView(*args, **kwargs):
        if 'children' in kwargs and 'controls' not in kwargs:
            kwargs['controls'] = kwargs.pop('children')
        return _OriginalGridView(*args, **kwargs)
    ft.GridView = _PatchedGridView
import webbrowser
import os
import json
import sys
from pathlib import Path
from typing import List, Dict, Optional, Callable
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize Tkinter for file dialogs
try:
    root = tk.Tk()
    root.withdraw()  # Hide the root window
except Exception as e:
    print(f"Warning: Could not initialize Tkinter: {e}")
    root = None

# Constants
PRIMARY_COLOR = "#7C4DFF"
SECONDARY_COLOR = "#448AFF"
ACCENT_COLOR = "#00B8D4"
DARK_BG = "#121212"
DARK_SURFACE = "#1E1E1E"
DARK_SURFACE_VARIANT = "#2D2D2D"
LIGHT_BG = "#F5F5F5"
LIGHT_SURFACE = "#FFFFFF"
LIGHT_SURFACE_VARIANT = "#F5F5F5"
ERROR_COLOR = "#CF6679"
SUCCESS_COLOR = "#69F0AE"

# Animation constants
ANIMATION_DURATION = 200  # ms
EASING = "easeInOut"

# Data file to store shortcuts
SHORTCUTS_FILE = "shortcuts.json"

class ShortcutManager:
    def __init__(self, filename='shortcuts.json'):
        self.filename = filename
        self.shortcuts = {}
        self.load_shortcuts()
    
    def load_shortcuts(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    # Load as list and convert to dict with IDs as keys
                    shortcuts_list = json.load(f)
                    self.shortcuts = {s['id']: s for s in shortcuts_list}
        except Exception as e:
            print(f"Error loading shortcuts: {e}")
            self.shortcuts = {}
    
    def save_shortcuts(self):
        try:
            with open(self.filename, 'w') as f:
                # Save as list for backward compatibility
                json.dump(list(self.shortcuts.values()), f, indent=2)
        except Exception as e:
            print(f"Error saving shortcuts: {e}")
    
    def add_shortcut(self, name: str, path: str, is_web: bool = False, icon: str = None, pinned: bool = False) -> bool:
        """Add a new shortcut and return True if successful"""
        try:
            # Generate a unique ID
            shortcut_id = max(self.shortcuts.keys(), default=0) + 1
            
            # Determine the best icon
            if not icon:
                if is_web:
                    icon = 'public'
                elif path.lower().endswith(('.exe', '.lnk')):
                    icon = 'apps'
                elif os.path.isdir(path):
                    icon = 'folder_open'
                else:
                    icon = 'insert_drive_file'
            
            shortcut = {
                'id': shortcut_id,
                'name': name,
                'path': path,
                'is_web': is_web,
                'icon': icon,
                'pinned': pinned,
                'created_at': datetime.now().isoformat(),
                'last_used': None
            }
            self.shortcuts[shortcut_id] = shortcut
            self.save_shortcuts()
            return True
        except Exception as e:
            print(f"Error adding shortcut: {e}")
            return False
    
    def get_pinned(self) -> List[Dict]:
        """Get all pinned shortcuts"""
        return [s for s in self.shortcuts.values() if s.get('pinned', False)]
    
    def get_recent(self, limit: int = 5) -> List[Dict]:
        """Get most recently used shortcuts"""
        try:
            return sorted(
                [s for s in self.shortcuts.values() if 'last_used' in s],
                key=lambda x: x['last_used'],
                reverse=True
            )[:limit]
        except:
            return []
    
    def toggle_pin(self, shortcut_id: int) -> bool:
        """Toggle pin status of a shortcut"""
        if shortcut_id in self.shortcuts:
            self.shortcuts[shortcut_id]['pinned'] = not self.shortcuts[shortcut_id].get('pinned', False)
            self.save_shortcuts()
            return self.shortcuts[shortcut_id]['pinned']
        return False
    
    def remove_shortcut(self, shortcut_id: int) -> bool:
        """Remove a shortcut by ID"""
        if shortcut_id in self.shortcuts:
            del self.shortcuts[shortcut_id]
            self.save_shortcuts()
            return True
        return False
    
    def update_shortcut(self, shortcut_id: int, **kwargs) -> bool:
        """Update shortcut properties"""
        if shortcut_id in self.shortcuts:
            self.shortcuts[shortcut_id].update(kwargs)
            self.save_shortcuts()
            return True
        return False
    
    def update_last_used(self, shortcut_id: int) -> bool:
        """Update last used timestamp of a shortcut"""
        if shortcut_id in self.shortcuts:
            self.shortcuts[shortcut_id]['last_used'] = datetime.now().isoformat()
            self.save_shortcuts()
            return True
        return False

def show_file_dialog(initial_dir=None, file_types=None):
    """Show file dialog and return selected path"""
    if not root:
        print("Tkinter not available for file dialog")
        return None
        
    try:
        file_path = filedialog.askopenfilename(
            initialdir=initial_dir or os.path.expanduser("~"),
            title="Select File or Application",
            filetypes=file_types or [
                ("All Files", "*"),
                ("Applications", "*.exe;*.lnk;*.app;*.appref-ms"),
                ("Documents", "*.pdf;*.docx;*.xlsx;*.pptx;*.txt;*.md"),
                ("Images", "*.png;*.jpg;*.jpeg;*.gif;*.webp;*.svg"),
                ("Videos", "*.mp4;*.avi;*.mov;*.mkv;*.webm"),
                ("Audio", "*.mp3;*.wav;*.ogg;*.m4a")
            ]
        )
        return file_path if file_path else None
    except Exception as e:
        print(f"Error in file dialog: {e}")
        return None

def show_folder_dialog(initial_dir=None):
    """Show folder dialog and return selected path"""
    if not root:
        print("Tkinter not available for folder dialog")
        return None
        
    try:
        folder_path = filedialog.askdirectory(
            initialdir=initial_dir or os.path.expanduser("~"),
            title="Select Folder",
            mustexist=True
        )
        return folder_path if folder_path else None
    except Exception as e:
        print(f"Error in folder dialog: {e}")
        return None

class ModernButton(ft.ElevatedButton):
    """A modern styled button with hover effects"""
    def __init__(self, *args, **kwargs):
        # Extract custom style properties
        bgcolor = kwargs.pop('bgcolor', None)
        color = kwargs.pop('color', None)
        padding = kwargs.pop('padding', ft.padding.symmetric(horizontal=24, vertical=12))
        radius = kwargs.pop('radius', 8)
        elevation = kwargs.pop('elevation', 0)
        
        super().__init__(*args, **kwargs)
        
        # Set default styles
        self.bgcolor = bgcolor or ft.colors.TRANSPARENT
        self.color = color or ft.colors.WHITE
        self.elevation = elevation
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=radius),
            padding=padding,
            overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            animation_duration=ANIMATION_DURATION,
            bgcolor=ft.MaterialStateProperty.resolve_with(
                lambda states: (
                    ft.colors.with_opacity(0.9, self.bgcolor)
                    if ft.MaterialState.HOVERED in states
                    else self.bgcolor
                )
            ),
        )
        self.on_hover = self.animate_button
    
    def animate_button(self, e):
        if e.data == "true":
            self.elevation = min(4, self.elevation + 1)
            self.update()
        else:
            self.elevation = max(0, self.elevation - 1)
            self.update()

def show_snackbar(message: str, is_error: bool = False):
    """Show a snackbar message at the bottom of the screen"""
    if not hasattr(show_snackbar, 'page'):
        return
        
    try:
        show_snackbar.page.snack_bar = ft.SnackBar(
            content=ft.Text(
                message,
                color=ft.colors.WHITE,
                weight=ft.FontWeight.W_500,
            ),
            bgcolor=ERROR_COLOR if is_error else SUCCESS_COLOR,
            behavior=ft.SnackBarBehavior.FLOATING,
            shape=ft.RoundedRectangleBorder(radius=8),
            margin=20,
            padding=ft.padding.symmetric(horizontal=20, vertical=16),
        )
        show_snackbar.page.snack_bar.open = True
        show_snackbar.page.update()
    except Exception as e:
        print(f"Error showing snackbar: {e}")

class EmptyState(ft.Container):
    """A widget to display when there's no content to show"""
    def __init__(
        self,
        page: ft.Page,
        title: str = "Nothing here yet",
        message: str = "Add something to get started",
        icon: str = "inbox",
        on_add_click=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.page = page
        
        self.title = title
        self.message = message
        self.icon = icon
        self.on_add_click = on_add_click
        
        self.padding = 40
        self.alignment = ft.alignment.center
        self.expand = True
        
        # Create the content
        self.content = ft.Column(
            [
                # Icon container with subtle background
                ft.Container(
                    content=ft.Icon(
                        name=self.icon,
                        size=48,
                        color=PRIMARY_COLOR
                    ),
                    padding=20,
                    bgcolor=f"{PRIMARY_COLOR}20",  # 20% opacity
                    border_radius=20,
                    margin=ft.margin.only(bottom=16)
                ),
                # Title
                ft.Text(
                    self.title,
                    size=20,
                    weight=ft.FontWeight.W_600,
                    text_align=ft.TextAlign.CENTER,
                    color=DARK_BG if self.page.theme_mode == ft.ThemeMode.LIGHT else LIGHT_BG
                ),
                # Message
                ft.Container(
                    content=ft.Text(
                        self.message,
                        size=14,
                        color=DARK_SURFACE_VARIANT if self.page.theme_mode == ft.ThemeMode.LIGHT else LIGHT_SURFACE_VARIANT,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    margin=ft.margin.only(top=8, bottom=24),
                    width=300
                ),
                # Action button
                ft.ElevatedButton(
                    text="Add New",
                    icon="add",
                    on_click=self._on_add_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.symmetric(horizontal=24, vertical=12),
                        overlay_color=f"{PRIMARY_COLOR}20"  # 20% opacity
                    )
                ) if on_add_click else None
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        )
    
    def _on_add_click(self, e):
        if callable(self.on_add_click):
            self.on_add_click(e)


class AppCard(ft.Card):
    """A modern card for app shortcuts with hover effects and actions"""
    def __init__(self, shortcut, on_click=None, on_pin=None, show_pin=True):
        super().__init__()
        self.shortcut = shortcut
        self.on_click_callback = on_click
        self.on_pin_callback = on_pin
        
        # Card styling
        self.elevation = 1
        self.margin = 6
        self.shape = ft.RoundedRectangleBorder(radius=16)
        self.hover_elevation = 4
        self.hover_scale = 1.02
        self.animation = ft.Animation(ANIMATION_DURATION, ft.AnimationCurve.EASE_IN_OUT)
        
        # Card content
        self.icon_container = ft.Container(
            content=ft.Icon(
                name=shortcut.get('icon', 'apps'),
                size=36,
                color=PRIMARY_COLOR if shortcut.get('pinned') else ft.colors.GREY_600
            ),
            width=60,
            height=60,
            border_radius=12,
            bgcolor=ft.colors.with_opacity(
                0.1,
                PRIMARY_COLOR if shortcut.get('pinned') else ft.colors.GREY_600
            ),
            alignment=ft.alignment.center,
            animate_scale=self.animation,
        )
        
        # App name with ellipsis for long names
        name_text = ft.Text(
            shortcut['name'],
            weight=ft.FontWeight.W_500,
            size=14,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
            tooltip=shortcut['name'],
        )
        
        # Path/URL text (truncated)
        path_text = ft.Text(
            shortcut['path'],
            size=12,
            color=ft.colors.GREY_500,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
            tooltip=shortcut['path'],
        )
        
        # Pin button
        self.pin_button = ft.IconButton(
            icon=ft.icons.PUSH_PIN if shortcut.get('pinned') else ft.icons.PUSH_PIN_OUTLINED,
            icon_size=20,
            icon_color=PRIMARY_COLOR if shortcut.get('pinned') else ft.colors.GREY_500,
            tooltip="Pin/Unpin" if show_pin else None,
            visible=show_pin,
            on_click=self._on_pin_clicked,
        )
        
        # Main content container
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(
                            name=shortcut.get('icon', 'link'),
                            size=32,
                            color=PRIMARY_COLOR,
                        ),
                        width=64,
                        height=64,
                        border_radius=12,
                        bgcolor=f"{PRIMARY_COLOR}20",
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(bottom=8)
                    ),
                    ft.Text(
                        shortcut['name'],
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.W_500,
                        max_lines=2,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        width=120
                    ),
                    ft.Container(height=4) if not show_pin else ft.Container(),
                    ft.Row([
                        ft.IconButton(
                            icon="star" if shortcut.get('pinned') else "star_border",
                            icon_size=16,
                            on_click=self.toggle_pin,
                            tooltip="Pin/Unpin",
                            icon_color=ft.colors.AMBER if shortcut.get('pinned') else ft.colors.GREY_600,
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER) if show_pin else ft.Container()
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
                width=120,
                height=140,
            ),
            padding=12,
            on_click=self._on_click,
            border_radius=12,
            ink=True,
            tooltip=f"Open {shortcut['name']}\n{shortcut['path']}",
        )
    
    def _on_click(self, e):
        # Animate click
        self.content.scale = 0.95
        self.update()
        
        # Reset animation
        def reset():
            self.content.scale = 1.0
            self.update()
            
        # Trigger callback after animation
        def trigger_callback():
            if self.on_click_callback:
                self.on_click_callback(self.shortcut)
        
        import asyncio
        asyncio.create_task(self._animate_click(reset, trigger_callback))
    
    async def _animate_click(self, reset_callback, click_callback):
        await asyncio.sleep(100)  # 100ms for click animation
        reset_callback()
        click_callback()
    
    def _on_hover(self, e):
        self.elevation = self.hover_elevation if e.data == "true" else 1
        self.content.scale = self.hover_scale if e.data == "true" else 1.0
        
        # Animate icon on hover
        if e.data == "true":
            self.icon_container.scale = 1.1
        else:
            self.icon_container.scale = 1.0
            
        self.update()
    
    def _on_pin_clicked(self, e):
        if self.on_pin_callback:
            # Animate pin click
            self.pin_button.icon = ft.icons.PUSH_PIN if not self.shortcut.get('pinned') else ft.icons.PUSH_PIN_OUTLINED
            self.pin_button.icon_color = PRIMARY_COLOR if not self.shortcut.get('pinned') else ft.colors.GREY_500
            
            # Update pin status
            pinned = self.on_pin_callback(self.shortcut['id'])
            self.shortcut['pinned'] = pinned
            
            # Update icon color based on pin status
            self.icon_container.bgcolor = ft.colors.with_opacity(
                0.1,
                PRIMARY_COLOR if pinned else ft.colors.GREY_600
            )
            
            # Update icon color
            self.icon_container.content.color = PRIMARY_COLOR if pinned else ft.colors.GREY_600
            
            self.update()
            
            # Show feedback
            show_snackbar(f"{self.shortcut['name']} {'pinned' if pinned else 'unpinned'}")
    
    def toggle_pin(self, e):
        if self.on_pin_callback:
            pinned = self.on_pin_callback(self.shortcut['id'])
            self.shortcut['pinned'] = pinned
            
            # Update icon color based on pin status
            self.icon_container.bgcolor = ft.colors.with_opacity(
                0.1,
                PRIMARY_COLOR if pinned else ft.colors.GREY_600
            )
            
            # Update icon color
            self.icon_container.content.color = PRIMARY_COLOR if pinned else ft.colors.GREY_600
            
            # Update pin button
            self.pin_button.icon = ft.icons.PUSH_PIN if pinned else ft.icons.PUSH_PIN_OUTLINED
            self.pin_button.icon_color = PRIMARY_COLOR if pinned else ft.colors.GREY_500
            
            self.update()
            
            # Show feedback
            show_snackbar(f"{self.shortcut['name']} {'pinned' if pinned else 'unpinned'}")

def main(page: ft.Page):
    # Page setup
    page.title = "App Launcher Pro"
    page.padding = 0
    # Ensure dark theme by default
    page.theme_mode = getattr(ft.ThemeMode, "DARK", "dark")
    page.window_width = 1280
    page.window_height = 800
    page.window_resizable = True
    page.window_maximizable = True
    page.window_minimizable = True
    
    # Set window icon if available
    try:
        if hasattr(sys, '_MEIPASS'):
            # Running as PyInstaller bundle
            icon_path = os.path.join(sys._MEIPASS, 'assets', 'icon.ico')
        else:
            # Running in development
            icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico')
            
        if os.path.exists(icon_path):
            page.window_icon = icon_path
    except Exception as e:
        print(f"Could not set window icon: {e}")
    # Initialize shortcut manager
    shortcut_manager = ShortcutManager()

    # Add some default shortcuts if none exist
    if not shortcut_manager.shortcuts:
        shortcut_manager.add_shortcut("GitHub", "https://github.com", is_web=True, pinned=True)
        shortcut_manager.add_shortcut("Discord", "https://discord.com", is_web=True, pinned=True)
        shortcut_manager.add_shortcut("Settings", "ms-settings:", pinned=True)
        shortcut_manager.add_shortcut("File Explorer", "explorer.exe", pinned=True)
    
    # Create app bar with theme toggle and search
    def create_app_bar():
        return ft.AppBar(
            leading_width=40,
            title=ft.Row(
                [
                    ft.Icon(ft.icons.ROCKET_LAUNCH, color=PRIMARY_COLOR, size=28),
                    ft.Text("App Launcher Pro", size=20, weight=ft.FontWeight.W_600),
                ],
                spacing=12,
            ),
            center_title=False,
            bgcolor=colors["surface"],
            elevation=0,
            toolbar_height=64,
            actions=[
                # Search field
                ft.Container(
                    content=search_field,
                    margin=ft.margin.only(right=16),
                    alignment=ft.alignment.center_right,
                ),
                # Theme toggle
                ft.IconButton(
                    icon=ft.icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE,
                    icon_color=colors["on_surface"],
                    tooltip="Toggle theme",
                    on_click=toggle_theme,
                ),
            ],
        )
    
    # Create tab content for Home (pinned apps)
    def create_home_tab():
        pinned_shortcuts = [s for s in shortcut_manager.shortcuts.values() if s.get('pinned')]
        
        if not pinned_shortcuts:
            return ft.Container(
                content=EmptyState(
                    page=page,
                    title="No Pinned Apps",
                    message="Pin your favorite apps to see them here",
                    icon="push_pin",
                    on_add_click=lambda e: setattr(tabs, 'selected_index', 2)  # Switch to Add New tab
                ),
                expand=True,
            )
        
        # Create a responsive grid of app cards
        return ft.GridView(
            runs_count=4,
            max_extent=180,
            child_aspect_ratio=0.9,
            spacing=16,
            run_spacing=16,
            padding=24,
            expand=True,
            controls=[
                AppCard(
                    shortcut=shortcut,
                    on_click=launch_shortcut,
                    on_pin=toggle_pin,
                    show_pin=True
                ) for shortcut in pinned_shortcuts
            ]
        )
    
    # Create tab content for All Apps
    def create_all_apps_tab():
        if not shortcut_manager.shortcuts:
            return ft.Container(
                content=EmptyState(
                    title="No Apps Found",
                    message="Add your first app to get started",
                    icon="apps",
                    on_add_click=lambda e: setattr(tabs, 'selected_index', 2)  # Switch to Add New tab
                ),
                expand=True,
            )
        
        # Create a responsive grid of all app cards
        return ft.Column(
            [
                # Search results count
                ft.Container(
                    content=ft.Text(
                        f"{len(shortcut_manager.shortcuts)} apps",
                        size=14,
                        color=colors["on_surface"],
                        weight=ft.FontWeight.W_500,
                    ),
                    padding=ft.padding.symmetric(horizontal=24, vertical=8),
                    alignment=ft.alignment.center_left,
                ),
                # App grid
                ft.Expanded(
                    child=ft.GridView(
                        runs_count=5,
                        max_extent=180,
                        child_aspect_ratio=0.9,
                        spacing=16,
                        run_spacing=16,
                        padding=ft.padding.only(left=24, right=24, bottom=24),
                        controls=[
                            AppCard(
                                shortcut=shortcut,
                                on_click=launch_shortcut,
                                on_pin=toggle_pin,
                                show_pin=True
                            ) for shortcut in shortcut_manager.shortcuts.values()
                        ]
                    )
                )
            ],
            spacing=0,
            expand=True,
        )
    
    # Function to launch a shortcut
    def launch_shortcut(shortcut):
        try:
            if shortcut.get('is_web'):
                webbrowser.open(shortcut['path'])
            else:
                os.startfile(shortcut['path'])
            show_snackbar(f"Opened {shortcut['name']}")
        except Exception as e:
            show_snackbar(f"Error opening {shortcut['name']}: {str(e)}", is_error=True)
    
    # Function to toggle pin status
    def toggle_pin(shortcut_id):
        return shortcut_manager.toggle_pin(shortcut_id)
    
    # Set up the main layout
    def setup_ui():
        # Update tab contents
        tabs.tabs[0].content.content = create_home_tab()
        tabs.tabs[1].content.content = create_all_apps_tab()
        
        # Set up the main layout
        page.add(
            ft.Column(
                [
                    create_app_bar(),
                    ft.Divider(height=1, color=colors["surface_variant"]),
                    ft.Container(
                        content=tabs,
                        expand=True,
                        bgcolor=colors["bg"]
                    )
                ],
                spacing=0,
                expand=True
            )
        )
        
        # Update the UI
        page.update()
    
    
    # Handle window close event
    def on_window_close(e):
        # Save shortcuts before closing
        shortcut_manager.save_shortcuts()
        page.window_destroy()
    
    page.window_prevent_close = True
    page.on_window_event = lambda e: on_window_close(e) if e.data == "close" else None

    # Theme colors
    def get_theme_colors():
        is_dark = page.theme_mode == ft.ThemeMode.DARK
        return {
            "bg": DARK_BG if is_dark else LIGHT_BG,
            "surface": DARK_SURFACE if is_dark else LIGHT_SURFACE,
            "surface_variant": DARK_SURFACE_VARIANT if is_dark else LIGHT_SURFACE_VARIANT,
            "on_bg": "#FFFFFF" if is_dark else "#000000",
            "on_surface": "#E6E6E6" if is_dark else "#333333",
            "primary": PRIMARY_COLOR,
            "primary_variant": ft.colors.with_opacity(0.2, PRIMARY_COLOR),
            "secondary": SECONDARY_COLOR,
            "accent": ACCENT_COLOR,
            "error": ERROR_COLOR,
            "success": SUCCESS_COLOR
        }

    colors = get_theme_colors()

    # Update colors when theme changes
    def update_theme(e=None):
        nonlocal colors
        colors = get_theme_colors()
        page.update()

    # Toggle theme function
    def toggle_theme(e=None):
        page.theme_mode = (
            ft.ThemeMode.LIGHT 
            if page.theme_mode == ft.ThemeMode.DARK 
            else ft.ThemeMode.DARK
        )
        update_theme()

    # Search field
    search_field = ft.TextField(
        hint_text="Search apps...",
        prefix_icon=ft.icons.SEARCH,
        border_radius=20,
        height=40,
        width=300,
        text_size=14,
        content_padding=10,
        border_color=colors["surface_variant"],
        focused_border_color=PRIMARY_COLOR,
    )

    # Tabs with modern styling
    global tabs
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=ANIMATION_DURATION,
        label_color=PRIMARY_COLOR,
        unselected_label_color=ft.colors.GREY_500,
        indicator_color=PRIMARY_COLOR,
        indicator_tab_size=True,
        divider_color=ft.colors.TRANSPARENT,
        tabs=[
            ft.Tab(
                text="Home",
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME,
                content=ft.Container(padding=0, expand=True)
            ),
            ft.Tab(
                text="All Apps",
                icon=ft.icons.APPS_OUTLINED,
                selected_icon=ft.icons.APPS,
                content=ft.Container(padding=0, expand=True)
            ),
            ft.Tab(
                text="Add New",
                icon=ft.icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.icons.ADD_CIRCLE,
                content=ft.Container(padding=0, expand=True)
            ),
            ft.Tab(
                text="About",
                icon=ft.icons.INFO_OUTLINE,
                selected_icon=ft.icons.INFO,
                content=ft.Container(padding=0, expand=True)
            )
        ],
        expand=True
    )
    
    # Function to create a shortcut card
    def create_shortcut_card(shortcut, on_click=None, show_pin=True):
        return AppCard(
            shortcut=shortcut,
            on_click=on_click or (lambda e: None),
            on_pin=toggle_pin if show_pin else None,
            show_pin=show_pin
        )
    
    # Function to open a shortcut
    def open_shortcut(shortcut, new_tab=False):
        if shortcut['is_web']:
            webbrowser.open(shortcut['path'])
        else:
            os.startfile(shortcut['path'])
    
    # Function to toggle pin status of a shortcut
    def toggle_pin_shortcut(shortcut_id):
        shortcut_manager.toggle_pin(shortcut_id)
        update_ui()
    
    # Function to update the UI
    def update_ui():
        # Update home tab
        home_grid.controls = [
            create_shortcut_card(s, lambda e, s=s: open_shortcut(s, True))
            for s in shortcut_manager.get_pinned()
        ]
        
        # Update all apps tab
        all_apps_grid.controls = [
            create_shortcut_card(s, lambda e, s=s: open_shortcut(s, True))
            for s in shortcut_manager.shortcuts.values()
        ]
        
        page.update()
    
    # Create UI elements
    home_grid = ft.GridView(
        expand=True,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1,
        spacing=20,
        run_spacing=20,
        padding=20
    )
    
    all_apps_grid = ft.GridView(
        expand=True,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1,
        spacing=20,
        run_spacing=20,
        padding=20
    )
    
    # Add new shortcut form
    new_shortcut_name = ft.TextField(label="Name", expand=True)
    new_shortcut_path = ft.TextField(label="Path or URL", expand=True)
    new_shortcut_is_web = ft.Checkbox(label="Web Link", value=True)
    
    def add_new_shortcut(e):
        name = new_shortcut_name.value.strip()
        path = new_shortcut_path.value.strip()
        is_web = new_shortcut_is_web.value
        
        if name and path:
            shortcut_manager.add_shortcut(name, path, is_web)
            new_shortcut_name.value = ""
            new_shortcut_path.value = ""
            update_ui()
            tabs.selected_index = 1  # Switch to All Apps tab
            page.update()
    
    add_new_form = ft.Container(
        content=ft.Column(
            [
                ft.Text("Add New Shortcut", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                new_shortcut_name,
                new_shortcut_path,
                new_shortcut_is_web,
                ft.ElevatedButton(
                    "Add Shortcut",
                    on_click=add_new_shortcut,
                    icon="add"
                )
            ],
            spacing=15,
            width=400,
        ),
        padding=20,
        bgcolor=colors['surface'],
        border_radius=10,
        margin=20
    )
    
    # About tab content
    about_content = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(
                            src="https://avatars.githubusercontent.com/u/your_github_id",
                            width=100,
                            height=100,
                            fit=ft.ImageFit.COVER,
                            border_radius=50
                        ),
                        ft.Column(
                            [
                                ft.Text("Arub Binali", size=28, weight=ft.FontWeight.BOLD),
                                ft.Text("Software Developer"),
                                ft.Row(
                                    [
                                        ft.IconButton(
                                            icon="email",
                                            on_click=lambda _: webbrowser.open("mailto:arubbinali@outlook.com"),
                                            tooltip="Email me"
                                        ),
                                        ft.IconButton(
                                            icon="code",
                                            on_click=lambda _: webbrowser.open("https://github.com/arubbinali"),
                                            tooltip="GitHub"
                                        ),
                                        ft.IconButton(
                                            icon="link",
                                            on_click=lambda _: webbrowser.open("https://linkedin.com/in/arubbinali"),
                                            tooltip="LinkedIn"
                                        )
                                    ]
                                )
                            ],
                            spacing=10
                        )
                    ],
                    spacing=20
                ),
                ft.Divider(),
                ft.Text("About Me", size=20, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "I'm a passionate software developer with expertise in building modern applications. "
                    "This App Launcher helps you organize and quickly access your favorite applications and web links.",
                    size=14
                ),
                ft.Text("\nSkills", size=18, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(skill),
                            padding=ft.padding.all(10),
                            bgcolor=colors['surface'],
                            border_radius=10,
                            margin=ft.margin.only(right=5, bottom=5)
                        )
                        for skill in ["Python", "JavaScript", "React", "Node.js", "Flet", "Flask", "Docker"]
                    ],
                    wrap=True,
                    spacing=5,
                    run_spacing=5,
                    scroll=ft.ScrollMode.AUTO
                )
            ],
            spacing=20
        ),
        padding=20,
        expand=True
    )
    
    # Set tab contents
    tabs.tabs[0].content = ft.Container(content=home_grid, expand=True)
    tabs.tabs[1].content = ft.Container(content=all_apps_grid, expand=True)
    tabs.tabs[2].content = ft.Container(content=add_new_form, expand=True, alignment=ft.alignment.center)
    tabs.tabs[3].content = about_content

    # Build overall layout now that tabs is ready
    setup_ui()    
    # Add everything to the page
    page.add(tabs)
    
    # Initial UI update
    update_ui()

if __name__ == "__main__":
    ft.app(target=main)

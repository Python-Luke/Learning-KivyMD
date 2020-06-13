from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.card import MDCardSwipe
from kivy.lang import Builder
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine

from custompy.customdialogs import CustomDialogs
from custompy.custompickers import CustomPickers


class MDTextFieldsScreen(MDScreen):
    pass


class MDButtonsScreen(MDScreen):
    pass


class MDToastScreen(MDScreen):
    pass


class MDDialogsScreen(MDScreen):
    pass


class MDChipsScreen(MDScreen):
    pass


class MDPickersScreen(MDScreen):
    pass


class MDSwitchesScreen(MDScreen):
    pass


class MDMenuScreen(MDScreen):
    pass


class MDCardScreen(MDScreen):
    pass


class MDCardSwipeScreen(MDScreen):
    pass


class MDExpansionPanelScreen(MDScreen):
    pass


class MDBottomNavigationScreen(MDScreen):
    pass


class MDBottomSheetScreen(MDScreen):
    pass


class SwipeToDeleteItem(MDCardSwipe):
    """Card with `swipe-to-delete` behavior."""

    text = StringProperty()


class DrawerContent(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CustomToolbar(
    ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color


class ExpansionPanelContent(MDBoxLayout):
    pass


class MainDemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Green'
        return Builder.load_file('main.kv')

    def on_bottom_navigation(self):
        # Without this, the bottom bar is positioned weird
        self.root.ids.MD_bottom_navigation_screen.ids.bottom_navigation.on_resize()

    def on_start(self):
        self.root.ids.nav_drawer.swipe_distance = 100
        self.custom_dialogs = CustomDialogs()
        self.custom_pickers = CustomPickers()

        # Set up the menus for the menu screen
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        self.menu_1 = MDDropdownMenu(
            caller=self.root.ids.MD_menu_screen.ids.button_1, items=menu_items, width_mult=4)
        self.menu_2 = MDDropdownMenu(
            caller=self.root.ids.MD_menu_screen.ids.custom_toolbar.ids.button_2, items=menu_items, width_mult=4)

        # Set up the swipe cards for card screen
        for i in range(10):
            self.root.ids.MD_card_swipe_screen.ids.MD_card_swipe_demo.add_widget(SwipeToDeleteItem(text=f'Item {i}'))
            self.root.ids.MD_expansion_panel_screen.ids.box.add_widget(
                MDExpansionPanel(
                    icon=r'kivymd/images/kivymd_logo.png',
                    content=ExpansionPanelContent(),
                    panel_cls=MDExpansionPanelThreeLine(
                        text="Text",
                        secondary_text="Secondary text",
                        tertiary_text="Tertiary text",
                    )
                )
            )

        # Update the current toolbar
        current_screen = self.root.ids.screen_manager.current
        self.root.ids[current_screen].ids.toolbar.left_action_items = [
            ['menu', lambda x: self.root.ids.nav_drawer.set_state('toggle')]]
        

    def change_screen(self, screen_name):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name
        # Update the current active toolbar
        self.root.ids[screen_name].ids.toolbar.left_action_items = [
            ['menu', lambda x: self.root.ids.nav_drawer.set_state('toggle')]]

    def toast(self, instance, value):
        toast(value)

    def remove_item(self, instance):
        self.root.ids.MD_card_swipe_screen.ids.MD_card_swipe_demo.remove_widget(instance)


if __name__ == '__main__':
    MainDemoApp().run()
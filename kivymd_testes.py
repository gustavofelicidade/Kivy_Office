import kivy
import kivymd

''' Testes da biblioteca KivyMD'''

#======================================================================================================================
#2.1.2 First KivyMD application
#
#=======================================================================================================================

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):


    def build(self):
        return MDLabel(text="Hello, World", halign="center")

#======================================================================================================================
#2.2 Themes
#
#=======================================================================================================================

'''2.2.1 Theming'''

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons

colors = {
    "Teal": {
        "50": "e4f8f9",
        "100": "bdedf0",
        "200": "97e2e8",
        "300": "79d5de",
        "400": "6dcbd6",
        "500": "6ac2cf",
        "600": "63b2bc",
        "700": "5b9ca3",
        "800": "54888c",
        "900": "486363",
        "A100": "bdedf0",
        "A200": "97e2e8",
        "A400": "6dcbd6",
        "A700": "5b9ca3",
    },

    "Blue": {
        "50": "e3f3f8",
        "100": "b9e1ee",
        "200": "91cee3",
        "300": "72bad6",
        "400": "62acce",
        "500": "589fc6",
        "600": "5191b8",
        "700": "487fa5",
        "800": "426f91",
        "900": "35506d",
        "A100": "b9e1ee",
        "A200": "91cee3",
        "A400": "62acce",
        "A700": "487fa5",
    },

    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },

    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }

}

KV = '''
MDBoxLayout:
    orientation: "vertical"
    
    MDToolbar:
        title: "Example Tabs"
    MDTabs:
        id: tabs
        
<Tab>

    MDIconButton:
        id: icon
        icon: root.icon
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

    icon = ObjectProperty()


class Example(MDApp):

    icons = list(md_icons.keys())[15:30]

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        for name_tab in self.icons:
            tab = Tab(text="This is " + name_tab, icon=name_tab)
            self.root.ids.tabs.add_widget(tab)

Example().run()

#======================================================================================================================
#API - kivymd.theming
#=======================================================================================================================

class kivymd.theming.ThemeManager(**kwargs)

'''To change the color scheme of an application:'''

from kivymd.app import MDApp
from kivymd.screen import MDScreen

from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green" # "Purple", "Red"
        screen = MDScreen()

        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen
MainApp().run()

'''primary_palette is an OptionProperty and defaults to ‘Blue’.

primary_hue
    The color hue of the application.
    Available options are: ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’,
    ‘A400’, ‘A700’.
    
    To change the hue color scheme of an application:'''

from kivymd.app import MDApp
from kivymd.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):


    def build(self):

        self.theme_cls.primary_palette = "Green" # "Purple", "Red"
        self.theme_cls.primary_hue = "200" # "500"

        screen = MDScreen()
        screen.add_widget(

            MDRectangleFlatButton(

                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()

'''
primary_hue = matiz primária:

    With a value of self.theme_cls.primary_hue = "500":
    With a value of self.theme_cls.primary_hue = "200":
   
'''

'''primary_hue is an OptionProperty e o padrão é ‘500’.

primary_light_hue

    Valor de matiz para primary_light.
    primary_light_hue is an OptionProperty and defaults to ‘200’.

primary_dark_hue

    Hue value for primary_dark.
    primary_light_hue is an OptionProperty and defaults to ‘700’.

primary_color

    The color of the current application theme in rgba format.
    primary_color is an AliasProperty that returns the value of the current application theme, property is
    readonly.

primary_light

    Colors of the current application color theme in rgba format (in lighter color).
'''

from kivy.lang import Builder
from kivymd.app import MDApp


KV = '''
MDScreen:
    MDRaisedButton:
        text: "primary_light"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_light
        
    MDRaisedButton:
        text: "primary_color"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        
    MDRaisedButton:
        text: "primary_dark"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark
'''

class MainApp(MDApp):


    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

MainApp().run()

'''
    primary_light é uma AliasProperty que retorna o valor do tema do aplicativo atual (em cor mais clara), 
    a propriedade é somente leitura.

primary_dark

    Cores do tema de cores do aplicativo atual em formato rgba  (in darker color).
    primary_dark é uma AliasProperty que retorna o valor do tema do aplicativo atual (in darker
    color), propriedade é somente leitura.
    
accent_palette

    A paleta de cores do aplicativo usada para itens como o indicador da guia no MDTabsBar class e assim por diante. . .
    TA imagem abaixo mostra os esquemas de cores com os valores self.theme_cls.accent_palette =
    'Blue', Red' e Yellow':

    accent_palette is an OptionProperty and defaults to ‘Amber’.

accent_hue

    Similar to primary_hue, but returns a value for accent_palette.
    accent_hue is an OptionProperty and defaults to ‘500’.

accent_light_hue
    Hue value for accent_light.
    accent_light_hue is an OptionProperty and defaults to ‘200’.

accent_dark_hue

Hue value for accent_dark.

accent_dark_hue is an OptionProperty and defaults to ‘700’.

accent_color
    Similar to primary_color, but returns a value for accent_color.
    accent_color is an AliasProperty that returns the value in rgba format for accent_color, property
    is readonly.

accent_light
    Similar to primary_light, but returns a value for accent_light.
    accent_light is an AliasProperty that returns the value in rgba format for accent_light, property
    is readonly.

accent_dark
    Similar to primary_dark, but returns a value for accent_dark.
    accent_dark is an AliasProperty that returns the value in rgba format for accent_dark, property is
    readonly.
    
App theme style.
    App theme style.

'''

from kivymd.app import MDApp
from kivymd.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
    self.theme_cls.theme_style = "Dark" # "Light"
    screen = MDScreen()
    screen.add_widget(
        MDRectangleFlatButton(
            text="Hello, World",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
    )
    return screen

MainApp().run()

KV = '''
MDBoxLayout:

    MDBoxLayout:
        md_bg_color: app.theme_cls.bg_light
    MDBoxLayout:
        md_bg_color: app.theme_cls.bg_normal
    MDBoxLayout:
        md_bg_color: app.theme_cls.bg_dark
    MDBoxLayout:
        md_bg_color: app.theme_cls.bg_darkest
'''
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):


    def build(self):
        self.theme_cls.theme_style = "Dark" # "Light"
        return Builder.load_string(KV)


MainApp().run()

'''bg_darkest is an AliasProperty that returns the value in rgba format for bg_darkest, property is
readonly.

opposite_bg_darkest
    The opposite value of color in the bg_darkest.
    opposite_bg_darkest is an AliasProperty that returns the value in rgba format for
    opposite_bg_darkest, property is readonly.

bg_dark
    Similar to bg_normal, but the color values are one tone lower (darker) than bg_normal.
    bg_dark is an AliasProperty that returns the value in rgba format for bg_dark, property is readonly.

opposite_bg_dark
    The opposite value of color in the bg_dark.

    opposite_bg_dark is an AliasProperty that returns the value in rgba format for opposite_bg_dark,
    property is readonly.

bg_normal
    Similar to bg_light, but the color values are one tone lower (darker) than bg_light.
    bg_normal is an AliasProperty that returns the value in rgba format for bg_normal, property is readonly.

opposite_bg_normal
    The opposite value of color in the bg_normal.
    opposite_bg_normal is an AliasProperty that returns the value in rgba format for
    opposite_bg_normal, property is readonly.

bg_light
    ” Depending on the style of the theme (‘Dark’ or ‘Light’) that the application uses, bg_light contains the
    color value in rgba format for the widgets background.
    bg_light is an AliasProperty that returns the value in rgba format for bg_light, property is readonly.

opposite_bg_light
    The opposite value of color in the bg_light.
    opposite_bg_light is an AliasProperty that returns the value in rgba format for
    opposite_bg_light, property is readonly.
'''

'''divider_color
Color for dividing lines such as MDSeparator.
divider_color is an AliasProperty that returns the value in rgba format for divider_color, property is readonly.
opposite_divider_color
The opposite value of color in the divider_color.
opposite_divider_color is an AliasProperty that returns the value in rgba format for
opposite_divider_color, property is readonly.
text_color
Color of the text used in the MDLabel.
text_color is an AliasProperty that returns the value in rgba format for text_color, property is
readonly.
opposite_text_color
The opposite value of color in the text_color.
opposite_text_color is an AliasProperty that returns the value in rgba format for
opposite_text_color, property is readonly.
secondary_text_color
The color for the secondary text that is used in classes from the module TwoLineListItem.
secondary_text_color is an AliasProperty that returns the value in rgba format for
secondary_text_color, property is readonly.
opposite_secondary_text_color
The opposite value of color in the secondary_text_color.
opposite_secondary_text_color is an AliasProperty that returns the value in rgba format for
opposite_secondary_text_color, property is readonly.
icon_color
Color of the icon used in the MDIconButton.
icon_color is an AliasProperty that returns the value in rgba format for icon_color, property is
readonly.
opposite_icon_color
The opposite value of color in the icon_color.
opposite_icon_color is an AliasProperty that returns the value in rgba format for
opposite_icon_color, property is readonly.
disabled_hint_text_color
Color of the disabled text used in the MDTextField.
disabled_hint_text_color is an AliasProperty that returns the value in rgba format for
disabled_hint_text_color, property is readonly.
opposite_disabled_hint_text_color
The opposite value of color in the disabled_hint_text_color.
opposite_disabled_hint_text_color is an AliasProperty that returns the value in rgba format
for opposite_disabled_hint_text_color, property is readonly.
'''

'''
error_color
    Color of the error text used in the MDTextField.
    error_color is an AliasProperty that returns the value in rgba format for error_color, property is
    readonly.
'''

'''
ripple_color
Color of ripple effects.
ripple_color is an AliasProperty that returns the value in rgba format for ripple_color, property
is readonly.
device_orientation
Device orientation.
device_orientation is an StringProperty.
standard_increment
Value of standard increment.
standard_increment is an AliasProperty that returns the value in rgba format for
standard_increment, property is readonly.
horizontal_margins
Value of horizontal margins.
horizontal_margins is an AliasProperty that returns the value in rgba format for
horizontal_margins, property is readonly.
set_clearcolor
font_styles
Data of default font styles.
Add custom font:

'''

KV = '''
MDScreen:
MDLabel:
text: "JetBrainsMono"
halign: "center"
font_style: "JetBrainsMono"
'''


from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles


class MainApp(MDApp):


    def build(self):
        LabelBase.register(
            name="JetBrainsMono",
            fn_regular="JetBrainsMono-Regular.ttf")

        theme_font_styles.append('JetBrainsMono')
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
        ]


MainApp().run()

'''font_styles is an DictProperty.
on_theme_style(self, interval: int, theme_style: str)

set_clearcolor_by_theme_style(self, theme_style)

set_colors(self, primary_palette: str, primary_hue: str, primary_light_hue: str, primary_dark_hue: str,
            accent_palette: str, accent_hue: str, accent_light_hue: str, accent_dark_hue: str)
    Courtesy method to allow all of the theme color attributes to be set in one call.

set_colors allows all of the following to be set in one method call:
        • primary palette color,
        • primary hue,
        • primary light hue,
        • primary dark hue,
        • accent palette color,
        • accent hue,
        • accent ligth hue, and
        • accent dark hue.
    Note that all values must be provided. If you only want to set one or two values use the appropriate method
    call for that.

'''

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):
    def build(self):
        self.theme_cls.set_colors(
            "Blue", "600", "50", "800", "Teal", "600", "100", "800"
        )
        screen = MDScreen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen

MainApp().run()

'''
    sync_theme_styles(self, *args)

class kivymd.theming.ThemableBehavior(**kwargs)

theme_cls
    Instance of ThemeManager class.
    theme_cls is an ObjectProperty.

device_ios
    True if device is iOS.
    device_ios is an BooleanProperty.

widget_style
    Allows to set one of the three style properties for the widget: ‘android’, ‘ios’, ‘desktop’.
    For example, for the class MDSwitch has two styles - ‘android’ and ‘ios’:
    
    MDSwitch:
        widget_style: "ios"


    widget_style is an OptionProperty and defaults to ‘android’.

opposite_colors
    For some widgets, for example, for a widget MDToolbar changes the color of the label to the color opposite
    to the main theme.

    MDToolbar:
        title: "MDToolbar"
        opposite_colors: True
        
    MDToolbar:
        title: "MDToolbar"
        opposite_colors: True
        
        
'''

#======================================================================================================================
# 2.2.2 Material App
#=======================================================================================================================

'''This module contains MDApp class that is inherited from App. MDApp has some properties needed for KivyMD library
(like theme_cls). You can turn on the monitor displaying the current FPS value in your application:
'''

KV = '''
MDScreen:
MDLabel:
text: "Hello, World!"
halign: "center"
'''


from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.fps_monitor_start()


MainApp().run()

# API - kivymd.app

class kivymd.app.MDApp(**kwargs)

# Application class, see App class documentation for more information.
'''
    theme_cls
        Instance of ThemeManager class.'''

# Warning: The theme_cls attribute is already available in a class that is inherited from the MDApp
# class. The following code will result in an error!

#class MainApp(MDApp):
    #theme_cls = ThemeManager()
    #theme_cls.primary_palette = "Teal"

# Note: Correctly do as shown below!

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"


#======================================================================================================================
# 2.2.3 Color Definitions
#=======================================================================================================================

'''See also:
Material Design spec, The color system
Material Design spec, The color tool
Material colors palette to use in kivymd.theming.ThemeManager. colors is a dict-in-dict where the first key is a
value from palette and the second key is a value from hue. Color is a hex value, a string of 6 characters (0-9, A-F)
written in uppercase.
For example, colors["Red"]["900"] is "B71C1C".
'''

# API - kivymd.color_definitions

#kivymd.color_definitions.colors

'''
    Color palette. Taken from 2014 Material Design color palettes.
    To demonstrate the shades of the palette, you can run the following code:
'''

from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty, StringProperty

from kivymd.color_definitions import colors
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout


demo = '''
<Root@MDBoxLayout>
    orientation: 'vertical'
    
    MDToolbar:
        title: app.title

    MDTabs:
        id: android_tabs
        on_tab_switch: app.on_tab_switch(*args)
        size_hint_y: None
        height: "48dp"
        tab_indicator_anim: False
        
    RecycleView:
        id: rv
        key_viewclass: "viewclass"
        key_size: "height"
    RecycleBoxLayout:
        default_size: None, dp(48)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: "vertical"
        
<ItemColor>

    size_hint_y: None
    height: "42dp"

    MDLabel:
        text: root.text
        halign: "center"
        
<Tab>
'''

from kivy.factory import Factory

from kivymd.app import MDApp


class Tab(BoxLayout, MDTabsBase):
    pass


class ItemColor(MDBoxLayout):
    text = StringProperty()
    color = ListProperty()


class Palette(MDApp):
    title = "Colors definitions"

    def build(self):
        Builder.load_string(demo)
        self.screen = Factory.Root()

        for name_tab in colors.keys():
            tab = Tab(text=name_tab)
            self.screen.ids.android_tabs.add_widget(tab)
        return self.screen

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tabs_label, tab_text
    ):
        self.screen.ids.rv.data = []
        if not tab_text:
            tab_text = 'Red'
        for value_color in colors[tab_text]:
            self.screen.ids.rv.data.append(
                {
                    "viewclass": "ItemColor",
                    "md_bg_color": get_color_from_hex(colors[tab_text][value_color]),

                    "text": value_color,
                }
            )

        def on_start(self):
            self.on_tab_switch(
                None,
                None,
                None,
                self.screen.ids.android_tabs.ids.layout.children[-1].text,
            )

        
Palette().run()

'''

kivymd.color_definitions.palette = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo',
'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber',
'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
Valid values for color palette selecting.
kivymd.color_definitions.hue = ['50', '100', '200', '300', '400', '500', '600', '700',
'800', '900', 'A100', 'A200', 'A400', 'A700']
Valid values for color hue selecting.
kivymd.color_definitions.light_colors
Which colors are light. Other are dark.
kivymd.color_definitions.text_colors
Text colors generated from light_colors. “000000” for light and “FFFFFF” for dark.
How to generate text_colors dict

'''

text_colors = {}
for p in palette:
    text_colors[p] = {}
    for h in hue:
        if h in light_colors[p]:
            text_colors[p][h] = "000000"
        else:
            text_colors[p][h] = "FFFFFF"

kivymd.color_definitions.theme_colors = ['Primary', 'Secondary', 'Background', 'Surface',
'Error', 'On_Primary', 'On_Secondary', 'On_Background', 'On_Surface', 'On_Error']

#  Cores de tema válidas.

#======================================================================================================================
#
#2.2.4 Icon Definitions
#
#=======================================================================================================================


'''See also:
Material Design Icons'''


'''List of icons from materialdesignicons.com. These expanded material design icons are maintained by Austin Andrews
(Templarian on Github).
LAST UPDATED: Version 5.9.55
'''


## To preview the icons and their names, you can use the following application:Para visualizar os ícones e seus nomes, você pode usar o seguinte aplicativo:


from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem


Builder.load_string(
'''
#:import images_path kivymd.images_path

<CustomOneLineIconListItem>
    IconLeftWidget:
      icon: root.icon
      
<PreviousMDIcons>

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)
        
        MDBoxLayout:
        adaptive_height: True
        
    MDIconButton:
        icon: 'magnify'
        
    MDTextField:
        id: search_field
        hint_text: 'Search icon'
        on_text: root.set_list_md_icons(self.text, True)
        
    RecycleView:
        id: rv
        key_viewclass: 'viewclass'
        key_size: 'height'
        
        RecycleBoxLayout:
            padding: dp(10)
            default_size: None, dp(48)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

''')

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):


    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

    def add_icon_item(name_icon):
        self.ids.rv.data.append(
            {
            "viewclass": "CustomOneLineIconListItem",
            "icon": name_icon,
            "text": name_icon,
            "callback": lambda x: x,
            }
        )

    self.ids.rv.data = []
    for name_icon in md_icons.keys():
        if search:
            if text in name_icon:
                add_icon_item(name_icon)
        else:
            add_icon_item(name_icon)


class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()


MainApp().run()

# API - kivymd.icon_definitions
# kivymd.icon_definitions.md_icons


#======================================================================================================================
# 2.2.5 Font Definitions
#=======================================================================================================================


#See also:
#Material Design spec, The type system

# API - kivymd.font_definitions

kivymd.font_definitions.fonts
kivymd.font_definitions.theme_font_styles = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6',
'Subtitle1', 'Subtitle2', 'Body1', 'Body2', 'Button', 'Caption', 'Overline', 'Icon']

        
#======================================================================================================================
#
# 2.3 Components
#
#=======================================================================================================================

#=======================================================================================================================
# 2.3.1 Screen
#=======================================================================================================================

    # Screen class equivalent. Simplifies working with some widget properties. For example:Equivalente à classe de tela. Simplifica o trabalho com algumas propriedades de widget. Por exemplo:

    # Screen

'''Screen:
    canvas:
        Color:
            rgba: app.theme_cls.primary_color

        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [25, 0, 0, 0]'''


# MDScreen

'''
    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
'''

# API - kivymd.uix.screen

class kivymd.uix.screen.MDScreen(**kw)
"Screen is an element intended to be used with a ScreenManager. Check module documentation for more information."
'''
    Events
    
        on_pre_enter: () Event fired when the screen is about to be used: the entering animation is
            started.
        
        on_enter: () Event fired when the screen is displayed: the entering animation is complete.

        on_pre_leave: () Event fired when the screen is about to be removed: the leaving animation is
            started.

        on_leave: () Event fired when the screen is removed: the leaving animation is finished.


#Changed in version 1.6.0: Events on_pre_enter, on_enter, on_pre_leave and on_leave were added.

'''

#=======================================================================================================================
# 2.3.2 Menu
#=======================================================================================================================

#See also:
#Material Design spec, Menus

# Menus display a list of choices on temporary surfaces.

#Usage

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
KV = '''
MDScreen:
MDRaisedButton:
id: button
text: "PRESS ME"
pos_hint: {"center_x": .5, "center_y": .5}
on_release: app.menu.open()
'''
class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]

self.menu = MDDropdownMenu(
caller=self.screen.ids.button,
items=menu_items,
width_mult=4,
)
def menu_callback(self, text_item):
print(text_item)
def build(self):
return self.screen
Test().run()


PAGINA 33



#=======================================================================================================================
# 2.4.2 Elevation
#=======================================================================================================================


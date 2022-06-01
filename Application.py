import os

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import youtube_dl

Window.maximize()

# Kivy Builder:
image = """
AsyncImage:
    source: "https://i.ibb.co/3THLZcf/download-icon.png"
    pos_hint: {"center_x": 0.5, "center_y": 0.80}
"""

Picture="""
AsyncImage:
    source: ""
    pos_hint: {}
"""

label_link = """
MDTextField:
    hint_text: "Enter Link"
    icon_right: "link"
    icon_right_color: [0/255,170/255,255/255,1]

    pos_hint: {"center_x": 0.51, "center_y": 0.5}
    size_hint_x: 0.7
"""
# ^   helper_text: "Hinweis: Es gehen nur YouTube Links!"
#     helper_text_mode: "persistent"


# Variablen zum zwischenspeichern oder prüfen:
counter = 0
proof = False
selection = 1
# App Build Klasse:
class App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        screen.size_hint

        # Erstellen der Widgets
        self.images = Builder.load_string((image))

        self.icon_button = MDIconButton(icon="rocket", pos_hint={"center_x": 0.07, "center_y": 0.96}, on_release=self.click_counter)

        self.icon_button_switch = MDIconButton(icon="youtube", pos_hint={"center_x": 0.11, "center_y": 0.5028}, theme_text_color="Custom",
                                            text_color = (255/255.0, 0/255.0, 0/255.0, 1), on_release=self.swap) #clipboard-text

        self.label = MDLabel(text="0", pos_hint={"center_x": 0.595, "center_y": 0.96}, theme_text_color="Custom",
                                            text_color = (0/255.0, 140/255.0, 255/255.0, 1))

        self.link = Builder.load_string(label_link)

        self.button = MDRectangleFlatIconButton(icon="cloud-download", text="DOWNLOAD", theme_text_color="Custom",
                                            text_color = (0/255.0, 140/255.0, 255/255.0, 1), pos_hint={"center_x": 0.5, "center_y": 0.4},
                                            on_release=self.download_x_check_input)

        # Widgets aufrufen
        screen.add_widget(self.icon_button)
        screen.add_widget(self.icon_button_switch)
        screen.add_widget(self.label)
        screen.add_widget(self.images)
        screen.add_widget(self.link)
        screen.add_widget(self.button)
        return screen

    # Close Dialog Funktionen
    def close_dialog_iL(self, obj):
        self.error_dialog_invalidLink.dismiss()
    def close_dialog_nF(self, obj):
        self.error_dialog_notFound.dismiss()

    def click_counter(self, obj):
        global counter
        if counter < 100:
            counter += 1
            self.label._set_text(str(counter))
        else:
            self.label._set_text("Secret1: App by Mathi")

    def swap(self, obj):
        global proof, selection
        if proof == False:
            self.icon_button_switch.icon = "spotify"
            self.icon_button_switch.theme_text_color = "Custom"
            self.icon_button_switch.text_color = (0/255.0, 255/255.0, 0/255.0, 1)
            selection = 2
            proof = True
        else:
            self.icon_button_switch.icon = "youtube"
            self.icon_button_switch.theme_text_color = "Custom"
            self.icon_button_switch.text_color = (255/255.0, 0/255.0, 0/255.0, 1)
            selection = 1
            proof = False

    def download_x_check_input(self, obj):
        close_button_iL = MDRectangleFlatIconButton(icon="close", text="CLOSE", theme_text_color="Custom",
                                            text_color = (0/255.0, 140/255.0, 255/255.0, 1), on_release=self.close_dialog_iL)
        close_button_nF = MDRectangleFlatIconButton(icon="close", text="CLOSE", theme_text_color="Custom",
                                            text_color = (0/255.0, 140/255.0, 255/255.0, 1), on_release=self.close_dialog_nF)

        self.error_dialog_invalidLink = MDDialog(title="ERROR", text="Die von dir getätigte Eingabe ist kein Link!",
                                            buttons=[close_button_iL])
        self.error_dialog_notFound = MDDialog(title="ERROR", text="Der von dir eingegebene Link, beinhaltet einen Fehler oder konnte nicht gefunden werden!",
                                            buttons=[close_button_nF])

        user_input = self.link.text.strip()
        if proof == False:
            if user_input[0:16] == "https://youtu.be" or user_input[0:23] == "https://www.youtube.com": # or https://open.spotify.com/track/0VzBKgimNRMauaqzT2rEnS?si=cfba0d7fc99a4480
                try:
                    video_info = youtube_dl.YoutubeDL().extract_info(                                   # if selection ==1
                        url=user_input, download=False
                    )
                    filename = f"{video_info['title']}.mp3"
                    options = {
                        'format': 'bestaudio/best',
                        'keepvideo': False,
                        'outtmpl': '../'+filename,
                    }

                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([video_info['webpage_url']])
                except:
                    self.error_dialog_notFound.open()
            else:
                self.error_dialog_invalidLink.open()
        else:
            None


if __name__ == "__main__":
    App().run()

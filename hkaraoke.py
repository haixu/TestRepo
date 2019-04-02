from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('mainframe.kv')
Builder.load_file('menubar.kv')
Builder.load_file('toolbar.kv')
Builder.load_file('listing.kv')
Builder.load_file('queuelist.kv')


class MainFrame(AnchorLayout):
    pass


class HKaraokeApp(App):
    def build(self):
        return MainFrame()


if __name__ == "__main__":
    HKaraokeApp().run()

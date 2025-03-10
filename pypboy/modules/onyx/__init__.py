from pypboy import BaseModule
from pypboy.modules.onyx import goodboy
import settings

class Module(BaseModule):

    def __init__(self, *args, **kwargs):
        self.submodules = [
            goodboy.Module(self)
        ]
        super(Module, self).__init__(*args, **kwargs)
        
    def handle_resume(self):
        settings.hide_top_menu = False
        settings.hide_submenu = False
        settings.hide_main_menu = False
        settings.hide_footer = False
        self.active.handle_action("resume")

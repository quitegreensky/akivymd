from kivy.utils import platform
from kivy.utils import get_hex_from_color

def change_statusbar_color(statuscolor):

    if platform!='android':
        return

    from android.runnable import run_on_ui_thread
    from jnius import autoclass

    Color = autoclass("android.graphics.Color")
    WindowManager = autoclass('android.view.WindowManager$LayoutParams')
    activity = autoclass('org.kivy.android.PythonActivity').mActivity

    def statusbar(color):
        color= get_hex_from_color(color)[:7]
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color)) 
        window.setNavigationBarColor(Color.parseColor(color))
    
    status= run_on_ui_thread(statusbar)
    
    return status(statuscolor)
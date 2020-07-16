from kivy.utils import platform
from kivy.utils import get_hex_from_color

def change_statusbar_color(statuscolor, icons_color='Light'):

    if platform!='android':
        return

    from android.runnable import run_on_ui_thread
    from jnius import autoclass

    Color = autoclass("android.graphics.Color")
    WindowManager = autoclass('android.view.WindowManager$LayoutParams')
    activity = autoclass('org.kivy.android.PythonActivity').mActivity
    View= autoclass('android.view.View')
    # ContexCompat= autoclass('androidx.core.content.ContextCompat ')

    def statusbar():
        color= get_hex_from_color(statuscolor)[:7]
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color)) 
        window.setNavigationBarColor(Color.parseColor(color))

        if icons_color=='Dark':
            window.getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR)
        elif icons_color=='Light':
            window.getDecorView().setSystemUiVisibility(0)

    status= run_on_ui_thread(statusbar)
    
    return status()
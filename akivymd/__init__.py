from kivy.logger import Logger

__version__ = 1.1
__description__ = 'A set of fancy widgets for KivyMD'
__author__= "Sina Namadian"
__email__="quitegreensky@gmail.com"
Logger.info(f"AKivymd: v{__version__}")

import akivymd.factory_registers
from akivymd.tools.pyinstaller_hooks import hooks_path
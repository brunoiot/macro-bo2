from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["keyboard", "pynput"], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('macro-bo2.py', base=base)
]

setup(name='macro-bo2',
      version = '1',
      description = 'macro for bo2',
      options = {'build_exe': build_options},
      executables = executables)

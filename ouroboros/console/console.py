from ..common import *

if sys.platform == 'win32':
    getch = ctypes.CFUNCTYPE(ctypes.c_int32)(('_getch', windll.msvcrt))
else:
    def getch():
        import tty
        import termios

        sys.stdin.flush()
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def pause(text = None):
    if text is not None:
        print(text)
    getch()

def setTitle(text):
    if sys.platform == 'win32':
        windll.kernel32.SetConsoleTitleW(str(text))
    else:
        sys.stdout.write(f'\033]0;{text}\007')

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

if isinstance(sys.stdout, io.TextIOWrapper):
    def _flushstdout():
        _write = sys.stdout.write

        def _flush_write(*args, **kwargs):
            _write(*args, **kwargs)
            sys.stdout.flush()

        sys.stdout.write = _flush_write

    _flushstdout()
    del _flushstdout

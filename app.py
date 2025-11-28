import curses, time, os
from config import load_config
from widgets import load_widgets, registry

def run_dashboard(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    cfg = load_config()
    load_widgets()
    widgets=[]
    for w in cfg["widgets"]:
        cls = registry[w["type"]]
        widgets.append(cls(**w))
    theme = cfg.get("theme","default")
    while True:
        stdscr.erase()
        header = f"Nexus Terminal - Theme: {theme}  (Press Q to quit)"
        stdscr.addstr(0,2, header)
        for w in widgets:
            try:
                stdscr.addstr(w.y, w.x, w.render())
            except Exception as e:
                stdscr.addstr(1,1, f"Widget error: {e}")
        stdscr.refresh()
        time.sleep(0.2)
        if stdscr.getch()==ord('q'):
            break

def main():
    curses.wrapper(run_dashboard)

if __name__=='__main__':
    main()

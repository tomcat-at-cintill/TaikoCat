import webview, sys
if len(sys.argv) == 1:
    webview.create_window('TaikoCat Client', 'https://tg.lv5.ac', fullscreen=True)
else:
    webview.create_window(f'TaikoCat Client (running custom server @ {sys.argv[1]})', sys.argv[1],fullscreen=True)
webview.start()
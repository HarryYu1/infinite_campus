import app
import webview

#app.create_app().run(debug =True)

app_instance = app.create_app()
window = webview.create_window('Infinite Campus App', app_instance, fullscreen=False, resizable=True)
webview.start(debug=False)
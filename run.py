import app
import webview

#app.create_app().run(debug =True)

app_instance = app.create_app()
window = webview.create_window('My first pywebview application', app_instance, fullscreen=False, resizable=True)
webview.start(debug=True)
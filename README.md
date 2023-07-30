# Infinite Campus Project
The Infinite Campus project will be programmed and maintained by the NCHS CS Club to automate the SOAR selection process

## Contacts & Info 🌐
[CS Club Website](https://nchscsclub.com/) or visit us in room 46 on Tuesday mornings

# Getting Started
### Some Python packages must be installed in order to run this program.
<br>If you haven't already, install Visual Studio Code and Github Desktop online. You will also need to install python.</br>
<br> pip (Debian Linux): ```sudo apt install python3-pip```; Root Required.</br>
<br>Flask: ```pip install flask``` </br>
<br>Webview: ```pip install pywebview``` </br>
<br>Pandas: ```pip install pandas``` </br>
<br>Matplotlib: ```pip install matplotlib``` </br>
<br>Sql Alchemy: ```pip install sqlalchemy``` </br>

### Potential errors when running the program:
<br> **Error: ```You must have either QT or GTK with Python extensions installed in order to use pywebview.```** </br>
<br> ---> Run the command (Windows 10/11): ```pip install cefpython3``` </br>
<br> ---> Run the command (Debian Linux): ```sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0```; Root required. </br>

<br> **Error: ```No module name 'qtpy'```** </br>
<br> ---> Run the command (All Operating Systems): ```pip install qtpy```

<br> **Error: ```Cannot import name 'QtWebWidgets' from 'PyQt5'```** </br>
<br> ---> Run the command (Debian Linux, Newer): ```sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine python3-pyqt5.qtwebchannel libqt5webkit5-dev```; Root required.</br>
<br> ---> Run the command if the previous one doesn't work (Debian Linux): ```sudo apt install python3-pyqt5 python3-pyqt5.qtwebkit python-pyqt5 python-pyqt5.qtwebkit libqt5webkit5-dev```; Root required. </br>
## Instructions for installation
* `sudo apt install python3-pyqt5.qtwebengine`
* `pip install pyqtwebengine`
* `mkdir /usr/local/share/dlbt_os/bza`
* `mkdir /usr/local/share/dlbt_os/bza/bizon_app`
* `git clone https://github.com/technopremium/bizon_app.git /usr/local/share/dlbt_os/bza`
* `git -C /usr/local/share/dlbt_os/bza/bizon_app checkout release`
* `sudo nano /usr/share/applications/bizon_start_app.desktop`
* Copy:
```
[Desktop Entry]
Name=Bizon Guide App
Type=Application
Exec=python3 /usr/local/share/dlbt_os/bza/bizon_app/main.py
Terminal=false
Icon=/usr/local/share/dlbt_os/bza/bizon_app/ico.png
Comment=The support app from bizon-tech.com
NoDisplay=false
Categories=DeepLearning;Support
Name[en]=Bizon Guide
```

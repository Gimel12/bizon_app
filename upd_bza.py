import os


print("updating the app..")
r = os.popen("git -C /usr/local/share/dlbt_os/bza/bizon_app/ pull https://ruben865474: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@github.com/ruben865474/bizon_app.git release").read()
print(r)
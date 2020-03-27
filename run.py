import subprocess



class UbuntuCustomizer(object):
    def __init__(self):
        #self.update_system()
        #self.update_system()
        self.install_git()

    def update_system(self):
        subprocess.run(["apt-get", "update"])

    def upgrade_system(self):
        subprocess.run(["apt-get", "upgrade"])

    def install_git(self):
        #subprocess.run(["apt-get", "install", "git"])
        #subprocess.run(["apt-get", "install", "keepassx"])
        subprocess.run("wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ", shell=True)
        subprocess.run("sudo sh -c 'echo \"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google.list'", shell=True)
        self.update_system()
        subprocess.run(["apt-get", "install", "google-chrome-stable"])


UbuntuCustomizer()

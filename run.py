import subprocess



class UbuntuCustomizer(object):

    def install(self):
        #self.update_system()
        #self.update_system()
        #self.install_from_ubuntu_software()
        self.install_from_pip3()
        # self.install_chrome()
        # self.install_vscode()
        
    def install_from_pip3(self):
        self.pip3_install("virtualenv")
        self.pip3_install("virtualenvwrapper")

    def execute_command(self, command):
        subprocess.run(command, shell=True)

    def update_system(self):
        subprocess.run(["apt-get", "update"])

    def upgrade_system(self):
        subprocess.run(["apt-get", "upgrade"])

    def apt_install(self, package_name):
        subprocess.run(["apt-get", "install", package_name, "-y"])

    def pip3_install(self, package_name):
        subprocess.run(["pip3", "install", package_name])

    def install_chrome(self):
        execute_command("wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ")
        execute_command("sudo sh -c 'echo \"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google.list'")
        self.update_system()
        apt_install("google-chrome-stable")

    def install_vscode(self):
        execute_command("curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
        execute_command("sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft-archive-keyring.gpg")
        execute_command("sudo sh -c 'echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list'")
        apt_install("apt-transport-https")
        self.update_system()
        apt_install("code")

    def install_from_ubuntu_software(self):
        # self.apt_install("curl")
        # self.apt_install("git")
        # self.apt_install("keepassx")
        # self.apt_install("telegram-desktop")
        self.apt_install("python3-pip")

if __name__ == "__main__":
	UbuntuCustomizer().install()

#subprocess.run("", shell=True)

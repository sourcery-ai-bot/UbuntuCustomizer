import os
import subprocess


class UbuntuCustomizer(object):
    """A script to  automatically configure Ubuntu.
    """

    def __init__(self):
        self.home_dir = "/".join(os.path.realpath(__file__).split('/')[:3])
        self.bashrc_path = f'{self.home_dir}/.bashrc'

    def customize(self):
        self.update_system()
        self.upgrade_system()
        self.install_from_ubuntu_software()
        self.install_from_pip3()
        self.install_chrome()
        self.install_vscode()
        self.install_nodejs()
        self.install_yarn()
        self.install_quasar()
        self.install_unetbootin()
        self.set_other_settings()

    def set_other_settings(self):
        self.execute_command(
            "git config --global user.email \"6pirule@gmail.com\"")
        self.execute_command("pip3 install pep8")

    def install_unetbootin(self):
        self.execute_command("sudo add-apt-repository ppa:gezakovacs/ppa")
        self.update_system()
        self.apt_install("unetbootin")

    def install_yarn(self):
        self.execute_command(
            "curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -")
        self.execute_command(
            "echo \"deb https://dl.yarnpkg.com/debian/ stable main\" | sudo tee /etc/apt/sources.list.d/yarn.list")
        self.update_system()
        self.apt_install("yarn")

    def install_quasar(self):
        self.execute_command("npm install -g @quasar/cli")

    def install_nodejs(self):
        self.execute_command(
            "curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -")
        self.apt_install("nodejs")

    def install_from_pip3(self):
        self.install_virtualenvwrapper()

    def install_virtualenvwrapper(self):
        self.pip3_install("virtualenv")
        self.pip3_install("virtualenvwrapper")
        self.execute_command(
            "echo \"export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3\" >> " + self.bashrc_path)
        self.execute_command(
            "echo \"source /usr/local/bin/virtualenvwrapper.sh\" >> " + self.bashrc_path)

    def execute_command(self, command):
        subprocess.run(command, shell=True)

    def update_system(self):
        subprocess.run(["apt-get", "update"])

    def upgrade_system(self):
        subprocess.run(["apt-get", "upgrade", "-y"])

    def apt_install(self, package_name):
        subprocess.run(["apt-get", "install", package_name, "-y"])

    def pip3_install(self, package_name):
        subprocess.run(["pip3", "install", package_name])

    def install_chrome(self):
        self.execute_command(
            "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ")
        self.execute_command(
            "sudo sh -c 'echo \"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google.list'")
        self.update_system()
        self.apt_install("google-chrome-stable")

    def install_vscode(self):
        self.execute_command(
            "curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
        self.execute_command(
            "sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft-archive-keyring.gpg")
        self.execute_command(
            "sudo sh -c 'echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list'")
        self.apt_install("apt-transport-https")
        self.update_system()
        self.apt_install("code")

    def install_from_ubuntu_software(self):
        self.apt_install("curl")
        self.apt_install("git")
        self.apt_install("keepassx")
        self.apt_install("telegram-desktop")
        self.apt_install("python3-pip")
        self.apt_install("npm")
        self.apt_install("gnome-shell-pomodoro")
        self.apt_install("libreoffice")
        self.apt_install("python-pip")


if __name__ == "__main__":
    UbuntuCustomizer().customize()

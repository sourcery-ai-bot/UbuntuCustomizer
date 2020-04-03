"""Ubuntu Customizer.

This module demonstrates how to automatically configure Ubuntu via Python script.
Usage:
    $ sudo python start.py
"""

import os
import subprocess


class UbuntuCustomizer(object):
    """A class to automatically configure Ubuntu.

    It needs sudo-mode for configure correctly.
    """

    def __init__(self):
        """Detect home directory and system files."""
        self.home_dir = "/".join(os.path.realpath(__file__).split('/')[:3])
        self.bashrc_path = f'{self.home_dir}/.bashrc'

    def customize(self):
        """Main method, which do all work."""
        self.update_apt()
        self.upgrade_system()
        self.install_from_ubuntu_software()
        self.install_from_pip3()
        self.install_chrome()
        self.install_vscode()
        self.install_nodejs()
        self.install_yarn()
        self.install_quasar()
        self.install_unetbootin()
        self.install_omnidb()
        self.install_pgAdmin()
        self.set_git_settings()

    def install_pgAdmin(self):
        self.apt_install("postgresql-common")
        self.execute_command(
            "sudo sh /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh")

    def install_omnidb(self):
        self.execute_command(
            "echo \"deb https://dl.bintray.com/wind39/omnidb-deb debian main\" > /etc/apt/sources.list.d/omnidb.list")
        self.execute_command("apt-key adv --recv-keys 379CE192D401AB61")
        self.update_apt()
        self.apt_install("omnidb-app")

    def set_git_settings(self):
        """Configure git."""
        self.execute_command(
            "git config --global user.email \"6pirule@gmail.com\"")

    def install_python_helpers(self):
        """Add helpers for python."""
        self.pip3_install("pep8")
        self.install_virtualenvwrapper()

    def install_unetbootin(self):
        """Install unetbootin for creating disk images."""
        self.execute_command("sudo add-apt-repository ppa:gezakovacs/ppa")
        self.update_apt()
        self.apt_install("unetbootin")

    def install_yarn(self):
        """Install yarn."""
        self.execute_command(
            "curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -")
        self.execute_command(
            "echo \"deb https://dl.yarnpkg.com/debian/ stable main\" | sudo tee /etc/apt/sources.list.d/yarn.list")
        self.update_apt()
        self.apt_install("yarn")

    def install_quasar(self):
        """Install Quasar Framework."""
        self.execute_command("npm install -g @quasar/cli")

    def install_nodejs(self):
        """Install NodeJS."""
        self.execute_command(
            "curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -")
        self.apt_install("nodejs")

    def install_virtualenvwrapper(self):
        """Install virtualenvwrapper."""
        self.pip3_install("virtualenv")
        self.pip3_install("virtualenvwrapper")
        self.execute_command(
            "echo \"export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3\" >> " + self.bashrc_path)
        self.execute_command(
            "echo \"source /usr/local/bin/virtualenvwrapper.sh\" >> " + self.bashrc_path)

    def execute_command(self, command):
        """Execute shell command."""
        subprocess.run(command, shell=True)

    def update_apt(self):
        """Update Ubuntu."""
        subprocess.run(["apt-get", "update"])

    def upgrade_system(self):
        """Upgrade Ubuntu."""
        subprocess.run(["apt-get", "upgrade", "-y"])

    def apt_install(self, package_name):
        """Install from apt."""
        subprocess.run(["apt-get", "install", package_name, "-y"])

    def pip3_install(self, package_name):
        """Install from pip3."""
        subprocess.run(["pip3", "install", package_name])

    def install_chrome(self):
        """Install Google Chrome."""
        self.execute_command(
            "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - ")
        self.execute_command(
            "sudo sh -c 'echo \"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google.list'")
        self.update_apt()
        self.apt_install("google-chrome-stable")

    def install_vscode(self):
        """Install VS code text editor."""
        self.execute_command(
            "curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
        self.execute_command(
            "sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft-archive-keyring.gpg")
        self.execute_command(
            "sudo sh -c 'echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list'")
        self.update_apt()
        self.apt_install("code")

    def install_from_ubuntu_software(self):
        """Install apps from apt."""
        for app_name in ["apt-transport-https", "dirmngr", "ca-certificates", "curl", "git", "gnupg", "keepassx", "telegram-desktop", "simplescreenrecorder", "python3-pip", "npm", "gnome-shell-pomodoro", "libreoffice", "python-pip"]:
            self.apt_install(app_name)


if __name__ == "__main__":
    UbuntuCustomizer().customize()

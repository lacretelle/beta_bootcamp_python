#!bin/bash

version=`python3 --version`
if [ "$1" = "install-python" ]; then
	if [ "$version" = "Python 3.7.4" ]; then
		echo -n "Python is already installed, do you want to reinstall it ? Y/N"
		read yesno
		if [ "$yesno" = "y" ] || [ "yesno" = "Y" ]; then
			brew uninstall --ignore-dependencies python3
			echo "python has been removed."
			brew install python3
			echo "python is installed."
		elif [ "$yesno" = "n" ] || [ "$yesno" = "N" ]; then
			echo "exit."
			exit
		else
			echo "Choose yes or no !"
		fi
	else
		brew install python3
		echo "python is installed."
		exit
	fi
fi

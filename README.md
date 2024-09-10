# Aliasing python

echo "alias python=/usr/bin/python3" >> ~/.zshrc
source ~/.zshrc

# Virtualenv is a tool used to create isolated Python environments.

# It creates a folder which contains all the necessary executables

# to use the packages that a Python project would need.

# -m option : module-name

# Create and Use Virtual Environments

# venv (for Python 3) allows you to manage separate package installations

# for different projects. It creates a “virtual” isolated Python installation.

# When you switch projects, you can create a new virtual environment which

# is isolated from other virtual environments.

python3 -m venv venv

# Before you can start using the environment you need to activate it:

source venv/bin/activate

# get latest packages : pip (also known by Python 3's alias pip3) is a

# package-management system written in Python and is used to install

# and manage software packages.

pip install --upgrade pip

# optional aliasing

echo alias python='./venv/bin/python3' >> venv/bin/activate

pip install tqdm

# optional aliasing

echo alias tqdm='./venv/bin/tqdm' >> venv/bin/activate

# If you are done working with the virtual environment you can

# deactivate it with:

deactivate
source venv/bin/activate

pip install flake8
alias norminette=flake8

rm -rf ft_package/**pycache**
rm -rf ft_package.egg-info
rm -rf build
rm -rf dist
rm -rf venv

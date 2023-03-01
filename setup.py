from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in flutterwave_integration/__init__.py
from flutterwave_integration import __version__ as version

setup(
	name="flutterwave_integration",
	version=version,
	description="Frappe app to handle flutterwave payments",
	author="Chipo Hameja",
	author_email="chipohameja@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

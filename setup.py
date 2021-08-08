from setuptools import setup, find_packages

#Distribute py wheels
#python3 setup.py bdist_wheel sdist
#twine check dist/*
#cd dist 
#twine upload *

with open("README.md", "r") as fh:
    long_description = fh.read()



setup(
	name="htmgem",
	version="0.0.2",
	description="Generate HTML with Python!",
	url="https://github.com/ClimenteA/htmgem",
	author="Alin Climente",
	author_email="climente.alin@gmail.com",
	license='MIT',
	python_requires='>3.5',
	long_description=long_description,
    long_description_content_type="text/markdown",
	packages=find_packages()
)


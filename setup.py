import setuptools

'''
This file sets up the whole package with some detail.
Using this setup file and requirements.txt including -e . at the ened, you can install required packages
in a editable mode.
'''
Aouthor= "Mohammad Amirifard"
Email = "Mohammad.amirifard@mail.polimi.it"
Src_repo = "Kideney_classifier" # When we set this to name of folder in src, we can add logger in __ini__ file in src folder
Vesrion = '0.0.1'

setuptools.setup(
    name=Src_repo,
    version=Vesrion,
    author= Aouthor,
    packages=setuptools.find_packages(where="src")
)
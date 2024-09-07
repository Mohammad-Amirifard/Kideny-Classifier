import setuptools

Aouthor= "Mohammad Amirifard"
Email = "Mohammad.amirifard@mail.polimi.it"
Project_name = "Kideney_Disease Classification"
Vesrion = '0.0.1'

setuptools.setup(
    name=Project_name,
    version=Vesrion,
    author= Aouthor,
    packages=setuptools.find_packages(where="src")
)
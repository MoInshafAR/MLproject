from setuptools import find_packages, setup
from typing import List
# This is the setup script for packaging the MLproject.

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> list[str]:                           
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []                       # Initialize an empty list to store requirements
    with open(file_path) as file_obj:       # Open the requirements file
        requirements = file_obj.readlines() # Read all lines from the file
    
        requirements = [req.replace("\n", "") for req in requirements ]    # Remove newline characters from each requirement
    if HYPEN_E_DOT in requirements:          # If the editable install marker is present
        requirements.remove(HYPEN_E_DOT)     # Remove it from the list of requirements  
    return requirements


# This setup script is used to package the MLproject for distribution.
setup(
    name="MLproject",
    version="0.1",
    author="Inshaf",
    author_email="mohamedinshaf096@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt"),
)

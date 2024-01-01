from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        HYPHEN_E_DOT = "-e ."
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
    
setup(
    name = "UNSWNB15_binray_classification",
    version = '0.0.1',
    author = "Soumit Das",
    author_email = "1803063soumit@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)

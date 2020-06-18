
from setuptools import setup, find_packages
import akivymd
requirements_path='requirements.txt'

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements(requirements_path)
setup(
    name='akivymd',
    version=str(akivymd.__version__),
    description=akivymd.__description__,
    author=akivymd.__author__,
    author_email=akivymd.__email__,
    license='MIT',
    install_requires=parse_requirements(requirements_path) ,
    packages=find_packages(),
      )
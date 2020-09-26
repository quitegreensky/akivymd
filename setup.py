
from setuptools import setup, find_packages
import os

requirements_path = 'requirements.txt'
with open("README.md", "r") as fh:
    long_description = fh.read()


def get_package_info():

    init_path = os.path.join(
        os.path.dirname(__file__),
        'akivymd',
        '__init__.py')
    info_dic = {
        '__version__': '',
        '__description__': '',
        '__author__': '',
        '__email__': ''
    }

    with open(init_path, 'rt') as info:
        for line in info:
            for info in info_dic.keys():
                if line.startswith(info):
                    info_dic[info] = line.split('=')[1]
                    continue
    return info_dic


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements(requirements_path)
package_info = get_package_info()
setup(
    name='akivymd',
    version=package_info['__version__'],
    description=package_info['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quitegreensky/akivymd",
    author=package_info['__author__'],
    author_email=package_info['__email__'],
    license='MIT',
    install_requires=parse_requirements(requirements_path),
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

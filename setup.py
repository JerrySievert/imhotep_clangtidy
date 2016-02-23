import sys
from setuptools import setup, find_packages

setup(
    name='imhotep_clangtidy',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/jerrysievert/imhotep_clangtidy',
    license='MIT',
    install_requires=['imhotep>=0.4.0'],
    tests_require=['mock', 'pytest'],
    author='Jerry Sievert',
    author_email='code@legitimatesounding.com',
    description='An imhotep plugin for clang-tidy',
    entry_points={
        'imhotep_linters': [
            '.cpp = imhotep_clangtidy.plugin:ClangTidy',
            '.c = imhotep_clangtidy.plugin:ClangTidy',
            '.cc = imhotep_clangtidy.plugin:ClangTidy'
        ],
    },
)

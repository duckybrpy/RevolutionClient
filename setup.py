from setuptools import setup, find_packages

setup(
    name='RevolutionClient',
    version='0.0.1a0',
    packages=find_packages(include=['RevolutionClient', 'RevolutionClient.utils.*']),
    install_requires=[
        'python-socketio==5.11.4',
        'requests==2.32.3'
    ],
    description='Esta em testes',
    author='DuckyBR',
    author_email='',
    url='https://github.com/duckybrpy/revolutionclient',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

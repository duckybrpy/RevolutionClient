from setuptools import setup, find_packages

setup(
    name='RevolutionClient',
    version='0.0.1a0',
    packages=find_packages(include=['RevolutionClient', 'RevolutionClient.*']),
    install_requires=[
        'python-socketio==5.11.4',
        'requests==2.32.3'
    ],
    description='Esta em testes',
    author='DuckyBR',
    author_email='',
    url='https://github.com/duckybrpy/revolutionclient',  
    link="https://github.com/duckybrpy/RevolutionClient/releases/download/Teste/RevolutionClient.zip"
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

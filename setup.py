from setuptools import setup, find_packages

setup(
    name="turing-machines-simulator",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'PyQt6>=6.6.1',
    ],
    author="Esteban de Jesús Santiago Torres",
    description="Simulador de Máquinas de Turing",
    python_requires='>=3.8',
)
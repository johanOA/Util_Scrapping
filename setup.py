from setuptools import setup, find_packages

setup(
    name="util_scrapping",
    version="0.1.0",
    author="Johan Ospina",
    author_email="johan.ospina@celuweb.com",
    description="Libreria util a la hora de hacer scrapping.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/johanOA/Util_Scrapping",
    install_requires=[
        "requests>=2.25.1,<3.0.0", # Asegura compatibilidad con la versión 2.x 
        "numpy>=1.21.0",     
    ],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT"
)
from setuptools import setup, find_packages

HOME_URL = "https://github.com/iamaziz/st_ollama"

setup(
    name="stbook",
    version="0.1",
    author="Aziz Alto",
    author_email="iamaziz.alto@gmail.com",
    description="Streamlit Notebook - imagine Jupyter notebook inside Streamlit.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=HOME_URL,
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "streamlit_code_editor",
        "ollama", # optional
    ],
    package_data={'stbook': ['app.py']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "stbook=stbook.cli:run_app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
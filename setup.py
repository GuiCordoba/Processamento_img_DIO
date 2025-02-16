from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_test",
    version="0.0.1",
    author="Guilherme Cordoba",
    author_email="guimcordoba@hotmail.com",
    description="Teste de processamento de imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GuiCordoba/Processamento_img_DIO",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)

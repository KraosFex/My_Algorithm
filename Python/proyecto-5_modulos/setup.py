# Siempre que se cree un paquete que se desea subir a pipy se debe añadir este archivo

# Que contine? una estructura que siempre se debe seguir
from setuptools import setup, find_packages

# Se debe añadir un archivo .md
# lee el contenido de archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setup(
  name="<Nombre de modulo>",
  version="<version del modulo>",
  packages=find_packages(),
  install_requires=[],
  author="<Nombre del auto>",
  description="<Descripcion brebe de lo que hace el modulo>",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="<la url de tu sitio web>",
)

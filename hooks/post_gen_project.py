import os
import pathlib

os.chdir("..")
p = pathlib.Path("{{cookiecutter.file_name}}")
f = p.joinpath("{{cookiecutter.file_name}}.py")
f.rename("./{{cookiecutter.file_name}}.py")
p.rmdir()

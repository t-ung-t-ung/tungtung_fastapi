import os

# like Linux <-> Windows
compatibility = False

if compatibility:
    with open("env.yaml") as file:
        while file.readline() != "dependencies:\n":
            pass
        line = file.readline()
        while line != "  - pip:\n":
            line = line.lstrip(" -")
            os.system(f"conda install -y -c conda-forge {line}")
            line = file.readline()
        for line in file.readlines():
            line = line.lstrip(" -")
            os.system(f"pip install {line}")
else:
    os.system("conda env update -f env.yaml")

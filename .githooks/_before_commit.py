import os

with open("env.yaml", "a") as env:
    with open("temp.yaml") as file:
        k = False
        for line in file.readlines():
            if line.find("- pip:") != -1:
                k = True
            if k:
                env.write(line)
        os.remove("temp.yaml")


import os

with open("env.yaml", "a") as env:
    with open("temp.yaml") as file:
        k = False
        for line in file.readlines():
            if k:
                env.write(line)
            if line.find("- pip:") != -1:
                env.write(":")
                k = True
        os.remove("temp.yaml")


import os

with open("env.yaml", "a") as env:
    with open("temp.yaml") as file:
        k = False
        j = False
        for line in file.readlines():
            if line.find("- pip:") != -1:
                k = True
            if not k and line.find("- pip") != -1:
                j = True
            if k:
                if not j:
                    env.write("  - pip\n")
                    j = True
                env.write(line)
        os.remove("temp.yaml")


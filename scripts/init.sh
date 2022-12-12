git config core.hooksPath .githooks
chmod ug+x .githooks/*
conda update -n base -c defaults conda -y
conda env update -f env.yaml
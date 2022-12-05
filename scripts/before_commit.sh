conda env export --no-builds --from-history | grep -v "prefix" > env.yaml
conda env export --no-builds | grep -v "prefix" > temp.yaml
python3 scripts/_before_commit.py

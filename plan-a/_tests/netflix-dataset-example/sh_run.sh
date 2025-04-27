#!/bin/bash

# micromamba create -f env.yml -n neflix-dataset-test --yes
# micromamba update -f env.yml -n neflix-dataset-test --yes
# micromamba activate neflix-dataset-test

# python3 ./src/main.py

micromamba run -n neflix-dataset-test python ./src/main.py
# micromamba run -n neflix-dataset-test python -m mypy --install-types

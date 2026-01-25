#!/bin/bash

cmake -B ./build
cd ./build || exit 1
cmake --build . --parallel



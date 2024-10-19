#!/bin/bash

dot -Tpng ./graph.dot > ./graph.dot.png
dot -Tsvg ./graph.dot > ./graph.dot.svg
dot -Tpng ./graph2.dot > ./graph2.dot.png
dot -Tsvg ./graph2.dot > ./graph2.dot.svg


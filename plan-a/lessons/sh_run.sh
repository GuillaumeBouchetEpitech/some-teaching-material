#!/bin/bash

echo ""
echo "Build target?"
echo "=> create:   1"
echo "=> update:   2"
echo "=> activate: 3"

echo ""

read USER_INPUT_PLATFORM

case $USER_INPUT_PLATFORM in
1)
  echo ""
  echo "selected target: create"
  echo ""

  micromamba create -n planA-lessons -f env.yml
  ;;
2)
  echo ""
  echo "selected target: update"
  echo ""

  micromamba update -n planA-lessons -f env.yml
  ;;
3)
  echo ""
  echo "selected target: activate"
  echo ""

  micromamba activate planA-lessons
  ;;
*)
  echo ""
  echo "selected target: nothing O_o"
  echo ""
  ;;
esac

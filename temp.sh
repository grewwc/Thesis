#!/bin/bash


echo "input a string."
read first
echo "input another string."
read second
total="$first $second"
echo $total 
echo "the length of the total string is ${#total}"

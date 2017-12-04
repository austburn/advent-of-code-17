#!/bin/bash

VALID_PASSWORDS=0

while read line
do
    echo "Input: $line"
    num_phrases=$(echo $line | sed 's/\(\s\)/\n/g' | wc -l)
    if [[ $num_phrases -gt 1 ]]; then
        num_duplicates=$(echo $line | sed 's/\(\s\)/\n/g' | sort | uniq -d | wc -l)
        if [[ $num_duplicates -eq 0 ]]; then
            VALID_PASSWORDS=$((VALID_PASSWORDS+1));
            echo -e "\tValid password!"
        fi
    fi
done < $1
# on - cat $1 | while ... vs. done < $1
# https://stackoverflow.com/questions/20681210/bash-incrementing-variable-in-loop
# http://mywiki.wooledge.org/BashFAQ/024


echo "File contained $VALID_PASSWORDS valid passwords."

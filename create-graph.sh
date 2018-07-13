#!/bin/bash
#####################################################################
##  create-graph.sh
##
##  Raymond Wan
##    rwan.work@gmail.com
##
##  Copyright (C) 2018, Raymond Wan, All rights reserved.
#####################################################################

snakemake --snakefile Snakefile.py --dag -np | dot -Tsvg > graph.svg


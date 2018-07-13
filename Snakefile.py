#####################################################################
##  Snakefile.py
##
##  Raymond Wan
##    rwan.work@gmail.com
##
##  Copyright (C) 2018, Raymond Wan, All rights reserved.
#####################################################################

##  Configuration file
#configfile: "config.yaml"


##  Define constraints on wildcards
wildcard_constraints:
  dataset = "iris|abalone|adult|shuttle-landing-control"


##  Include additional functions and rules


##  Beginning of rules
rule all:
  input:
    "Output/Complete/iris.done",
    "Output/Complete/abalone.done"


rule Download_Data:
  output:  
    output_fn1 = "Output/Download/{dataset}.data"
  params:
    dataset = "{dataset}"
  shell:
    """
    wget https://archive.ics.uci.edu/ml/machine-learning-databases/{params.dataset}/{params.dataset}.data --output-document={output.output_fn1}
    """


rule Count_Lines:
  input:
    input_fn1 = "Output/Download/{dataset}.data"
  output:
    output_fn1 = "Output/Count/{dataset}.txt"
  shell:
    """
    wc -l {input.input_fn1} >{output.output_fn1}
    """


rule Randomize_Lines:
  input:
    input_fn1 = "Output/Download/{dataset}.data"
  output:
    output_fn1 = "Output/Random/{dataset}.txt"
  shell:
    """
    cat {input.input_fn1} | shuf >{output.output_fn1}
    """


rule Compute_MD5:
  input:
    input_fn1 = "Output/Random/{dataset}.txt"
  output:
    output_fn1 = "Output/MD5/{dataset}.txt"
  shell:
    """
    cat {input.input_fn1} | md5sum >{output.output_fn1}
    """


rule Compress_Randomize:
  input:
    input_fn1 = "Output/Random/{dataset}.txt"
  output:
    output_fn1 = "Output/Compress/{dataset}.gz"
  shell:
    """
    cat {input.input_fn1} | gzip -c >{output.output_fn1}
    """


rule Complete:
  input:
    input_fn1 = "Output/Count/{dataset}.txt",
    input_fn2 = "Output/MD5/{dataset}.txt",
    input_fn3 = "Output/Compress/{dataset}.gz"
  output:
    output_fn1 = "Output/Complete/{dataset}.done"
  shell:
    """
    touch {output.output_fn1}
    """


Snakemake Example
=================

Introduction
------------

Snakemake is a workflow definition language based on Python (that is not by me).  There is some excellent documentation [here](https://snakemake.readthedocs.io/en/stable/) already.

This repository is an example that I created to accompany a presentation I will gave on 14 July 2018 at the [Tokyo Linux User Group](https://tlug.jp/).  A video of this talk can be seen on [YouTube](https://www.youtube.com/watch?v=Vq_v_C6HE84).  These slides can be found in the slides/ subdirectory in PDF format.


Requirements
------------


|Software           |Version   |Required?  |Ubuntu package name   |
|:-----------------:|:--------:|:---------:|:--------------------:|
|Snakemake          | 4.3.1    | Yes       |snakemake             |
|wget               | 1.19.4   | Yes       |wget                  |
|Graphviz           | 2.40.1   | No        |graphviz              |
|GNU core utilities | 8.28     | Yes       |coreutils             | 
|gzip               | 1.6      | Yes       |gzip                  |

This example was run on an Ubuntu 18.04 system with additional software 
summarized in the above table.  As this example is not particularly 
complex, other Linux distributions will work, as well as older versions
of the above software.


Running the Example
-------------------

### About the Example

This example performs the following simple tasks (that arguably can be performed
without Snakemake):

1.  Download an example from the University of California of Irvine's Machine Learning Repository.
2.  Count the number of lines in the data file.
3.  Randomize the lines of the data file.
4.  Compress the permuted data file.
5.  Calculate the MD5 message digest of the permuted data file.

### Sample Commands

  * Run through the example:
    * `snakemake --snakefile Snakefile.py`

  * Generate the directed acyclic graph (as `graph.svg`) using Graphviz:
    * `./create-graph.sh`


Files and Directories
---------------------

After cloning and running through the example, the following directory structure should result:

    .
    ├── create-graph.sh   Bash script for creating a directed acyclic graph using Snakemake and dot
    ├── graph.svg         Output of create-graph.sh 
    ├── LICENSE           GNU GPL license v3
    ├── Output            Output directory created after running the example
    │   ├── Complete      Output from rule Complete
    │   ├── Compress      Output from rule Compress_Randomize
    │   ├── Count         Output from rule Count_Lines
    │   ├── Download      Output from rule Download_Data
    │   ├── MD5           Output from rule Compute_MD5
    │   └── Random        Output from rule Randomize_Lines
    ├── README.md         This file
    ├── Slides            Slides presented on July 14, 2018 at TLUG
    └── Snakefile.py      Main Snakefile (with a .py extension).


Notes
-----

Some notes about this example:
    * The filename of a Snakemake file should be `Snakefile`.  I have added a `.py`
      extension to enable syntax highlighting in my editor...


About this Snakemake Example
----------------------------

I can be reached at:  rwan.work@gmail.com 

My homepage is [here](http://www.rwanwork.info/).

The latest version of this example can be obtained from [GitHub](https://github.com/rwanwork/Snakemake-Example).

If you have any suggestions or general comments, feel free to write to the above address or submit an issue.


Copyright and License
---------------------

    Snakemake Example
    Copyright (C) 2018  Raymond Wan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
     
    Please see the file LICENSE for further information.


    Raymond Wan
    July 13, 2018


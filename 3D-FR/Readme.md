# The 3D version of FR algorithm
## Input
- in .txt file 
- format:
```bash
// node group
1--2
// where 1 & 2 are nodes & there is an edge joining 1 & 2 (without weight)

- example input and output can be found under input & output folder above
```
## Build
```bash
cd 3D-FR

cmake -H. -Bbuild

cmake --build build -- -j3
```
## Run
### Generate position of nodes
```bash
./build/bin/graph_visualisation -d {input folder}/{name}.txt  {output folder}/{name}.txt

output will be in .txt file
usage:

-h help 
-v version 
-i number of iterations, default = 100 
-w width, default = 10 
-l length, default = 10 
-n interval, default = 0 --> used only when you want to generate process 
```

### Plot 3D graph
```bash
python3 misc/PlotGraph3d.py {output folder}/{name}.txt {png output folder}/{name}.html

usage: 

-h help 
-v version 
-n interval --> used when generate process (must match params of command that generate position of nodes)
-i iterations --> used when generate process
```
Output will be .html file.
## Others
### Dependencies 

#### For c++ script

- gcc
- cmake

#### For python scripts

- networkx 
- matplotlib
- pandas
- scipy
- plotly (for 3d graphs)

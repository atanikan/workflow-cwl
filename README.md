# workflow-cwl

## About

Simulates a workflow where a docker script is instantiated running pw.x with pw.in file and wstat.x with wstat.in file sequentially using cwl in a unix O.S. Change inputs in the west.yml file and *.in files to simulate other results. You can visualize the workflow at https://view.commonwl.org/

## Prerequisistes

- Python3
- pip
- docker

## Installation

User needs to install cwlgen - A python script which generates cwl files. Follow https://github.com/common-workflow-language/python-cwlgen or run,

```bash
  pip install cwlgen
```

cwl tool to run cwl files and its workflows. Follow https://github.com/common-workflow-language/cwltool or run, 

```bash
 pip install cwltool
```

## Usage

To run pw.x code with pw.in file to generate pw.out file

```bash
python genpw.py
cwl-runner pw.cwl pw.yml
```

To run wstat.x code with wstat.in file to generate wstat.out file

```bash 
python genwstat.py
cwl-runner wstat.cwl wstat.yml
```


To run the entire workflow where first pw runs and then wstat runs

```bash
python genworkflow.py
cwl-runner workflow.cwl workflow.yml
```

## Visualize
To visualize the workflow, paste  at https://view.commonwl.org/








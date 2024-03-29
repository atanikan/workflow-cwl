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

```bash
python genwest.py
python genworkflow.py
cwl-runner west_workflow.cwl west.yml
```

## Visualize

To visualize the workflow, paste https://github.com/atanikan/workflow-cwl/blob/master/west_workflow.cwl at https://view.commonwl.org/








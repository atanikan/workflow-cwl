#!/usr/bin/env cwl-runner

$namespaces:
  s: http://schema.org/
baseCommand: mpirun
class: CommandLineTool
cwlVersion: v1.0
doc: Runs wstat.x code for different input paramaters
id: wstat_tool
inputs:
- default: wstat.in
  doc: Can be wstat.in or input file of your choice
  id: input_file
  inputBinding:
    position: 3
    prefix: -i
  type: File
- default: wstat.x
  doc: runs wstat.x
  id: script_type
  inputBinding:
    position: 2
  type: File
- default: 2
  doc: choose 2, 3, 4
  id: no_of_cores
  inputBinding:
    position: 1
    prefix: -np
  type: int
- default: wstat.out
  doc: produces wstat.out
  id: output
  inputBinding:
    position: 4
    prefix: -o
  type: File
label: calculates wstat.x with wstat.in input and wstat.out as output
outputs:
- doc: Output File generated with west wstat.x code
  id: wstat_output_file
  outputBinding:
    glob: '*.out'
  type: File
s:about: WSTAT code that runs WSTAT for an input wstat.in file to generate wstat.out
s:name: WSTAT

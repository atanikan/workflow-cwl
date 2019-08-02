#!/usr/bin/env cwl-runner

$namespaces:
  s: http://schema.org/
baseCommand: mpirun
class: CommandLineTool
cwlVersion: v1.0
doc: Runs pw.x code for different input paramaters
id: pw_tool
inputs:
- default: pw.in
  doc: Can be pw.in or input file of your choice
  id: input_file
  inputBinding:
    position: 3
    prefix: -i
  type: File
- default: pw.x
  doc: runs pw.x
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
- default: pw.out
  doc: produces pw.out
  id: output
  inputBinding:
    position: 4
    prefix: '>'
  type: File
label: calculates pw.x with pw.in input and pw.out as output
outputs:
- doc: Output File generated with west pw.x code
  id: pw_output_file
  outputBinding:
    glob: '*.out'
  type: File
s:about: PW code runs pw for an input pw.in file to generate pw.out
s:name: PW

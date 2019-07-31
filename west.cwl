#!/usr/bin/env cwl-runner

$namespaces:
  s: http://schema.org/
baseCommand: sh
class: CommandLineTool
cwlVersion: v1.0
doc: Runs west code for different input paramaters
id: west_tool
inputs:
- doc: West shell script which generates output based on inputs using docker
  id: script_file
  inputBinding:
    position: 1
  type: File
- doc: Input file for west code. Can be pw.in, wstat.in
  id: input_file
  inputBinding:
    position: 2
  type: File
- doc: Urls to download upf files used for pw, wstat scripts
  id: URLs
  inputBinding:
    position: 3
  type: string
- doc: choose pw or wstat
  id: script_type
  inputBinding:
    position: 4
  type: string
- doc: choose 2, 3, 4
  id: no_of_cores
  inputBinding:
    position: 5
  type: int
label: calculates pw.x, wstat.x and generates pw.out,wstat.out file
outputs:
- doc: Output File generated with west pw.x or wstat.x code
  id: west_output_file
  outputBinding:
    glob: '*.out'
  type: File
s:about: West code runs pw for an input pw.in file to generate pw.out, or wstat for
  wstat.in with wstat.out file
s:name: West

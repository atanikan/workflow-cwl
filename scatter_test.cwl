#!/usr/bin/env cwl-runner

class: Workflow
requirements:
  - class: ScatterFeatureRequirement
cwlVersion: v1.0
doc: Tool to generate west code
id: west_workflow_tool
inputs:
  URLs:
    doc: Urls to download upf files used for west scripts
    id: URLs
    inputBinding:
      position: 3
    type: string
  input_file_array:
    doc: Input file for west code. Can be pw.in, wstat.in, wfreq.in
    id: input_file_array
    inputBinding:
      position: 2
    type: File[]
  no_of_cores:
    doc: choose between pw, wstat, wfreq
    id: no_of_cores
    inputBinding:
      position: 5
    type: int
  script_file:
    doc: West script which generates pw.out, wstat.out based on inputs
    id: script_file
    inputBinding:
      position: 1
    type: File
  script_type_array:
    doc: choose between pw, wstat, wfreq
    id: script_type_array
    inputBinding:
      position: 4
    type: string[]
label: generates pw.out and wstat.out files
outputs:
  output_file:
    doc: Output File generated with west code
    type: File[]
    outputSource: west_tool/west_output_file
steps:
  west_tool:
    scatter: [script_type,input_file]
    scatterMethod: "dotproduct"
    in:
      script_file: script_file
      input_file: input_file_array
      URLs: URLs
      script_type: script_type_array
      no_of_cores: no_of_cores
    run: west.cwl
    out: [west_output_file]


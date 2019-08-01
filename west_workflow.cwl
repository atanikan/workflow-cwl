#!/usr/bin/env cwl-runner

class: Workflow
cwlVersion: v1.0
doc: Workflow tool to generate west code
id: west_workflow_tool
inputs:
  URLs:
    doc: Urls to download upf files used for west scripts
    id: URLs
    inputBinding:
      position: 3
    type: string
  input_file_array:
    doc: Input file for west code. Can be pw.in, wstat.in
    id: input_file_array
    inputBinding:
      position: 2
    type:
      items: File
      type: array
  no_of_cores:
    doc: No of cores to run on 2 ,3 ,4
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
    doc: choose between pw, wstat
    id: script_type_array
    inputBinding:
      position: 4
    type:
      items: string
      type: array
label: Workflow tool to generates pw.out and wstat.out files
outputs:
  output_file:
    id: output_file
    label: Output File generated with west code
    outputSource: west_tool/west_output_file
    type:
      items: File
      type: array
requirements:
  ScatterFeatureRequirement: {}
steps:
  west_tool:
    doc: runs west.cwl
    in:
      URLs:
        id: URLs
        source: URLs
      input_file:
        id: input_file
        source: input_file_array
      no_of_cores:
        id: no_of_cores
        source: no_of_cores
      script_file:
        id: script_file
        source: script_file
      script_type:
        id: script_type
        source: script_type_array
    out:
    - west_output_file
    run: west.cwl
    scatter:
    - script_type
    - input_file
    scatterMethod: dotproduct

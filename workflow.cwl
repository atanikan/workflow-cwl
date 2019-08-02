#!/usr/bin/env cwl-runner

class: Workflow
cwlVersion: v1.0
doc: Workflow tool to generate west code
id: west_workflow_tool
inputs:
  no_of_cores:
    default: 2
    doc: No of cores to run on 2 ,3 ,4
    id: no_of_cores
    type: int
  pw_input_file:
    default: pw.in
    doc: Input file for west code. Can be pw.in
    id: pw_input_file
    type: File
  pw_output:
    default: pw.out
    doc: passes pw.out
    id: pw_output
    type: File
  pw_script:
    default: pw.x
    doc: runs pw.x
    id: pw_script
    type: File
  wstat_input_file:
    default: wstat.in
    doc: Input file for west code. Can be wstat.in
    id: wstat_input_file
    type: File
  wstat_output:
    default: wstat.out
    doc: passes wstat.out
    id: wstat_output
    type: File
  wstat_script:
    default: wstat.x
    doc: runs wstat.x
    id: wstat_script
    type: File
label: Workflow tool to generates pw.out and wstat.out files
outputs:
  pw_output_file:
    id: pw_output_file
    label: Output File generated with pw code
    outputSource: pw_tool/pw_output_file
    type: File
  wstat_output_file:
    id: wstat_output_file
    label: Output File generated with wstat code
    outputSource: wstat_tool/wstat_output_file
    type: File
steps:
  pw_tool:
    doc: runs pw.cwl
    in:
      input_file:
        id: input_file
        source: pw_input_file
      no_of_cores:
        id: no_of_cores
        source: no_of_cores
      output:
        id: output
        source: pw_output
      script_type:
        id: script_type
        source: pw_script
    out:
    - pw_output_file
    run: pw.cwl
  wstat_tool:
    doc: runs wstat.cwl
    in:
      input_file:
        id: input_file
        source: wstat_input_file
      no_of_cores:
        id: no_of_cores
        source: no_of_cores
      output:
        id: output
        source: wstat_output
      script_type:
        id: script_type
        source: wstat_script
    out:
    - wstat_output_file
    run: wstat.cwl

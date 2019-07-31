#!/usr/bin/env cwl-runner

$namespaces:
  s: http://schema.org/
baseCommand: sh
class: CommandLineTool
cwlVersion: v1.0
doc: Runs west code specifically pw, wstat or wfreq
id: west_tool
inputs:
- doc: West script which generates pw.out, wstat.out based on inputs
  id: script_file
  inputBinding:
    position: 1
  type: File
- doc: Input file for west code. Can be pw.in, wstat.in, wfreq.in
  id: input_file
  inputBinding:
    position: 2
  type: File
- doc: Urls to download upf files used for west scripts
  id: URLs
  inputBinding:
    position: 3
  type: string
- doc: choose between pw, wstat, wfreq
  id: script_type
  inputBinding:
    position: 4
  type: string
- doc: choose between pw, wstat, wfreq
  id: no_of_cores
  inputBinding:
    position: 5
  type: int
label: generates pw.out and wstat.out files
outputs:
- doc: Output File generated with west code
  id: output
  outputBinding:
    glob: '*.out'
  type: File
s:about: West code runs pw , wstat for an input file.
s:name: West

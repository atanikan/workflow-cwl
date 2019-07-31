'''
Example of usage of the cwlgen library
'''

'''
simulating this,
sh fetchWest.sh http://www.quantum-simulation.org/potentials/sg15_oncv/upf/H_ONCV_PBE-1.0.upf,http://www.quantum-simulation.org/potentials/sg15_oncv/upf/Si_ONCV_PBE-1.1.upf pw 2
'''


###########  Import  ###########



import cwlgen

if __name__ == "__main__":

    # Create a tool
    # Write in an output file
    #cwl_tool.export()
    #cwl_tool.export("west.cwl")
    
    cwl_tool = cwlgen.workflow.Workflow(workflow_id='west_tool',
                                        label='generates pw.out and wstat.out files',
                                        doc='Tool to generate west code',
                                        cwl_version='v1.0')
    
    

    # Add  inputs (script_file, URLs, type, no_of_cores)
    script_binding = cwlgen.CommandLineBinding(position=1)
    script_file = cwlgen.workflow.InputParameter('script_file',
                                              param_type='File',
                                              input_binding=script_binding,
                                              doc='West script which generates pw.out, wstat.out based on inputs')
    cwl_tool.inputs.append(script_file)

    file_binding = cwlgen.CommandLineBinding(position=2)
    input_file = cwlgen.workflow.InputParameter('input_file',
                                              param_type='File',
                                              input_binding=file_binding,
                                              doc='Input file for west code. Can be pw.in, wstat.in, wfreq.in')
    cwl_tool.inputs.append(input_file)


    url_binding = cwlgen.CommandLineBinding(position=3)
    urls = cwlgen.workflow.InputParameter('URLs',
                                           param_type='string',
                                           input_binding=url_binding,
                                           doc='Urls to download upf files used for west scripts')
    cwl_tool.inputs.append(urls)

    script_type_binding = cwlgen.CommandLineBinding(position=4)
    type_script = cwlgen.workflow.InputParameter('script_type',
                                           param_type='string',
                                           input_binding=script_type_binding,
                                           doc='choose between pw, wstat, wfreq')
    cwl_tool.inputs.append(type_script)

    core_binding = cwlgen.CommandLineBinding(position=5)
    cores = cwlgen.workflow.InputParameter('no_of_cores',
                                           param_type='int',
                                           input_binding=core_binding,
                                           doc='choose between pw, wstat, wfreq')
    cwl_tool.inputs.append(cores)

    
    # Add 1 output
    output_bind = cwlgen.CommandOutputBinding(glob="*.out")
    output = cwlgen.CommandOutputParameter('output',
                                           param_type='File',
                                           output_binding=output_bind,
                                           doc='Output File generated with west code')
    cwl_tool.outputs.append(output)


    workflow_pw = cwlgen.workflow.WorkflowStep('pw_tool',
                                                'west.cwl')
    #workflow_pw_in = workflow_pw.WorkflowStepInput('script_file','script_file') 
    workflow_pw.inputs.append(script_file)
    #workflow_pw.outputs.append(output)	
    cwl_tool.steps.append(workflow_pw)
    #cwl_tool.outputs.append(output)
    cwl_tool.export("w.cwl")

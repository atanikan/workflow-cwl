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
    west_tool = cwlgen.CommandLineTool(tool_id='west_tool',
                                      label='calculates pw.x, wstat.x and generates pw.out,wstat.out file',
                                      base_command='sh')

    # Add  inputs (script_file, URLs, type, no_of_cores)
    script_binding = cwlgen.CommandLineBinding(position=1)
    script_file = cwlgen.CommandInputParameter('script_file',
                                              param_type='File',
                                              input_binding=script_binding,
                                              doc='West shell script which generates output based on inputs using docker')
    west_tool.inputs.append(script_file)
    
    file_binding = cwlgen.CommandLineBinding(position=2)
    input_file = cwlgen.CommandInputParameter('input_file',
                                              param_type='File',
                                              input_binding=file_binding,
                                              doc='Input file for west code. Can be pw.in, wstat.in')
    west_tool.inputs.append(input_file)
    

    url_binding = cwlgen.CommandLineBinding(position=3)
    urls = cwlgen.CommandInputParameter('URLs',
                                           param_type='string',
                                           input_binding=url_binding,
                                           doc='Urls to download upf files used for pw, wstat scripts')
    west_tool.inputs.append(urls)
    
    script_type_binding = cwlgen.CommandLineBinding(position=4)
    type_script = cwlgen.CommandInputParameter('script_type',
                                           param_type='string',
                                           input_binding=script_type_binding,
                                           doc='choose pw or wstat')
    west_tool.inputs.append(type_script)

    core_binding = cwlgen.CommandLineBinding(position=5)
    cores = cwlgen.CommandInputParameter('no_of_cores',
                                           param_type='int',
                                           input_binding=core_binding,
                                           doc='choose 2, 3, 4')
    west_tool.inputs.append(cores)
    
    # Add 1 output
    output_bind = cwlgen.CommandOutputBinding(glob="*.out")
    output = cwlgen.CommandOutputParameter('west_output_file',
                                           param_type='File',
                                           output_binding=output_bind,
                                           doc='Output File generated with west pw.x or wstat.x code')
    west_tool.outputs.append(output)

    # Add documentation
    west_tool.doc = "Runs west code for different input paramaters"

    # Add Metadata
    metadata = {'name': 'West',
                'about': 'West code runs pw for an input pw.in file to generate pw.out, or wstat for wstat.in with wstat.out file'}
    west_tool.metadata = cwlgen.Metadata(**metadata)
    west_tool.metadata = cwlgen.Metadata(**metadata)

    # Write in an output file
    west_tool.export("west.cwl")

'''
Example of usage of the cwlgen library for command line tool
'''

'''
simulating this,  mpirun --allow-run-as-root -np 2 wstat.x -i wstat.in > wstat.out
'''


###########  Import  ###########



import cwlgen

if __name__ == "__main__":

    # Initialize a command line tool
    west_tool = cwlgen.CommandLineTool(tool_id='wstat_tool',
                                      label='calculates wstat.x with wstat.in input and wstat.out as output',
                                      base_command='mpirun')

    # Add  inputs (script_file, type, no_of_cores)
    file_binding = cwlgen.CommandLineBinding(prefix='-i',position=3)
    input_file = cwlgen.CommandInputParameter('input_file',
                                              param_type='File',
                                              default='wstat.in',
                                              input_binding=file_binding,
                                              doc='Can be wstat.in or input file of your choice')
    west_tool.inputs.append(input_file)
    

    script_type_binding = cwlgen.CommandLineBinding(position=2)
    type_script = cwlgen.CommandInputParameter('script_type',
                                           param_type='File',
                                           default='wstat.x', 
                                           input_binding=script_type_binding,
                                           doc='runs wstat.x')
    west_tool.inputs.append(type_script)

    core_binding = cwlgen.CommandLineBinding(prefix='-np',position=1)
    cores = cwlgen.CommandInputParameter('no_of_cores',
                                           param_type='int',
                                           default=2,
                                           input_binding=core_binding,
                                           doc='choose 2, 3, 4')
    west_tool.inputs.append(cores)
    
    output_file_binding = cwlgen.CommandLineBinding(prefix='-o',position=4)
    output = cwlgen.CommandInputParameter('output',
                                           param_type='File',
                                           default='wstat.out',
                                           input_binding=output_file_binding,
                                           doc='produces wstat.out')
    west_tool.inputs.append(output)

    # Add 1 output with type to fetch
    output_bind = cwlgen.CommandOutputBinding(glob="*.out")
    output = cwlgen.CommandOutputParameter('wstat_output_file',
                                           param_type='File',
                                           output_binding=output_bind,
                                           doc='Output File generated with west wstat.x code')
    west_tool.outputs.append(output)

    

    # Add documentation
    west_tool.doc = "Runs wstat.x code for different input paramaters"

    # Add Metadata
    metadata = {'name': 'WSTAT',
                'about': 'WSTAT code that runs WSTAT for an input wstat.in file to generate wstat.out'}
    west_tool.metadata = cwlgen.Metadata(**metadata)
    west_tool.metadata = cwlgen.Metadata(**metadata)

    # Write in an output file
    west_tool.export("wstat.cwl")

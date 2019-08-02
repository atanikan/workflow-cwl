'''
Example of usage of the cwlgen library for command line tool
'''

'''
simulating this,  mpirun --allow-run-as-root -np 2 pw.x -i pw.in > pw.out
'''


###########  Import  ###########



import cwlgen

if __name__ == "__main__":

    # Initialize a command line tool
    west_tool = cwlgen.CommandLineTool(tool_id='pw_tool',
                                      label='calculates pw.x with pw.in input and pw.out as output',
                                      base_command='mpirun')

    # Add  inputs (script_file,script-pw.x, no_of_cores)
    file_binding = cwlgen.CommandLineBinding(prefix='-i',position=3)
    input_file = cwlgen.CommandInputParameter('input_file',
                                              param_type='File',
                                              default='pw.in',
                                              input_binding=file_binding,
                                              doc='Can be pw.in or input file of your choice')
    west_tool.inputs.append(input_file)
    

    script_type_binding = cwlgen.CommandLineBinding(position=2)
    type_script = cwlgen.CommandInputParameter('script_type',
                                           param_type='File',
                                           default='pw.x', 
                                           input_binding=script_type_binding,
                                           doc='runs pw.x')
    west_tool.inputs.append(type_script)

    core_binding = cwlgen.CommandLineBinding(prefix='-np',position=1)
    cores = cwlgen.CommandInputParameter('no_of_cores',
                                           param_type='int',
                                           default=2,
                                           input_binding=core_binding,
                                           doc='choose 2, 3, 4')
    west_tool.inputs.append(cores)
    
    output_file_binding = cwlgen.CommandLineBinding(prefix='>',position=4)
    output = cwlgen.CommandInputParameter('output',
                                           param_type='File',
                                           default='pw.out',
                                           input_binding=output_file_binding,
                                           doc='produces pw.out')
    west_tool.inputs.append(output)

    # This section is to verify if out file is generated. Can be made optional as output is already given in input paramters.
    output_bind = cwlgen.CommandOutputBinding(glob="*.out")
    output = cwlgen.CommandOutputParameter('pw_output_file',
                                           param_type='File',
                                           output_binding=output_bind,
                                           doc='Output File generated with west pw.x code')
    west_tool.outputs.append(output)

    

    # Add documentation
    west_tool.doc = "Runs pw.x code for different input paramaters"

    # Add Metadata
    metadata = {'name': 'PW',
                'about': 'PW code runs pw for an input pw.in file to generate pw.out'}
    west_tool.metadata = cwlgen.Metadata(**metadata)
    west_tool.metadata = cwlgen.Metadata(**metadata)

    # Write in an output file
    west_tool.export("pw.cwl")

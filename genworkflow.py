'''
Example of usage of the cwlgen workflow library
'''

'''
simulating this,
sh fetchWest.sh http://www.quantum-simulation.org/potentials/sg15_oncv/upf/H_ONCV_PBE-1.0.upf,http://www.quantum-simulation.org/potentials/sg15_oncv/upf/Si_ONCV_PBE-1.1.upf pw 2
'''


###########  Import  ###########
import cwlgen

if __name__ == "__main__":

    # Initialize workflow
    cwl_tool = cwlgen.workflow.Workflow(workflow_id='west_workflow_tool',
                                        label='Workflow tool to generates pw.out and wstat.out files',
                                        doc='Workflow tool to generate west code',
                                        cwl_version='v1.0')
    
   
    #Schema defining reuqirement for scatter feature
    scatter_class = cwlgen.ScatterFeatureRequirement()
    cwl_tool.requirements.append(scatter_class)
 
    # Add  inputs (script_file, URLs, type, no_of_cores to the workflow
    script_binding = cwlgen.CommandLineBinding(position=1)
    script_file = cwlgen.workflow.InputParameter('script_file',
                                              param_type='File',
                                              input_binding=script_binding,
                                              doc='West script which generates pw.out, wstat.out based on inputs')
    cwl_tool.inputs.append(script_file)

    file_binding = cwlgen.CommandLineBinding(position=2)
    input_file_array = cwlgen.workflow.InputParameter('input_file_array',
                                              param_type='File[]',
                                              input_binding=file_binding,
                                              doc='Input file for west code. Can be pw.in, wstat.in')
    cwl_tool.inputs.append(input_file_array)


    url_binding = cwlgen.CommandLineBinding(position=3)
    URLs = cwlgen.workflow.InputParameter('URLs',
                                           param_type='string',
                                           input_binding=url_binding,
                                           doc='Urls to download upf files used for west scripts')
    cwl_tool.inputs.append(URLs)

    script_type_binding = cwlgen.CommandLineBinding(position=4)
    script_type_array = cwlgen.workflow.InputParameter('script_type_array',
                                           param_type='string[]',
                                           input_binding=script_type_binding,
                                           doc='choose between pw, wstat')
    cwl_tool.inputs.append(script_type_array)

    core_binding = cwlgen.CommandLineBinding(position=5)
    no_of_cores = cwlgen.workflow.InputParameter('no_of_cores',
                                           param_type='int',
                                           input_binding=core_binding,
                                           doc='No of cores to run on 2 ,3 ,4')
    cwl_tool.inputs.append(no_of_cores)

    
    # Path to fetch outputs from
    output = cwlgen.workflow.WorkflowOutputParameter('output_file',
                                           param_type='File[]',
                                           output_source='west_tool/west_output_file',
                                           label='Output File generated with west code')
    cwl_tool.outputs.append(output)

    # Toggle between pw and wstat for pw.in and wstat.in
    workflow_west = cwlgen.workflow.WorkflowStep('west_tool',
                                               'west.cwl',
                                               doc='runs west.cwl',
                                               scatter=['script_type','input_file'],
                                               scatter_method='dotproduct')
    # Add workflow step inputs
    workflow_west_script_file = cwlgen.WorkflowStepInput('script_file','script_file')
    workflow_west_input_file = cwlgen.WorkflowStepInput('input_file','input_file_array')
    workflow_west_URLs = cwlgen.WorkflowStepInput('URLs','URLs')
    workflow_west_script_type = cwlgen.WorkflowStepInput('script_type','script_type_array')
    workflow_west_cores =  cwlgen.WorkflowStepInput('no_of_cores','no_of_cores')
    workflow_west.inputs.extend((workflow_west_script_file,workflow_west_input_file,workflow_west_URLs,workflow_west_script_type,workflow_west_cores))
    
    workflow_west_output = cwlgen.WorkflowStepOutput('west_output_file')
    workflow_west.out.append(workflow_west_output)
    #Add first step
    cwl_tool.steps.append(workflow_west)
    #Export cwl 
    cwl_tool.export("west_workflow.cwl")

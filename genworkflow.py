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
    
   
    # Add  all inputs to the entire workflow (i.e inputs needed for pw.cwl and wstat.cwl)
    pw_input_file = cwlgen.workflow.InputParameter('pw_input_file',
                                              param_type='File',
                                              default='pw.in',
                                              doc='Input file for west code. Can be pw.in')
    cwl_tool.inputs.append(pw_input_file)

    wstat_input_file = cwlgen.workflow.InputParameter('wstat_input_file',
                                              param_type='File',
                                              default='wstat.in',
                                              doc='Input file for west code. Can be wstat.in')
    cwl_tool.inputs.append(wstat_input_file)


    pw_script = cwlgen.workflow.InputParameter('pw_script',
                                           param_type='File',
                                           default='pw.x', 
                                           doc='runs pw.x')
    cwl_tool.inputs.append(pw_script)

    wstat_script = cwlgen.workflow.InputParameter('wstat_script',
                                           param_type='File',
                                           default='wstat.x',
                                           doc='runs wstat.x')
    cwl_tool.inputs.append(wstat_script)

    

    no_of_cores = cwlgen.workflow.InputParameter('no_of_cores',
                                           param_type='int',
                                           default=2,
                                           doc='No of cores to run on 2 ,3 ,4')
    cwl_tool.inputs.append(no_of_cores)

    pw_output_file = cwlgen.workflow.InputParameter('pw_output',
                                           param_type='File',
                                           default='pw.out',
                                           doc='passes pw.out')
    cwl_tool.inputs.append(pw_output_file)

    wstat_output_file = cwlgen.workflow.InputParameter('wstat_output',
                                           param_type='File',
                                           default='wstat.out',
                                           doc='passes wstat.out')
    cwl_tool.inputs.append(wstat_output_file)


    
    # This section defined path to fetch outputs from. The output id defined in pw.cwl and wstat.cwl. This is to verify if output is written. 
    #Can be made optional as ouput file is passed as an input paramter
    pw_output = cwlgen.workflow.WorkflowOutputParameter('pw_output_file',
                                           param_type='File',
                                           output_source='pw_tool/pw_output_file',
                                           label='Output File generated with pw code')
    cwl_tool.outputs.append(pw_output)


    wstat_output = cwlgen.workflow.WorkflowOutputParameter('wstat_output_file',
                                           param_type='File',
                                           output_source='wstat_tool/wstat_output_file',
                                           label='Output File generated with wstat code')

    cwl_tool.outputs.append(wstat_output)

    ##################### Add steps to workflow ############################### 
    # Workflow for for pw.x
    workflow_pw = cwlgen.workflow.WorkflowStep('pw_tool',
                                               'pw.cwl',
                                               doc='runs pw.cwl')
    
    # Pass workflow step inputs to pw.cwl as needed. The ids are defined in pw.cwl
    workflow_pw_input_file = cwlgen.WorkflowStepInput('input_file','pw_input_file')
    workflow_pw_script_type = cwlgen.WorkflowStepInput('script_type','pw_script')
    workflow_cores =  cwlgen.WorkflowStepInput('no_of_cores','no_of_cores') #can be reused in wstat
    workflow_pw_output_file = cwlgen.WorkflowStepInput('output','pw_output')
    workflow_pw.inputs.extend((workflow_pw_input_file,workflow_pw_script_type,workflow_cores,workflow_pw_output_file))
    # Pass output
    workflow_pw_output = cwlgen.WorkflowStepOutput('pw_output_file')
    workflow_pw.out.append(workflow_pw_output)
    #Add first step
    cwl_tool.steps.append(workflow_pw)

    #workflow for wstat.x
    workflow_wstat = cwlgen.workflow.WorkflowStep('wstat_tool',
                                               'wstat.cwl',
                                               doc='runs wstat.cwl')

    # Pass workflow step inputs to pw.cwl as needed. The ids are defined in pw.cwl
    workflow_wstat_input_file = cwlgen.WorkflowStepInput('input_file','wstat_input_file')
    workflow_wstat_script_type = cwlgen.WorkflowStepInput('script_type','wstat_script')
    workflow_wstat_output_file = cwlgen.WorkflowStepInput('output','wstat_output')
    workflow_wstat.inputs.extend((workflow_wstat_input_file,workflow_wstat_script_type,workflow_cores,workflow_wstat_output_file))
    # Pass output
    workflow_wstat_output = cwlgen.WorkflowStepOutput('wstat_output_file')
    workflow_wstat.out.append(workflow_wstat_output)
    # Add second step
    cwl_tool.steps.append(workflow_wstat)

    #Export cwl 
    cwl_tool.export("workflow.cwl")

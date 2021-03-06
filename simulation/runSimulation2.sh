#!/bin/bash

######################################
# Author: Jefri Draup                #
# Email: jefri.draup@edfenergy.com   #
######################################

# Please refer to Issue:
# https://gitlab.cs.man.ac.uk/mbgm6aab/weldingworkbench/issues/2

#### You need to set these up front ################################################################################
####################################################################################################################
#source /home/mbgm6aab/codes/tfel/master/install/env.sh
#export pathToSalome='/home/mbgm6aab/salome_meca/appli_V2019.0.3_universal'
#export pathToHere=$( pwd )
#export srcDir='/home/mbgm6aab/Documents/weldingworkbench'
####################################################################################################################
####################################################################################################################

####################################################################################################################
### Set environment variables
####################################################################################################################
source ../user.config

####################################################################################################################
### File Management
####################################################################################################################
rm -r $USER_WELDWB_srcDir/simulation/tmp
rm $USER_WELDWB_pathToHere/unsetMe
mkdir $USER_WELDWB_srcDir/simulation/tmp

####################################################################################################################
### Launch simulation
####################################################################################################################
pushd $USER_WELDWB_srcDir/simulation/tmp
cp $USER_WELDWB_srcDir/templates/* .
$USER_WELDWB_pathToSalome/salome shell killSalome.py	
$USER_WELDWB_pathToSalome/salome shell -- as_run $USER_WELDWB_srcDir/simulation/tmp/nonlinearthermal.export
$USER_WELDWB_pathToSalome/salome shell killSalome.py	
popd	

####################################################################################################################
### Clear environment variables
####################################################################################################################
printenv | grep 'USER_WELDWB_' | sed 's/=.*//' | sed 's/USER_/unset USER_'/ > $USER_WELDWB_pathToHere/unsetMe 
source $USER_WELDWB_pathToHere/unsetMe
rm ./unsetMe

####################################################################################################################
### END
####################################################################################################################

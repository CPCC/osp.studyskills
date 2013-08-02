osp.studyskills
===============

Study skills assessment application for OSP.

This application requires OSP version 1.3.5 or later to already be installed.
OSP is presently available at http://code.google.com/p/osp/.


To install the study skills assessment, clone the repository
and then run the setup script::

    cd osp.studyskills
    ./scripts/studyskills_setup.sh


This is not an unattended setup script. 
You will be prompted several times during the course of running it.
It is recommended you view the setup script prior to running it to ensure path references match those used in your original OSP installation. (If they do not match, you will need to either edit the script or perform a manual install).
When the script prompts you to edit your OSP settings, you should edit the settings file to enable onlinereadiness in the CUSTOM_ASSESSMENTS setting. 
You should make a backup of your existing OSP database prior to installing this application.

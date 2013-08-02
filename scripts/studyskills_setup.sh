# This setup script can be used to do an initial or updated install
# of the study skills assessment application for OSP. Your OSP
# should already have been upgraded to at least version 1.3.5
# prior to doing an initial install of this assessment application.
# Run script from repo root: ./scripts/setup.sh

echo ""
echo "Note - This application requires OSP version 1.3.5 or higher to already be installed."
echo "Do you wish to proceed? [Y/n] "
read CONTINUE_INSTALL

if [ "$CONTINUE_INSTALL" == "Y" ] || [ "$CONTINUE_INSTALL" == "y" ] || [ "$CONTINUE_INSTALL" == "" ]
then
    CONTINUE_INSTALL="y"
else
    CONTINUE_INSTALL="n"
fi

if [ $CONTINUE_INSTALL == "y" ]
then
    if [ -d "/opt/virtualenv/osp" ]
    then
        # OSP is installed in a virtualenv
        export WORKON_HOME=/opt/virtualenv
        source /usr/local/bin/virtualenvwrapper.sh
        workon osp
    fi

     Install assessment application into python library

    python setup.py install

    # Open osp settings file and verify study skills settings are enabled.
    echo ""
    echo "Open Django settings file for editing? [Y/n] "
    read EDIT_SETTINGS

    if [ "$EDIT_SETTINGS" == "Y" ] || [ "$EDIT_SETTINGS" == "y" ] || [ "$EDIT_SETTINGS" == "" ]
    then
        EDIT_SETTINGS="y"
    else
        EDIT_SETTINGS="n"
    fi

    if [ $EDIT_SETTINGS == "y" ]
    then
        # Open Django settings file for editing
        vim /opt/wsgi/osp_settings.py
        sudo touch /opt/wsgi/osp.wsgi
    else
        echo ""
    fi

    # Create or update database table(s) for study skills app in OSP database.
    echo ""
    echo -n "Update OSP database tables (did you back up your database first)? [Y/n] "
    read UPDATE_DATABASE

    if [ "$UPDATE_DATABASE" == "Y" ] || [ "$UPDATE_DATABASE" == "y" ] || [ "$UPDATE_DATABASE" == "" ]
    then
        UPDATE_DATABASE="y"
    else
        UPDATE_DATABASE="n"
    fi

    if [ $UPDATE_DATABASE == "y" ]
    then
        # Run south migration to install new tables.
        export PYTHONPATH=$PYTHONPATH:/opt/wsgi:/opt/django/osp
        django-admin.py migrate studyskills --settings=osp_settings
    fi
 fi



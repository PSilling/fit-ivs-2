#!/bin/bash
  
if [ -f "/usr/share/ivs-chicken-calc/ivs-icon.png" ]; then
    echo "You are about to uninstall ivs-chicken-calc program. Are you sure you want to uninstall it?(y/n)"
    read answer
    if echo "$answer" | grep -iq "^y" ;then
        sudo rm ./gui_calc.spec
        sudo rm -rf dist
        sudo rm -rf build
        sudo rm -rf ../src/__pycache__
	    sudo rm /usr/share/applications/gui_calc
        sudo rm -rf /usr/share/ivs-chicken-calc
        sudo rm /usr/share/applications/ivs-chicken-calc.desktop

        echo "Uninstallation was successful!"
    else
        echo "Uninstallation was cancelled"
        exit
    fi
    
else
    echo "Program is already uninstalled. You can install it via installer."
fi
    

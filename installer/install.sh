#!/bin/bash
 
if [ -f "/usr/share/ivs-chicken-calc/ivs-icon.png" ]; then
   echo "This file is already installed. You can uninstall it via uninstaller"
else
   if which pip3 >/dev/null; then
        echo "Checking dependecies..."
    else
        echo "Package 'pip3' is missing. Do you wish to install it?(y/n)"
        read answer
        if echo "$answer" | grep -iq "^y" ;then
            sudo apt install python3-pip
        else
            echo "Installation was not successful!"
            exit
        fi
    fi

    if which pyqt5 >/dev/null; then
        echo ""
    else
        echo "In order to install calculator you need to install pyqt5 first. Do you wish to install it?(y/n)"
        read answer
        if echo "$answer" | grep -iq "^y" ;then
            sudo -H pip3 install pyqt5 2>/dev/null
        else
            echo "Installation was not successful!"
            exit
        fi
    fi

    if which pyinstaller >/dev/null; then
        echo "You are about to install ivs-chicken-calc [~100MB]. Do you wish to install it?(y/n)"
        read answer
        if echo "$answer" | grep -iq "^y" ;then
            pyinstaller -F ../src/gui_calc.py
        else
            echo "Installation was not successful!"
            exit
        fi
    else
        echo "In orderd to install ivs-chicken-calc you need to install PyInstaller. Do you wish to install it?(y/n)"
        read answer
        if echo "$answer" | grep -iq "^y" ;then
            sudo -H pip3 install pyinstaller 2>/dev/null

            echo "You are about to install ivs-chicken-calc [~100MB]. Do you wish to install it?(y/n)"
            read answer
            if echo "$answer" | grep -iq "^y" ;then
                pyinstaller -F ../src/gui_calc.py
            else
                echo "Installation was not successful!"
                exit
            fi
        else
            echo "Installation was not successful!"
            exit
        fi
    fi
    echo "You need to enter your password to complete installation."
   
    sudo mv ./dist/gui_calc /usr/share/applications
    sudo mkdir /usr/share/ivs-chicken-calc
    sudo cp ../ivs-icon.png /usr/share/ivs-chicken-calc/
    chmod u+x "uninstall.sh"
    sudo mv ./uninstall.sh /usr/share/applications/
    cp /usr/share/applications/uninstall.sh ./
    if [ ! -e "ivs-chicken-calc.desktop" ]; then
        echo "[Desktop Entry]" >> "ivs-chicken-calc.desktop"
        echo "Version=1.0" >> "ivs-chicken-calc.desktop"
        echo "Type=Application" >> "ivs-chicken-calc.desktop"
        echo "Terminal=false" >> "ivs-chicken-calc.desktop"
        echo "Exec=/usr/share/applications/gui_calc" >> "ivs-chicken-calc.desktop"
        echo "Name=ivs-chicken-calc" >> "ivs-chicken-calc.desktop"
        echo "Comment=Simple calculator with GUI for second IVS project." >> "ivs-chicken-calc.desktop"
        echo "Icon=/usr/share/ivs-chicken-calc/ivs-icon.png" >> "ivs-chicken-calc.desktop"
        echo "Categories=Utility" >> "ivs-chicken-calc.desktop"
    fi 
    chmod u+x "ivs-chicken-calc.desktop"
    sudo mv ./ivs-chicken-calc.desktop /usr/share/applications

if [ ! -e "remove-chicken-calc.desktop" ]; then
        echo "[Desktop Entry]" >> "remove-chicken-calc.desktop"
        echo "Version=1.0" >> "remove-chicken-calc.desktop"
        echo "Type=Application" >> "remove-chicken-calc.desktop"
        echo "Terminal=true" >> "remove-chicken-calc.desktop"
        echo "Exec=/usr/share/applications/uninstall.sh" >> "remove-chicken-calc.desktop"
        echo "Name=remove-chicken-calc" >> "remove-chicken-calc.desktop"
        echo "Comment=Uninstaller for ivs-chicken-calc." >> "remove-chicken-calc.desktop"
        echo "Icon=/usr/share/ivs-chicken-calc/ivs-icon.png" >> "remove-chicken-calc.desktop"
        echo "Categories=Utility" >> "remove-chicken-calc.desktop"
    fi 
    chmod u+x "remove-chicken-calc.desktop"
    sudo mv ./remove-chicken-calc.desktop /usr/share/applications

sudo rm ./gui_calc.spec
        sudo rm -rf dist
        sudo rm -rf build
        sudo rm -rf ../src/__pycache__

    echo "Installation was successful!"
fi
# Importing HMI file to HMI Modbus Viewer App
![](/Tools/images/HMIModbusViewerApp.jpg)
1. Open The HMI Modbus Viewer App

    * **Continue to step 2 if you *are* met with this screen**:

        ![](/Tools/images/HMIModbusViewerImportScreen.jpg)

    * If you **are not** met with this screen:
        * Select "Start screen settings" from the top right app menu (three dots in a vertical line).

            ![](/Tools/images/HMIModbusViewerStartScreen.jpg)

        * When prompted to "Show the start window" select yes.

            ![](/Tools/images/HMIModbusViewerStartScreenPrompt.jpg)

        * Restart the app by pressing the system back button twice to close the app, then open the viewer again.
2. Select "Import project"
3. Navigate to where you downloaded the HMI file and select it.
4. The new HMI will loaded and be ready to use.

# If the app fails to communicate (elements greyed out / unresponsive):

![](/Tools/images/HMIModbusViewerGreyedOut.jpg)

1. Select "Edit servers list" from the top right app menu (three dots in a vertical line)

    ![](/Tools/images/HMIModbusViewerEditServersList.jpg)

2. From the server list page:
    
    ![](/Tools/images/HMIModbusViewerServersList.jpg)
    
    * First select "Apply the server to all elements"
    * Then select the server you want to switch to.

### If the server is not in the list
1. ensure the device is connected
    * Bluetooth is paired to Tablet

    or

    * USB is properly connected
2. Add the server to the list with the corresponding button at the top bar of the server list page.
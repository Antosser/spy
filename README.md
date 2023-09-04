# Spy
This software creates a screenshot around the cursor every time the user clicks and saves all images highly compressed.  
By default, the files are saved under `~/spy/yyyy-mm-dd/hh-mm-ss-ffff.jpg`

# Installation
1. Extract this repository into any folder.
2. Install Python
3. Run both `.bat` files
4. Make sure that .pyw file are opened by Python by default by double-clicking `main.pyw` and selecting Python in the `Open With` menu.

# Removal
* Remove `main.pyw` from the `%appdata%/Microsoft/Windows/Start Menu/Programs/Startup` directory.
* Kill the Python task by searching `Python` in Task Manager and killing the results.

# Configuration
You can configure the app by changing the three variables in the `%appdata%/Microsoft/Windows/Start Menu/Programs/Startup/main.pyw` file.  
Defaults:
```
image_radius = 400
image_quality = 20 # 0 - 100
directory_name = 'spy'
```

# Notice
This software is not intended for malicious purposes.

# License
Copying and distribution of this file, with or without modification, are permitted in any medium provided you do not contact the author about the file or any problems you are having with the file.
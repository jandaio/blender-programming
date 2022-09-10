#Progress written by Alejandro

* Blender version installed 3.3 with python 3.10.2 ( import sys print(sys.version_info) in python console )
* Hello world , first aproaches with default library bpy 
  * To use on the blender python text IDE it is necessary to import bpy , but on other hand if you are on the line by line interpreter is imported by default.
  * Access to a blender object example bpy.data.objects['Cube']
* It is not a nice IDE to work on blender python editor, I can imagine that it is better to match version and them use visual code.. on going....

Visual Code
* I follow this link https://b3d.interplanety.org/en/using-microsoft-visual-studio-code-as-external-ide-for-writing-blender-scripts-add-ons/ :
  * install the python extension by microsoft, you can search the extension ctrl +shit +x . intelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refacto . NOTE: The visual code would prompt a popup asking to install this anyways. 
  * I noticed that the blender text editor and the visual code editor intellisense does not work by default for python API's so I did this following steps:
    * install blender_autocomplete project with git clone https://github.com/Korchy/blender_autocomplete.git  ( or you can download it from that github repository where each folder is related with the blender version that you what to use ). Example folder installed at 'C:/Users/aleco/Documents/Desarrollos/GitHub/common/blender_autocomplete/3.2'
   * Add the following two lines on the user setting workspace JSON FILE:
    ```json 
        {
           "python.linting.pylintArgs": [
             "--init-hook",
             "import sys; sys.path.append('C:/Users/aleco/Documents/Desarrollos/GitHub/common/blender_autocomplete/3.2')"], 
            "python.analysis.extraPaths": ["C:/Users/aleco/Documents/Desarrollos/GitHub/common/blender_autocomplete/3.2"]
        } 
    ```
  * I have tested two ways to execute Blender python script done in visual code :
    * Manually execute each time the code created in Visual Code creating a code in blender like this one:
    * ```python
      import bpy
      import os
   
      filename = os.path.join("C:/Users/aleco/Documents/Desarrollos/GitHub/blender-programming/test/", "testing.py")
      exec(compile(open(filename).read(), filename, 'exec'))
      ```
     * Dinamically:
       install the “Blender Development” extension by Jacques Lucke 
       
       
       
   

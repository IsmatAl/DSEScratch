# thesisProject

This project is part of my thesis 'Dynamic analysis of Scratch code to infer CT skills'

Scratch projects that can be processed by the app must be definitions of custom blocks. Blocks to be used as part of custom block definitions must belong to one of the following categories:

    1. Operators
    2. Control (except wait_seconds, wait_untill, when_I_start, create_clone_of, delete_this_clone)
    3. Looks (only say_x_for_n_seconds, say_x blocks)
    4. Variables ( only set_var_to_x, change_var_by_x blocks)

The arguments of custom blocks must be integers but return types can be strings as well as integers

Before starting to launch the app make sure the following list of programming languages and tools are installed:
 1. Python (https://www.python.org/downloads/). Make sure it is added to the system's Path environment
 2. Graphiz (https://graphviz.org/download/source/). This link can be usefull (https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft)
 3. npm (https://www.npmjs.com/get-npm). The version should be 6. npm install -g npm@6
 
 

In order to start the app execute the following commands in the specified folders


  inside front-end\
    npm install\
    npm run start
  
  inside project root file:\
    python -m venv env
    .\env\Scripts\activate

  inside backend:\
    pip install -r .\requirements.txt OR install every item in the requirement.txt file one by one manually, (e.g, pip install z3) in case of an error\
    cd .\dynamicanalysis\
    python manage.py runserver

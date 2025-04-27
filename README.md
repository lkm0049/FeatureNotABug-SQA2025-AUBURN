# FeatureNotABug-SQA2025-AUBURN
Group Project for COMP 5710 Software Quality Assurance with Dr. Effat Farhana at Auburn University

Team Name:  Feature Not A Bug </br>
Team Members: Liam Maher, Trey Edmondson

Notes:
- Important:  The Github Actions for Bandit was not required in the instructions, all edits made after the deadline were me trying to get it to work just out of curiosity.  Nothing else was modified after the deadline besides the GitHub Actions for the Bandit Pre-commit.
- To make the project run as intended, the provided Dockerfile and environment.yml had to be slightly modified.  We have included those updated files here.  They are not included in the `KubeSec-master/` directory, as we wanted to keep the submission documents in one place.
- The precommit git hook that is required, is included in the `hooks/` directory, to make it easier to view the usage.
- Screenshots of successful execution have been included in the `screenshots/` directory.

Results and Scripts:
- Included in the `KubeSec-master/` directory are the scripts that were modified for this project.
- Included in the `KubeSec-master/results/` directory are the results from running specific parts of the project.

Commands to Run:
- Build the docker image:
  - ```docker build --no-cache -t slikube .```
- Run the script and output to the results directory:
  
  ```bash
  docker run -it --rm \
    --name slikube-container \
    -v "$(pwd)/results:/results" \
    slikube

Breakdown of Work Done:
  - 4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed.
      - Hook created and present in the `hooks/` directory.
  - 4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the `fuzz.py` file. `fuzz.py` will be automatically executed from GitHub actions.
  - 4.c. Integrate forensics by modifying 5 Python methods of your choice.
     - Files modified, with corresponding methods:
         - `main.py`:
           - `main()`
           - `getCountFromAnalysis()`
         - `parser.py`:
           - `loadMultiYAML()`
           - `checkParseError()`
         - `scanner.py`:
           - `scanSingleManifest()`
           - `runScanner()`
         - `graphtaint.py`:
           - `getMatchingTemplates()`
           - `getValidTaints()`
    

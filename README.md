# FeatureNotABug-SQA2025-AUBURN
Group Project for COMP 5710 Software Quality Assurance with Dr. Effat Farhana at Auburn University

Team Name:  Feature Not A Bug </br>
Team Members: Liam Maher, Trey Edmondson

Notes:
- To make the project run as intended, the provided Dockerfile and environment.yml had to be slightly modified.  We have included those updated files here.  They are not included in the `KubeSec-master/` directory, as we wanted to keep the submission documents in one place.

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


Report
------

Lessons Learned:
--
Fuzzing: Learning to spot typing and variable assignment issues is extremely valuable to fix issues in code to minimize unexpected behavior when dealing with user and file input when you can’t guarantee  its integrity.

GitHub Actions: Learning to have GitHub automate scripts running can help find bugs when dealing with large repositories with many contributors.

Git Hook: Git hooks help prevent bad code from being commited and showing possible errors and functionality issues to the user before commiting

Forensics: Constant logging allow program tracking to quickly locate bugged code when dealing with large codebases

Activities:
----------
## 4.a Git Hook for Static Analysis  
**What we did**  
- Wrote a pre-commit hook (`.git/hooks/pre-commit`) that checks whether any `.py` files are staged.  
- If so, it runs Bandit recursively over the entire repo and writes `results/bandit_report.csv`.  
- If no Python files changed, it prints “No Python files changed. Skipping Bandit scan.”  

**What we learned**  
- How to detect staged file changes in a shell script.  
- How to integrate Bandit into a Git hook.  

---

## 4.b Fuzzing with `fuzz.py`  
**What we did**  
- Selected five representative functions in our parser and scanner modules.  
- Wrote `fuzz.py` to generate random inputs (malformed strings, extreme numeric values, missing keys) and invoke each function in a loop.  
- Logged any exceptions or assertion failures to `results/fuzz_report.txt`.  

**What we learned**  
- Even simple boundary and type fuzzing uncovers edge-case bugs (e.g. unhandled `None` inputs, unexpected list lengths).  
- Automating fuzz tests in a single script makes it easy to re-run after every change.  

---

## 4.c Forensic Instrumentation  
**What we did**  
- Added detailed logging (timestamps, call stacks) to five core methods involved in parsing, data transformation, and JSON output.  
- Ensured that every entry in our logs includes a unique request ID and execution context.  
- Verified that logs persist through errors and can be correlated to specific input files.  

**What we learned**  
- How lightweight instrumentation can dramatically improve debugging.  
- The importance of consistent, structured log formats for traceability.  



Contributions:
-------------
Trey Edmondson - Fuzz.py and Fuzz Action Runner

Liam Maher - Repo creation, git hook + bandit, forensics

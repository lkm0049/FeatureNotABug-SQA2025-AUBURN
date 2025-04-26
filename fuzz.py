from graphtaint import constructHelmString
from graphtaint import getValidTaints
import scanner

def fuzzer():

    #Fuzzing graphtaint's constructHelmString function with a tuple not of size 3
    #upper_key, key, _ = hiera_tuple does not verify integrity of the tuple before attempting to assign it
    try:
        print(constructHelmString(('only', 'two')))
    except Exception as e:
        print(f"Error: {e}")

    try:
        print(constructHelmString(('is', 'one', 'too', 'many')))
    except Exception as e:
        print(f"Error: {e}")

    #Fuzzing scanner's runScanner function with an invalid folder directory
    #Tries to return empty value sarif_json which errors out
    try:
        content_as_ls, sarif_json = scanner.runScanner('/nonexistant/')
    except Exception as e:
        print(f"Error: {e}")

    #Fuzzing graphtaint's getValidTaints function with a tuple of not size two
    #script_name, helm_string = match does not verify integrity of the tuple before assigning it
    try:
        script_name, helmstring = getValidTaints(("one", "too", "many"))
    except:
        print(f"Error: {e}")
    try:
        script_name, helmstring = getValidTaints(("notenough"))
    except:
        print(f"Error: {e}")
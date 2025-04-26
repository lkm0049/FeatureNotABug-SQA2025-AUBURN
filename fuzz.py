import graphtaint
import scanner

def fuzzer():

    print("Fuzzing graphtaint's constructHelmString function with a tuple not of size 3")
    #upper_key, key, _ = hiera_tuple does not verify integrity of the tuple before attempting to assign it
    try:
        print(graphtaint.constructHelmString(('only', 'two')))
    except Exception as e:
        print(f"Error: {e}")

    try:
        print(graphtaint.constructHelmString(('is', 'one', 'too', 'many')))
    except Exception as e:
        print(f"Error: {e}")

    #Fuzzing scanner's runScanner function with an invalid folder directory
    #Tries to return empty value sarif_json which errors out
    print("Fuzzing scanner's runScanner function with an invalid folder directory")
    try:
        content_as_ls, sarif_json = scanner.runScanner('/nonexistant/')
    except Exception as e:
        print(f"Error: {e}")

    #Fuzzing graphtaint's getValidTaints function with a tuple of not size two
    #script_name, helm_string = match does not verify integrity of the tuple before assigning it
    print("Fuzzing graphtaint's getValidTaints function with a tuple of not size two")
    try:
        script_name, helmstring = graphtaint.getValidTaints(("one", "too", "many"))
    except Exception as e:
        print(f"Error: {e}")
    try:
        script_name, helmstring = graphtaint.getValidTaints(("notenough"))
    except Exception as e:
        print(f"Error: {e}")

    #Fuzzing scanner's scanUserName function with a noniterable type None
    #for val_ in val_lis: where val_list is not typechecked
    print("Fuzzing scanner's scanUserName function with a noniterable type None")
    try:
        names = scanner.scanUserName('user', None)
    except Exception as e:
        print(f"Error: {e}")

    #Fuzzing scanner's scanPasswords function with a noniterable type None
    #for val_ in val_lis: where val_list is not typechecked
    print("Fuzzing scanner's scanPasswords function with a noniterable type None")
    try:
        passwords = scanner.scanPasswords('passwd', None)
    except Exception as e:
        print(f"Error: {e}")
'''
Akond Rahman 
Sep 21, 2022
Source Code to Run Tool on All Kubernetes Manifests 
Test GitHook TEST
'''
import scanner 
import pandas as pd 
import constants
import typer
from pathlib import Path
#import myLogger
import myLogger
logObj = myLogger.giveMeLoggingObject()


def getCountFromAnalysis(ls_):
    #LOG 4: Show that the analysis is being performed on the scanner results
    logObj = myLogger.giveMeLoggingObject()
    logObj.info("LOG 4: Analyzing result tuples from scanner output")
    list2ret           = []
    for tup_ in ls_:
        within_sec_cnt = 0 
        dir_name       = tup_[0]
        script_name    = tup_[1]        
        within_secret  = tup_[2]  # a list of dicts: [unameDict, passwordDict, tokenDict]
        within_sec_cnt = len(within_secret[0]) + len( within_secret[1]  ) + len( within_secret[2] )
        '''
        ### format: ('data', 'password', ([], ['MTIzNAo='], [])) => (<rootKey>, <key>, <data_list>) ... need the list of the last tuple
        if isinstance( within_secret, tuple ):
            within_sec_cnt = len( within_secret[-1][1] )
            # print( script_name,  within_secret, within_sec_cnt, type(within_secret) ) 
        '''
        templa_secret  = tup_[3]       ### format: a list , we will not use this in dumping       
        taint_secret   = tup_[4]       ###   format: a list 
        privilege_dic  = tup_[5]
        http_dict      = tup_[6]        
        secuContextDic = tup_[7]
        nSpaceDict     = tup_[8]                
        absentResoDict = tup_[9]                 
        rollUpdateDic  = tup_[10]
        netPolicyDict  = tup_[11]                
        pidfDict       = tup_[12]                
        ipcDict        = tup_[13]                 
        dockersockDic  = tup_[14]
        hostNetDict    = tup_[15]                        
        cap_sys_dic    = tup_[16]
        host_alias_dic = tup_[17]
        allow_priv_dic = tup_[18]
        unconfined_dic = tup_[19]
        cap_module_dic = tup_[20]
        k8s_flag       = tup_[21]
        helm_flag      = tup_[22]

        list2ret.append(  ( dir_name, script_name, within_sec_cnt, len(taint_secret), len(privilege_dic), len(http_dict), len(secuContextDic), len(nSpaceDict), len(absentResoDict), len(rollUpdateDic), len(netPolicyDict), len(pidfDict), len(ipcDict), len(dockersockDic), len(hostNetDict), len(cap_sys_dic), len(host_alias_dic), len(allow_priv_dic), len(unconfined_dic), len(cap_module_dic) , k8s_flag, helm_flag  )  )
        #LOG 5:  Show that getCountFromAnalysis is complete and then list the number of entries returned.
        logObj.info("LOG 5: getCountFromAnalysis completed. {} entries returned.".format(len(list2ret)))
    return list2ret


def main(directory: Path = typer.Argument(..., exists=True, help="Absolute path to the folder than contains Kubernetes manifests"),
         ):
    """
    Run KubeSec in a Kubernetes directory and get results in a CSV file.

    """
    #LOG 1: Show that it is beginning the analysis and on which directory
    logObj.info("LOG 1: Starting KubeSec analysis on directory: {}".format(directory))
    content_as_ls, sarif_json   = scanner.runScanner( directory )
    
    with open("SLIKUBE.sarif", "w") as f:
      f.write(sarif_json)
      #LOG 2: Show that the sarif file has been created
      logObj.info("LOG 2: SARIF output saved to SLIKUBE.sarif")

    df_all          = pd.DataFrame( getCountFromAnalysis( content_as_ls ) )
    outfile = Path(directory, "slikube_results.csv")

    df_all.to_csv( outfile, header= constants.CSV_HEADER , index=False, encoding= constants.CSV_ENCODING )
    #LOG 3: Show that the CSV file has been created.
    logObj.info("LOG 3: CSV results saved to {}".format(outfile))


if __name__ == '__main__':

    '''
    DO NOT DELETE ALL IN K8S_REPOS AS TAINT TRACKING RELIES ON BASH SCRIPTS, ONE OF THE STRENGTHS OF THE TOOL 
    '''
    ORG_DIR         = '../home/TEST_ARTIFACTS/'
    OUTPUT_FILE_CSV = './PROJECT_MAIN_OUTPUT.csv'

    # ORG_DIR         = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_GITLAB_OUTPUT.csv'


    # ORG_DIR         = '/Users/arahman/K8S_REPOS/BRINTO_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_BRINTO_OUTPUT.csv'

    # take sarif_json from scanner
    typer.run(main)








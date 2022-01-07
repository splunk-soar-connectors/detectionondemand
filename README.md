[comment]: # "Auto-generated SOAR connector documentation"
# Detection on Demand

Publisher: FireEye  
Connector Version: 1\.0\.2  
Product Vendor: FireEye  
Product Name: Detection on Demand  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.8\.24304  

This app integrates with FireEye's Detection on Demand service to identify malicious files and hashes

[comment]: # ""
[comment]: # "File: readme.md"
[comment]: # ""
[comment]: # "Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
For more information, visit <https://fireeye.dev/docs/detection-on-demand/> .  
  
Have suggestions for improvement to this app? Contact us at
[developers@fireeye.com](mailto:%20developers@fireeye.com) .


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Detection on Demand asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | The base url of the Detection on Demand API to connect to
**api\_token** |  required  | password | An API token for accessing the Detection on Demand API

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[detonate file](#action-detonate-file) - Execute a file in FireEye's various detection engines to determine what malicious behaviors, if any, the file exhibits  
[detonate url](#action-detonate-url) - Send a URL to Detection on Demand to scan for malicious behavior and artifacts  
[lookup hash](#action-lookup-hash) - Search FireEye's hash database to see if there is already a report on the file  
[get report](#action-get-report) - Get a detailed report on the execution results of a submitted file  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'detonate file'
Execute a file in FireEye's various detection engines to determine what malicious behaviors, if any, the file exhibits

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault\_id** |  required  | Vault ID of file to detonate | string |  `pe file`  `pdf`  `flash`  `apk`  `jar`  `doc`  `xls`  `ppt`  `txt`  `vault id` 
**password** |  optional  | Password to be used by the detection engine to decrypt a password protected file | string | 
**param** |  optional  | Command line parameter\(s\) to be used by detection engine when running the file\. Mainly applicable to \.exe files\. For example, setting param to "start \-h localhost \-p 5555" will make the detection engine run a file named "malicious\.exe" as "malicious\.exe start \-h localhost \-p 5555" | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.vault\_id | string |  `pe file`  `pdf`  `flash`  `apk`  `jar`  `doc`  `xls`  `ppt`  `txt`  `vault id` 
action\_result\.parameter\.password | string | 
action\_result\.parameter\.param | string | 
action\_result\.data\.\*\.report\_id | string |  `detectionondemand report id` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'detonate url'
Send a URL to Detection on Demand to scan for malicious behavior and artifacts

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | The URL to analyze | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.url | string |  `url` 
action\_result\.data\.\*\.report\_id | string |  `detectionondemand report id` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'lookup hash'
Search FireEye's hash database to see if there is already a report on the file

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**md5\_hash** |  required  | The MD5 hash of the file to investigate | string |  `md5` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.md5\_hash | string |  `md5` 
action\_result\.data\.\*\.is\_malicious | boolean |  `detectionondemand is malicious` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get report'
Get a detailed report on the execution results of a submitted file

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report\_id** |  required  | ID of the report to view | string |  `detectionondemand report id` 
**presigned\_url\_expiry** |  required  | Number of hours to let the presigned URL be active for | numeric | 
**poll\_interval** |  required  | Number of seconds to wait between each request to get the report | numeric | 
**poll\_attempts** |  required  | Total number of attempts to fetch the report before failing | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.report\_id | string |  `detectionondemand report id` 
action\_result\.parameter\.presigned\_url\_expiry | numeric | 
action\_result\.parameter\.poll\_interval | numeric | 
action\_result\.parameter\.poll\_attempts | numeric | 
action\_result\.data\.\*\.file\_name | string |  `file name` 
action\_result\.data\.\*\.urls | string |  `url` 
action\_result\.data\.\*\.is\_malicious | boolean |  `detectionondemand is malicious` 
action\_result\.data\.\*\.presigned\_report\_url | string |  `detectionondemand presigned report url` 
action\_result\.data\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.report\_id | string |  `detectionondemand report id` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
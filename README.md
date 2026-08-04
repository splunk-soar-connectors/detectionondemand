# Detection on Demand

Publisher: FireEye <br>
Connector Version: 3.0.0 <br>
Product Vendor: FireEye <br>
Product Name: Detection on Demand <br>
Minimum Product Version: 4.8.24304

This app integrates with FireEye's Detection on Demand service to identify malicious files and hashes

### Configuration variables

This table lists the configuration variables required to operate Detection on Demand. These variables are specified when configuring a Detection on Demand asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** | required | string | The base url of the Detection on Demand API to connect to |
**api_token** | required | password | An API token for accessing the Detection on Demand API |
**verify_server_cert** | optional | boolean | Verify the TLS certificate presented by the Detection on Demand API |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration <br>
[detonate file](#action-detonate-file) - Execute a file in FireEye's various detection engines to determine what malicious behaviors, if any, the file exhibits <br>
[detonate url](#action-detonate-url) - Send a URL to Detection on Demand to scan for malicious behavior and artifacts <br>
[lookup hash](#action-lookup-hash) - Search FireEye's hash database to see if there is already a report on the file <br>
[get report](#action-get-report) - Get a detailed report on the execution results of a submitted file

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** <br>
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'detonate file'

Execute a file in FireEye's various detection engines to determine what malicious behaviors, if any, the file exhibits

Type: **generic** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault_id** | required | Vault ID of file to detonate | string | `pe file` `pdf` `flash` `apk` `jar` `doc` `xls` `ppt` `txt` `vault id` |
**password** | optional | Password to be used by the detection engine to decrypt a password protected file | string | |
**param** | optional | Command line parameter(s) to be used by detection engine when running the file. Mainly applicable to .exe files. For example, setting param to "start -h localhost -p 5555" will make the detection engine run a file named "malicious.exe" as "malicious.exe start -h localhost -p 5555" | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.vault_id | string | `pe file` `pdf` `flash` `apk` `jar` `doc` `xls` `ppt` `txt` `vault id` | |
action_result.parameter.password | string | | |
action_result.parameter.param | string | | |
action_result.data.\*.report_id | string | `detectionondemand report id` | 9f7dd79d-1e94-473d-bef9-bd405a04336a |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'detonate url'

Send a URL to Detection on Demand to scan for malicious behavior and artifacts

Type: **generic** <br>
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** | required | The URL to analyze | string | `url` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.url | string | `url` | https://www.test.com |
action_result.data.\*.report_id | string | `detectionondemand report id` | 9f7dd79d-1e94-473d-bef9-bd405a04336a |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'lookup hash'

Search FireEye's hash database to see if there is already a report on the file

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**md5_hash** | required | The MD5 hash of the file to investigate | string | `md5` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.md5_hash | string | `md5` | 4ba739fd8c216809e485e7972597c995 |
action_result.data.\*.is_malicious | boolean | `detectionondemand is malicious` | True False |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get report'

Get a detailed report on the execution results of a submitted file

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**report_id** | required | ID of the report to view | string | `detectionondemand report id` |
**presigned_url_expiry** | required | Number of hours to let the presigned URL be active for | numeric | |
**poll_interval** | required | Number of seconds to wait between each request to get the report | numeric | |
**poll_attempts** | required | Total number of attempts to fetch the report before failing | numeric | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.report_id | string | `detectionondemand report id` | |
action_result.parameter.presigned_url_expiry | numeric | | |
action_result.parameter.poll_interval | numeric | | |
action_result.parameter.poll_attempts | numeric | | |
action_result.data.\*.file_name | string | `file name` | malware.exe |
action_result.data.\*.urls | string | `url` | https://www.test.com |
action_result.data.\*.is_malicious | boolean | `detectionondemand is malicious` | True False |
action_result.data.\*.presigned_report_url | string | `detectionondemand presigned report url` | https://public-feapi.marketplace.apps.fireeye.com/reports/874da611-f82a-4331-afde-5943f4facb92?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZXBvcnup67QiOiJlZWE4NmM1Yi01YWJiLTQ3MmItYWEwYi0zYjY3NDkxM2MwZmIiLCJleHAiOjE1ODc5MjM4ODJ9.qVx5iTZKBPsbRLIc1iIiLj3BI9nzimPaSB087AHPn1Y |
action_result.data.\*.md5 | string | `md5` | 1512e23daa92e6f178b3a6cdac4d507a |
action_result.data.\*.report_id | string | `detectionondemand report id` | 9f7dd79d-1e94-473d-bef9-bd405a04336a |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2026 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

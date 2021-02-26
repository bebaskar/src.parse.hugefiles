# src.palo.alto.sre.test
Coding assignments - Sr SRE role

Overview
This repository houses code for test exercises for a SRE role in PaloAlto Networks.

The main directory is
./paloAlto

<b>File structure,</b>

./src.palo.alto.sre.test/logFile holds the content of server access logs
./src.palo.alto.sre.test/util file holds the helper methods related to server log parsing
./src.palo.alto.sre.test/main file is the main executable file

Refer requirements.txt for Python3 packages used in the repo.

To execute the script, run  python main.py -h

<b>Sample help response,</b>

usage: python main.py --get10MaxRequestedPage --getPercentageOfSuccessRequest --getPercentageOfNotSuccessRequest --getTop10SuccessPageRequest --getTop10UnSuccessPageRequest --get10TopHosts

Analyzing server logs placed under paloAlto/logFile


optional arguments:
  -h, --help            show this help message and exit
  --get10MaxRequestedPage [GET10MAXREQUESTEDPAGE]
                        Get top 10 requested URI
												
  --getPercentageOfSuccessRequest [GETPERCENTAGEOFSUCCESSREQUEST]
                        Percentage of successful requests (anything in the 200s and 300s range)
												
  --getPercentageOfNotSuccessRequest [GETPERCENTAGEOFNOTSUCCESSREQUEST]
                        Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
												
  --getTop10SuccessPageRequest [GETTOP10SUCCESSPAGEREQUEST]
                        Percentage of successful requests (anything that is not in the 200s or 300s range)
												
  --getTop10UnSuccessPageRequest [GETTOP10UNSUCCESSPAGEREQUEST]
                        Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
												
  --get10TopHosts [GET10TOPHOSTS]
                        The top 10 hosts making the most requests, displaying the IP address and number of requests made.
												


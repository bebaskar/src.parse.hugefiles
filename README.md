<b>Overview</b>
This repository houses code for test exercises for a SRE role in PaloAlto Networks.

The main directory is
./src.palo.alto

<b>File structure,</b>

./src.palo.alto/logFile holds the content of server access logs

./src.palo.alto/util file holds the helper methods related to server log parsing

./src.palo.alto/main file is the main executable file

Refer requirements.txt for Python3 packages used in the repo.

To execute the script, run  python main.py -h

<b>Sample help,</b>

(studies) bdharmaraja-a01:paloAlto bdharmarajan$ python main.py -h

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
												
<b>Sample request and response,</b>

(studies) bdharmaraja-a01:paloAlto bdharmarajan$ python main.py --getPercentageOfSuccessRequest --getPercentageOfNotSuccessRequest --get10TopHosts  --getTop10SuccessPageRequest --getTop10UnSuccessPageRequest --get10TopHosts

INFO:root:---------------------

INFO:root:Executing the query,

INFO:root:---------------------

INFO:root:Percentage of successful requests (anything in the 200s and 300s range),
92.35602094240838

INFO:root:Percentage of unsuccessful requests (anything not in the 200s and 300s range),
4.7643979057591626

INFO:root:Top 10 successful requests(anything in the 200s and 300s range - 
['/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53', '/apache-log/access.log', '/robots.txt', '/index.php?option=com_phocagallery&view=category&id=2%3Awinterfotos&Itemid=53', '/administrator/index.php', '/', '/modules/mod_bowslideshow/tmpl/css/bowslideshow.css', '/templates/jp_hotel/css/template.css', '/templates/jp_hotel/css/layout.css', '/templates/jp_hotel/css/menu.css']

INFO:root:Top 10 unsuccessful requests(anything not in the 200s and 300s range - 
['/favicon.ico', '/administrator/%22', '/templates/_system/css/general.css', '/index.php?option=com_easyblog&view=dashboard&layout=write', '/libraries/joomla/template/mark.php', '/wp-login.php', '/87/5.php', '/icons/blank.gif', '/icons/back.gif', '/icons/text.gif']

INFO:root:Top 10 hosts making requests - 
[('45.132.207.221', 110), ('45.153.227.31', 108), ('45.132.51.62', 104), ('45.144.0.179', 102), ('45.132.51.36', 100), ('45.138.145.131', 96), ('45.138.4.22', 90), ('45.144.0.98', 88), ('45.138.145.106', 84), ('176.222.58.254', 82)]


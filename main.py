from util import  util
import os
import sys
import logging
import argparse
import pdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class logParser(util):
    """Initialize Util class"""

    def __init__(self, logFile):
        super().__init__(logFile)
        super().readLines()

    def get10MaxRequestedPage(self, length= 10):
        return sorted(self.ipPages.items(), key = lambda kv:kv[1], reverse=True)[:length]

    def getPercentageOfSuccessRequest(self):
        for total, status in self.ipResponse.items():
            logging.debug("Total number of api requests received are, {}".format(total))
            for res,resCount in status.items():
                if ("200" or "300") in res:
                    success = int(resCount)
        return (success / total) * 100

    def getPercentageOfNotSuccessRequest(self):
        for total, status in self.ipResponse.items():
            logging.debug("Total number of api requests received are, {}".format(total))
            for res,resCount in status.items():
                if ('200' or '300') not in str(res):
                    failure = int(resCount)
        return (failure / total) * 100

    def getTop10SuccessPageRequest(self, length=10):
        res = []
        for total, status in self.pageResponse.items():
            if ('200' or '300') in str(status):
                    res.append(total)
        logging.debug("Total {} number of pages are requested in the server".format(len(res)))
        logging.info("Top 10 successful requests(anything in the 200s and 300s range - \n{}".format(res[:length]))
        return res[:length]

    def getTop10UnSuccessPageRequest(self, length=10):
        res = []
        for total, status in self.pageResponse.items():
            if ('200' or '300') not in str(status):
                    res.append(total)
        logging.debug("Total {} number of pages are requested in the server".format(len(res)))
        logging.info("Top 10 unsuccessful requests(anything not in the 200s and 300s range - \n{}".format(res[:length]))
        return res[:length]

    def get10TopHosts(self, length=10):
        logging.debug("Fetching the top {} hosts which executed most number of requests and its count ".format(length))
        return sorted(self.ipMap.items(), key=lambda kv: kv[1], reverse=True)[:length]

def main():
    parser = argparse.ArgumentParser(usage='python main.py'
                                     ' --get10MaxRequestedPage'
                                     ' --getPercentageOfSuccessRequest'
                                     ' --getPercentageOfNotSuccessRequest'
                                     ' --getTop10SuccessPageRequest'
                                     ' --getTop10UnSuccessPageRequest'
                                     ' --get10TopHosts',
                                     description='Analyzing server logs placed under src.palo.alto.sre.test/logFile')
    parser.add_argument('--get10MaxRequestedPage', help='Get top 10 requested URI', nargs='?', const=1, type=int)
    parser.add_argument('--getPercentageOfSuccessRequest', help='Percentage of successful requests (anything in the 200s and 300s range)', nargs='?', const=1, type=int)
    parser.add_argument('--getPercentageOfNotSuccessRequest', help='Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)', nargs='?', const=1, type=int)
    parser.add_argument('--getTop10SuccessPageRequest',
                        help='Top 10 successful requests(anything that is not in the 200s or 300s range)', nargs='?', const=1, type=int)
    parser.add_argument('--getTop10UnSuccessPageRequest',
                        help='Top 10 unsuccessful requests(anything that is not in the 200s or 300s range)', nargs='?', const=1, type=int)
    parser.add_argument('--get10TopHosts',
                        help='The top 10 hosts making the most requests, displaying the IP address and number of requests made.', nargs='?', const=1, type=int)
    args = parser.parse_args()
    # Specify path
    path = 'logFile'

    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        logging.info("Server logs are not found {}".format(path))
        sys.exit()


    try:
        logging.info('---------------------')
        logging.info('Executing the query,')
        logging.info('---------------------')
        obj = logParser(path)
        if args.get10MaxRequestedPage:
            logging.info("Top 10 requested URI, ")
            print(obj.get10MaxRequestedPage())
        if args.getPercentageOfSuccessRequest:
            logging.info("Percentage of successful requests (anything in the 200s and 300s range),")
            print(obj.getPercentageOfSuccessRequest())
        if args.getPercentageOfNotSuccessRequest:
            logging.info("Percentage of unsuccessful requests (anything not in the 200s and 300s range),")
            print(obj.getPercentageOfNotSuccessRequest())
        if args.getTop10SuccessPageRequest:
            obj.getTop10SuccessPageRequest()
        if args.getTop10UnSuccessPageRequest:
            obj.getTop10UnSuccessPageRequest()
        if args.get10TopHosts:
            logging.info("Top 10 hosts making requests - ")
            print(obj.get10TopHosts())


    except ValueError as e:
        logging.error('Upgrade process failed')
        raise e

if __name__ == '__main__':
    main()


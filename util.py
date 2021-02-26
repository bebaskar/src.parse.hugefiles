import re
from collections import OrderedDict
import logging

"""Utility Helper class"""
class util:

    """@:param fileName - Server access logs
       Please note regex expects the log string in the format of -
       IPv4 - - [DateTime] "REST METHOD URI HTTP/1.1" REST_STATUS_CODE *** "-"
    """
    def __init__(self, fileName):
        self.regex = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(GET|PUT|POST|DELETE|PATCH|HEAD)(.*)HTTP.\S+\"\W(\d+).*(?![\w\d])$"
        self.logFile = fileName
        self.ipMap = OrderedDict()
        self.ipResponse = OrderedDict()
        self.ipPages = OrderedDict()
        self.pageResponse = OrderedDict()
        self.response = {}
        self.lineCount = 0

    def readLines(self):
        file = open(self.logFile, 'r')
        Lines = file.readlines()
        for line in Lines:
            self.lineCount +=1
            self.parse(line.strip())

        self.ipResponse[self.lineCount] = self.response
        for k, v in self.ipMap.items():
            logging.debug("Ip map contents")
            logging.debug("{} ---> {}".format(k, v))
        for k, v in self.ipPages.items():
            logging.debug("Ip pages contents")
            logging.debug("{} ---> {}".format(k, v))
        for k, v in self.ipResponse.items():
            logging.debug("Ip response code contents")
            logging.debug("{} ---> {}".format(k, v))

    def parse(self, test_str):
        try:
            matches = re.finditer(self.regex, test_str, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                logging.debug(
                    "Match {matchNum} was found t {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                                 end=match.end(), match=match.group()))

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                ipAddress = str(match.group(1)).strip()
                restResponse = str(match.group(4)).strip()
                page = str(match.group(3)).strip()

                logging.debug("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                                start=match.start(groupNum),
                                                                                end=match.end(groupNum),
                                                                                group=match.group(groupNum)))

            self.ipPages[page] = 1 if page not in self.ipPages.keys() else int(self.ipPages[page]) + 1
            self.ipMap[ipAddress] = 1 if ipAddress not in self.ipMap.keys() else int(self.ipMap[ipAddress]) + 1
            self.response[restResponse] = 1 if restResponse not in self.response.keys() else int(self.response[restResponse]) + 1
            self.pageResponse[page] = restResponse

        except Exception as e:
            logging.exception("Failed to parse {} line, see regex" .format(test_str))
            raise e

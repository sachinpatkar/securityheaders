from securityheaders.checkers import Checker, FindingType, Finding, FindingSeverity

class HeaderPresentChecker(Checker):
    def check(self, headers, header, description, options):
        if not header or not headers:
           return []

        if header in headers.keys():
            return [Finding(header, FindingType.INFO_DISCLOSURE, header + ' header present. ' + description,FindingSeverity.INFO, header, headers[header])]
        return []  
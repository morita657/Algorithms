from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        catalog = defaultdict(int)
        for i in range(len(cpdomains)):
            domainData = cpdomains[i].split()
            num, domain = int(domainData[0]), domainData[1]
            splittedDomain = domain.split(".")[::-1]
            name = ""
            for j in range(len(splittedDomain)):
                name = splittedDomain[j] + '.' + name
                if name[:-1] in catalog.keys():
                    catalog[name[:-1]].append(num)
                else:
                    catalog[name[:-1]] = [num]
        output = []
        keyList = catalog.keys()
        # print catalog
        for key in range(len(keyList)):
            # print catalog[keyList[key]], sum(catalog[keyList[key]])
            data = "%s %s" % (sum(catalog[keyList[key]]), keyList[key])
            output.append(data)
        return output

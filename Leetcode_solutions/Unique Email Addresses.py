class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sentTo = []
        for email in range(len(emails)):
            mail = emails[email].split("@")
            local = mail[0]
            domain = mail[1]
            local = local.replace(".", "")
            for ch in range(len(local)):
                if local[ch] == "+":
                    local = local[:ch]
                    break
            mail = local + "@" + domain
            sentTo.append(mail)
        return len(list(set(sentTo)))

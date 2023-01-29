def num_unique_emails(emails):
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0]
        local = local.replace('.', '')
        email = local + '@' + domain
        unique_emails.add(email)

    return len(unique_emails)


print(
    num_unique_emails([
        "test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    ]))

print(num_unique_emails(["a@leetcode.com", "b@leetcode.com",
                         "c@leetcode.com"]))

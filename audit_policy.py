import re
import sys

#'01FA070000000000000000000000000000000000000000000000000001000000000000000000000009000000'
#'010100000900187778000000010000000300000003000100010001000000010000000000000003000000000000000000000000000000000000000000000000000000000000000000000000000000010001000000000000000000010000000100000000000000000000000000000000000000000000000000050009000C00030004000600060004000400'



def audit_policy(audit_string):

    policies = {'Auditing': 1, 'Restart, Successes, and Failures': 9, 'Logons and Logoffs': 17,
                'File and Object Access': 25, 'Use of User Rights': 33, 'Process Tracking': 41,
                'Securiy Policy Management': 49, 'User and Group Management': 57,
                'Active Directory Service Access': 65, 'Domain Account Logon': 73}

    if not int(audit_string[policies['Auditing']]):
        print '--- Auditing is disabled ---'
    else:
        print '+++ Auditing is enabled +++'
        for policy in policies:
            if int(audit_string[policies[policy]]) and policy != 'Auditing':
                print policy, 'is enabled.'

if __name__ == '__main__':
    to_audit = None
    
    try:
        to_audit = sys.argv[1]
    except IndexError:
        print 'Usage: {} [audit string]'
        raise SystemExit

    if to_audit:
        if not re.match("\w+", to_audit):
            print 'Edit your string to eliminate spaces, then retry.'
            raise SystemExit
        else:
            audit_policy(to_audit)

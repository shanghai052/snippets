auditstring = '01FA070000000000000000000000000000000000000000000000000001000000000000000000000009000000'
auditstring2 = '000100000900187778000000010000000300000003000100010001000000010000000000000003000000000000000000000000000000000000000000000000000000000000000000000000000000010001000000000000000000010000000100000000000000000000000000000000000000000000000000050009000C00030004000600060004000400'
others = '010400000000000515000000242B96FF40F56C187871A33A'

def audit_policy(audit_string):
	'''
	Parse through a windows registry key:
		HKLM\Security\Policy\PolAcDmS\ 
	and return what policies are in place, if any.
	
	@param audit_string: string stored in windows registry
	'''
	
	policies = {'Auditing': 1, 'Restart, Successes, and Failures': 9, 'Logons and Logoffs': 17, 
				'File and Object Access': 25, 'Use of User Rights': 33, 'Process Tracking': 41, 
				'Securiy Policy Management': 49, 'User and Group Management': 57, 
				'Active Directory Service Access': 65, 'Domain Account Logon': 73}
	
	if int(audit_string[policies['Auditing']]) == 0:
		print '--- Auditing is disabled ---'
	else:
		print '+++ Auditing is enabled +++'
		for policy in policies:
			if int(audit_string[policies[policy]]) != 0 and policy != 'Auditing':
				print policy, 'is enabled.'



audit_policy(auditstring)
audit_policy(auditstring2)

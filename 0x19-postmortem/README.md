##  Issue Summary

During the afternoon hours of 5:45 PM to 8:30 PM TOC, an error 500 is presented within the AAA RADIUS authentication servers, causing users who were using the network, could not log in to the LDAP active directory server, the problem affected 70% of users because all users were not using this authentication system. The main cause of this service interruption was an invalid configuration change within the configuration of this server (/etc/freeradius/3.0/radius.conf).

## Timeline (all times Colombia Time)

- 5:45 PM: The alert was detected in the monitoring system
- 6:00 PM: Technicians are alerted
- 6:30 PM: Users began to disconnect
- 7:00 PM: 70% of users disconnected
- 7:15 PM: Roolback configuration file
- 7:30 PM: 100% of users are connected

## Root Cause

At 5:40 PM a network administrator inadvertently accessed the main server to make some optimization changes to the server, edited the /etc/freeradius/3.0/radius configuration files.conf without making a backup of this file first, due to company policies, all services are restarted by means of a script every day at 5:45 PM at this point the authentications of the users started to fail and the failure was detected in our monitoring systems, by 7:00 PM all users would have been de-authenticated

## Resolution and recovery

At 6:00 PM the engineering team was called to investigate the case, at 6:15 PM they entered the server to investigate which was the affected file or which was causing the problems in the AAA server, at 6:40 PM they found the configuration line which was affecting the problem in the server, at 7:15 PM they changed the configuration of the file, they restarted the server and at 7:30 PM they were able to verify the operation of the network, making tests together in each of the affected locations

##  Corrective and Preventative Measures

corrective and preventive measures Over the past two days, we have conducted an internal review and analysis of the disruption. The following are the actions we are taking to address the underlying causes of the problem and help prevent recurrence and improve response times:

- We're implementing a new user group that only has permission on this file
- Password change of the servers every week
- We create a script which creates a directory with the backup of the files

This way we help to facilitate the correction of the services and the continuous learning in the company

This script will monitor that the public to s3 Bucket has been enabled or not.If the public access is enable it will give the 1 as output if public access is diabled then it will give 0 as output.

Below are the step to use this scripts:
1. install the awscli
2. configure awscli with the zabbbix user by running the "aws configure" provide the aws secret and access key
3. if zabbix-agent is installed then move/copy the "userparameter_s3acl.conf" to the the /etc/zabbix/zabbix_agentd.d/ dir
4. Restart the zabbix-agent
5. Go to zabbix UI, then create Items on the host on which we have configure the awscli and zabbix-agent with below item key
    bucket.publicRead[bucketname]
    bucket.publicWrite[bucketname]
 after the set interval time it will start fetching the access.
6. For alert we can set the triggers.


NOTE:Will update and make this easy to configure.


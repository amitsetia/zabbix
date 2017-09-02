nginx

# Template and script to monitor nginx web server.

# Monitoring Items

* Nginx Waiting
* Nginx Writing
* Nginx Requests
* Nginx Reading
* Nginx Active
* Nginx Handled
* Nginx Accepted


#CONFIGURATION:-

1. First we configure nginx so that nginx provide is the details:
       a. Copy the "status.conf" to the "/etc/nginx/sites-enable" directory.
       b. Edit the File and add your ZAbbix IP
       c. Restart the nginx service (service nginx restart/systemctl restart nginx)
  You can test the access to the status site by running this command on the server: curl http://localhost:10061/nginx-status

2. Now we will configure the zabbix-agent:-
       a. copy the "userparameter_nginx.conf" to the "/etc/zabbix/azbbix_agent.d/".
       b. Restart the zabbix-agent service (service zabbix-agentd restart)
3. Download and import the file zbx_export_templates.xml.

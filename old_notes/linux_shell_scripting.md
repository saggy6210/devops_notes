How to check default route and routing table ?
netstat -n

How to check which ports are listening in my Linux Server ?
netstat -listen or lsof -i 

How to print specific line and convert from lowercase to uppercase?
awk 'NR=line-number{print toupper($0)}' filename

Display number of users loggined in to server?
w

How do I print date in different format?

Command: date

DAT=`date +\%y%m%d%H%M%S`

How to check  specific process is up or down?

If you get return value 1 then process is UP, else process is down.
Status=`ps -fu user_name | grep "process_name" | grep -v grep |wc -l`

How to delete specific days old logs/files?

By using this command you can delete number days old log. please use correct files extension that you want to delete and give number of days old log/files ypu want to delete.

find . -type f -name "*.files_extension" -mtime +days  -exec rm -rf {} \;

Example :
To delete more than 20 days old log files use below command.
find . -type f -name "*.log*" -mtime +20  -exec rm -rf {} \;

How to check from since server is up?

You can use below in your script to check current date, server status and server is up from how many days.
Command : uptime
status=`uptime`
current_time=`echo $status | awk '{print $1}' `
up_status=`echo $status | awk '{print $2}'`

up_since=`echo $status | awk '{print $3}'`

How to check ram size of the server?

You can use below in your script to check RAM size of the server.
Command: free -g -t
ram_size=`free -g -t | grep buffer | tail -1`
used_size=`echo $ram_size | awk '{print $3}'`

free_size=`echo $ram_size | awk '{print $4}'`

How to replace content/string of file? 

sed -i "s/source_pattern/target_pattern/g" file
perl -pi -e 's/source_pattern/target_pattern/g' file
  
How to setup password less ssh connectivity? 

1. First create .ssh directory at home by using mkdir .ssh
2. keygen -t rsa <enter>
3. copy public key from .ssh/id_rsa.pub to .ssh/authorized_key
3. try to connect ssh remote_host

How to copy directory or file from remote server?

scp file target_host:directory_path
scp -r dir/ target_host:directory_path

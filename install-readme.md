# Must chmod 755 daemons to start program

sudo chmod 755 /home/pi/Projects/init-sched-daemon.sh
########################################################
# Other Notes
########################################################
# Check status
sudo systemctl status hello.service

# Start service
sudo systemctl start hello.service

# Stop service
sudo systemctl stop hello.service

# Check service's log
sudo journalctl -f -u hello.service


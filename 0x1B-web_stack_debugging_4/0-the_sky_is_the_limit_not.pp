# to increase the amount of Traffic the Nginx server can Handle.

# increase the ULIMIT of the default file
exec { 'fix--for--nginx':
  # Modify tghe ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx'
  # specify the path for the sed command
  path	=> '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  #Specify path for the init.d script
  path 	=> '/etc/init.d/',
}

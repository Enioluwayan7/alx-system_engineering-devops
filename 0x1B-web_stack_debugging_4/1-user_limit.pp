# Enable the user Holberton to login and open file without error

# Increase hard file limit for Holberton users.
exec { 'increase-hard-file-limit-for-holberton-user':
  command  => "sed -i '/holberton hard/s/4/50000/' /etc/security/limits.conf",
  path	=> '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton users.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path	=> '/usr/local/bin/:/bin/'
}

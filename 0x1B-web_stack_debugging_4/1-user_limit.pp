# Enable user holberton to login and open file without error.

# Increase hard file limits for holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limits for holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i "/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

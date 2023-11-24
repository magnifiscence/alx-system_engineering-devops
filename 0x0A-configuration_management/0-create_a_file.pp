#Creates a file with the content "I love puppet" in /tmp/school
file { '/tmp/school':
  ensure  => 'file',
  content => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

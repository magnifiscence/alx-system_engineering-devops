# Installing Flask on Ubuntu 20.04
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

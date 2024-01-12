# Requirements:
# Your SSH client configuration must be configured
# to use the private key ~/.ssh/school
# Your SSH client configuration must be configured
# to refuse to authenticate using a password

exec { '/etc/ssh/ssh_config':
  command  => 'sudo sed -i "s/PasswordAuthentication yes/PasswordAuthentication no\n\tIdentityFile ~\/.ssh\/school/" /etc/ssh/ssh_config',
  provider => shell
}

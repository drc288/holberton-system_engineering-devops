# Update the password authentication for not
file_line {
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}
# Add the key
file_line {
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton'
}

#  install and configure an Nginx server using Puppet instead of Bash
# Requirements:
#	Nginx should be listening on port 80
#	When querying Nginx at its root / with a GET request
#	(requesting a page) using curl, it must return a page that
#	contains the string Hello World!
#	The redirection must be a “301 Moved Permanently”
#	Your answer file should be a Puppet manifest containing commands
#	to automatically configure an Ubuntu machine to
#	respect above requirements
exec {'update packages':
  command  => 'sudo apt-get update',
  provider => shell
}

package { 'nginx':
  ensure     => 'installed',
}

file {'/usr/share/nginx/html/index.html':
  path    => '/usr/share/nginx/html/index.html',
  content => 'Hello World!'
}

file {'/var/www/html/custom_404.html':
  content => "Ceci n'est pas une page"
}

exec {'configure nginx':
  command  => 'sudo sed -i "30i \\\tlocation /redirect_me {\n\t\treturn 301 https://intranet.alxswe.com;\n\t}\n" /etc/nginx/sites-available/default',
  provider => shell
}

exec {'nginx restart':
  command  => 'sudo service nginx restart',
  provider => shell
}

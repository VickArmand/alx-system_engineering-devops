# creating a custom HTTP header response, on a web server with Puppet.
exec {'update packages':
  command  => 'sudo apt-get update',
  provider => shell
}

package { 'nginx':
  ensure  => 'installed',
}

file {'/usr/share/nginx/html/index.html':
  content => 'Hello World!',
  path    => '/usr/share/nginx/html/index.html'
}

file {'/var/www/html/custom_404.html':
  content => "Ceci n'est pas une page",
  path    => '/var/www/html/custom_404.html'
}

exec {'nginx configuration':
  command  => 'sudo sed -i -E "s/^[^#]+location \/ \{/\\\terror_page 404 \/custom_404.html;\n\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/intranet.alxswe.com;/" /etc/nginx/sites-available/default',
  provider => shell
}

exec {'nginx configuration 2':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i -E "s/^server \{/server {\n\tadd_header X-Served-By $HOST;/" /etc/nginx/sites-available/default'
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell
}

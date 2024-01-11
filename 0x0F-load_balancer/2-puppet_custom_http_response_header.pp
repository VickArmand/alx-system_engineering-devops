# creating a custom HTTP header response, on a web server with Puppet.
exec {
  command  => 'sudo apt-get update -y'
  provider => 'shell'
}

exec {
  command => 'sudo apt-get install nginx -y'
  provider => 'shell'
}

file {'/usr/share/nginx/html/index.html'
  content => 'Hello World!'
}

file {'/var/www/html/custom_404.html'
  content => "Ceci n'est pas une page"
}

exec {
  command => 'sudo sed -i -E "s/^[^#]+location \/ \{/\\\terror_page 404 \/custom_404.html;\n\tlocation \/redirect_me {\n\t\treturn 301 https:\/\/intranet.alxswe.com;/" /etc/nginx/sites-available/default'
  provider => 'shell'
}

exec {
  command => 'sudo sed -i -E "s/^server \{/server {\n\tadd_header X-Served-By $HOST;/" /etc/nginx/sites-available/default'
  provider => 'shell'
}

exec {
  command => 'sudo service nginx restart'
  provider => 'shell'
}

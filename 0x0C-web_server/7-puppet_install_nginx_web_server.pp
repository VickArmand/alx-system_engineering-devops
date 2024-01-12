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
  command  => 'sudo apt-get -y update',
  provider => shell
}

package { 'nginx':
  ensure => 'installed',
}

exec {'/usr/share/nginx/html/index.html':
  command    => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell
}

exec {'/var/www/html/custom_404.html':
  command    => 'echo "Ceci n\'est pas une page" | sudo tee /var/www/html/custom_404.html',
  provider => shell
}

file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}
exec {'nginx restart':
  command  => 'sudo service nginx restart',
  provider => shell
}

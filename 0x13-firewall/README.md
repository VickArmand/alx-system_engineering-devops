<h1>Welcome to the adventures of Firewalls</h1>
<h4>Learning objectives</h4>
<ul>
<li>ufw installation</li>
<li>ufw configuration</li>
<li>Using telnet to check if sockets are open</li>
<li>Port forwarding</li>
</ul>
<h4><center>Warning!</center></h4>
<p>Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.</p>

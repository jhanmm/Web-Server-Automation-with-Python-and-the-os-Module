import os

# 1. Atualização do sistema
os.system("dnf update -y")

# 2. Instalação de dependências
os.system("dnf install -y httpd git")

# 3. Gerenciamento do serviço
os.system("systemctl start httpd")
os.system("systemctl enable httpd")

# Libera o HTTP no firewall
os.system("firewall-cmd --permanent --add-service=http")
os.system("firewall-cmd --reload")

# 4. Deploy da aplicação
os.system("git clone https://github.com/denilsonbonatti/mundo-invertido.git /tmp/mundo-invertido")
os.system("cp -R /tmp/mundo-invertido/* /var/www/html/")
os.system("rm -rf /tmp/mundo-invertido")

# 5. Permissões / SELinux 
os.system("restorecon -R /var/www/html/")
os.system("chmod -R 755 /var/www/html/")
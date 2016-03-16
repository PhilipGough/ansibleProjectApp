#configManagmentProject
This repo consists of two projects on two seperate branches using a similar Flask application

#Ansible
The Ansible(master) branch includes the Playbooks and templates used to deploy a fault tolerant, highly available PostgrSQL cluster, behind an Nginx loadbalancer, two Nginx webservers and uWSGI app servers

#Chef
The Chef repo includes the recipes and files required to deploy the same Flask application with a Mongo database and a HAProxy load balancer

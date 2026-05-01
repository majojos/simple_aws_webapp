# simple_aws_webapp

## Setup

1. Terraform
   terraform init
   terraform apply

2. SSH to EC2
   get the ssh command: python3 get_ssh_connect_commands_ecs2.py
   connect: ssh -i file.pem user@ip

3. install k3s
   curl -sfL https://get.k3s.io | sh -

4. install ArgoCD
   sudo kubectl create namespace argocd
   sudo kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

5. install git
   sudo dnf update -y
   sudo dnf install git -y

6. clone repo
   git clone https://github.com/majojos/simple_aws_webapp.git

7. create argocd app
   sudo kubectl apply -f simple_aws_webapp/argocd/app.yaml

8. ArgoCD UI
   sudo kubectl port-forward svc/argocd-server -n argocd 8080:443


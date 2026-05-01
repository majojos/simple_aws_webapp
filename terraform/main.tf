provider "aws" {
  region = "eu-central-1"
}

resource "aws_security_group" "devops_sg" {
  name = "devops-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "devops" {
  ami           = "ami-0ed094fb1304fd857"
  instance_type = "t3.micro"
  security_groups = [aws_security_group.devops_sg.name]

  tags = {
    Name = "devops-argocd"
  }
}

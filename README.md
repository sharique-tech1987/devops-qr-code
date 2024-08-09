
# QR Code Generator: Powered by FastAPI, Next.js, Kubernetes, and Terraform

## A sample QR Code Generator application built using FastAPI and Next.js, deployed on a Elastic Kubernetes cluster with infrastructure managed by Terraform.

This example project demonstrates a cloud-native app with a Next.js front-end and FastAPI backend, storing QR codes in S3. It automates DevOps by containerizing, deploying via GitHub Actions to EKS, and uses Kubernetes for scalable infrastructure. Terraform provisions AWS resources like VPC and EKS. Thanks to [Rishab](https://github.com/rishabkumar7) for the backend and front-end code. This example demonstrates how to accomplish the following tasks:

* Develop a Next.js front-end application that accepts a URL for QR code generation.
* Implement routing in FastAPI for managing API endpoints.
* Use FastAPI to store the generated QR images in an S3 bucket.
* Automate the containerization and push Docker images to Docker Hub via GitHub Actions.
* Deploy Kubernetes objects such as Deployments, Services, ConfigMaps, Secrets, and Ingress to manage the application.
* Set up automatic deployment to an EKS cluster using GitHub Actions.
* Utilize Terraform to provision a VPC and EKS cluster on AWS.

## How to use this example project

**Note:** This example uses AWS to create infrastructure.









In this guide, we will cover the following:

* Running the api app
* Running the QR generator front-end
* Building and running the project with docker
* Creating infrastructure using Terraform
* Deploying the app on an EKS cluster (coming soon)

### Running the api app
* Setup S3 bucket api keys on aws
* Change the keys in api/app/.env file
* Install venv for python
* Activate the venv
* Install python dependencies

Run the commands to start the api app from the root of the directory
```bash
cd  api
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Running the QR generator front-end
Install node version >= 18. Navigate to front-end-nextjs directory
```bash
cd front-end-nextjs
npm install
npm run dev
```

To test the app
```bash
http://localhost:3000/
```

### Building and running the project with docker
__Note:__ Run these command from the root of the project

To build the api app
```bash
docker build -f ./api/Dockerfile -t devops-qr-code-api:latest .
```

To build the front-end app
```bash
docker build -f ./front-end-nextjs/Dockerfile -t devops-qr-code-front-end:latest .
```

To run the api app
```bash
docker run -p 8000:8000 devops-qr-code-api:latest
```

To run the front-end app
```bash
docker run -p 3000:3000 -d devops-qr-code-front-end
```

To test the app
```bash
http://localhost:3000/
```

### Creating infrastructure using Terraform
* Setup AWS CLI.
* Generate keys on AWS to use with AWS CLI.
* Create S3 bucket to store terraform state and replace the bucket name in the **terraform.tf** file with your bucket.

```bash
 backend "s3" {
    bucket         	   = "[Your-Bucket-Name]"
    key              	   = "state/terraform.tfstate"
    region         	   = "[Your Region]"
  }
```

* Install terraform.
* Install kubectl to interact with EKS cluster.
Run the following commands to create infrastructure.

```bash
cd infra
terraform init
terraform validate
terraform plan
terraform apply
```
Update the kube config file so you can access the EKS cluster
```bash
aws eks update-kubeconfig --name [Your-Cluster-Name] --region [Your-Region]
```

To check you can access the cluster
```bash
kubectl get nodes
```

## Find a bug
If you encounter an issue or have suggestions for improving this project, please submit an issue via the "Issues" tab above.

## Author

[Sharique Ali](https://github.com/sharique-tech1987)


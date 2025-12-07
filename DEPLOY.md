# Deployment Instructions

This guide covers how to push your project to GitHub and deploy it to AWS Elastic Beanstalk (EB) with S3 for static/media files.

## GitHub Repository

**Repository URL**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
_(Replace with your actual GitHub repository URL after creating it)_

## Prerequisites

1.  **Git Installed**: Ensure you have Git installed.
2.  **AWS CLI & EB CLI**: Install the AWS CLI and Elastic Beanstalk CLI (`awsebcli`).
3.  **AWS Account**: You need an active AWS account with access keys.
4.  **S3 Bucket**: You'll need to create an S3 bucket for static and media files.

## 1. Push to GitHub

Initialize the repository and push your code.

```bash
# Initialize Git
git init

# Add all files (excludes ignored files in .gitignore)
git add .

# Commit changes
git commit -m "Initial commit - Ready for deployment"

# Link to your GitHub repository (replace URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to main branch
git push -u origin main
```

## 2. Create S3 Bucket for Static/Media Files

Before deploying to Elastic Beanstalk, create an S3 bucket to store your static and media files.

### Option 1: AWS Console

1. Go to **AWS S3 Console**: https://s3.console.aws.amazon.com/
2. Click **Create bucket**.
3. **Bucket name**: Choose a globally unique name (e.g., `cheatsheets-hub-static-files`).
4. **Region**: Select the same region as your EB environment (e.g., `us-east-1`).
5. **Block Public Access**: Uncheck "Block all public access" (required for static files).
6. Click **Create bucket**.
7. After creation, go to **Permissions** tab -> **Bucket Policy** and add:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
        }
    ]
}
```
_(Replace `YOUR-BUCKET-NAME` with your actual bucket name)_

8. Go to **Permissions** -> **CORS** and add:

```json
[
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET", "HEAD"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
]
```

### Option 2: AWS CLI

```bash
# Create bucket
aws s3 mb s3://cheatsheets-hub-static-files --region us-east-1

# Set public access
aws s3api put-bucket-policy --bucket cheatsheets-hub-static-files --policy file://bucket-policy.json
```

## 3. Deploy to AWS Elastic Beanstalk

### Step A: Initialize EB Application

Run this in your project root:

```bash
eb init -p python-3.9 cheatsheets-hub
```
- It will ask for your region (e.g., `us-east-1` for N. Virginia).
- It may ask if you want to use CodeCommit (say `N`).

### Step B: Create Environment

Create the environment (this provisions EC2 instances, Load Balancer, etc.):

```bash
eb create cheatsheets-env
```
_This process takes about 5-10 minutes._

### Step C: Configure Environment Variables

**CRITICAL**: You must set your secrets in the AWS Console or via CLI.

**Option 1: AWS Console**
1. Go to AWS Elastic Beanstalk Console.
2. Click your environment (`cheatsheets-env`).
3. Go to **Configuration** -> **Software** -> **Edit**.
4. Scroll to **Environment properties** and add:

| Name | Value |
|------|-------|
| `DJANGO_SECRET_KEY` | `your-secure-secret-key-here` |
| `DEBUG` | `False` |
| `USE_S3` | `TRUE` |
| `AWS_ACCESS_KEY_ID` | `your-aws-access-key` |
| `AWS_SECRET_ACCESS_KEY` | `your-aws-secret-access-key` |
| `AWS_STORAGE_BUCKET_NAME` | `your-unique-bucket-name` |

5. Click **Apply**.

**Option 2: CLI**
```bash
eb setenv DJANGO_SECRET_KEY='...' AWS_ACCESS_KEY_ID='...' ...
```

### Step D: Redeploy (if needed)

If you change code or config:

```bash
git add .
git commit -m "Update"
eb deploy
```

## 3. Verify Deployment

1. Run `eb open` to visit your live site.
2. Run `eb status` to see health.
3. Run `eb logs` to debug errors.

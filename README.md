# How to use it


## Provider configuration
```bash
### AWS Environments
export AWS_REGION="us-east-1"
export AWS_ACCESS_KEY_ID="myAccessKeyID"
export AWS_SECRET_ACCESS_KEY="mySecretAccessKeyID"

### Vault Environments
export VAULT_URL="http://127.0.0.1:8200"
export VAULT_TOKEN="badVaultToken"
```

## Call
```bash
### AWS Parameter Store
➜ ~ python getParameter.py "parameter-store" "/teste/duvidei/parameter"

### Vault
➜ ~ python getParameter.py "vault" "/teste/duvidei/patameter"
```

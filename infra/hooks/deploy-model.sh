#!/bin/bash
set -e

echo "🚀 Hook: Ensuring Model Deployment 'gpt-4o-mini' exists..."

if [ -z "$AZURE_AI_ACCOUNT_NAME" ]; then
    echo "❌ Error: AZURE_AI_ACCOUNT_NAME is not set."
    exit 1
fi

if [ -z "$AZURE_RESOURCE_GROUP" ]; then
    echo "❌ Error: AZURE_RESOURCE_GROUP is not set."
    exit 1
fi

az cognitiveservices account deployment create \
  --name "$AZURE_AI_ACCOUNT_NAME" \
  --resource-group "$AZURE_RESOURCE_GROUP" \
  --deployment-name "gpt-4o-mini" \
  --model-name "gpt-4o-mini" \
  --model-version "2024-07-18" \
  --model-format OpenAI \
  --sku-capacity 30 \
  --sku-name "Standard" \
  --output none

echo "✅ Hook: Model Deployment complete."

FROM n8nio/n8n:latest

USER root

RUN if command -v apk >/dev/null 2>&1; then \
      apk add --no-cache python3 py3-pip; \
    elif command -v apt-get >/dev/null 2>&1; then \
      apt-get update && apt-get install -y --no-install-recommends python3 python3-pip && rm -rf /var/lib/apt/lists/*; \
    else \
      echo "No supported package manager found" && exit 1; \
    fi

USER node

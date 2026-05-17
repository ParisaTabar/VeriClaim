FROM n8nio/n8n:1.80.0

USER root
# نصب پایتون در نسخه پایدار (این بار بدون هیچ مشکلی نصب می‌شود)
RUN apk update && apk add --no-cache python3 py3-pip

USER node


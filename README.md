
# Lembra Aí

## Docker Setup

### 1. Environment Variables

Make sure you have a proper `.env` file in the same directory as your `docker-compose.yml`. For example:

### 2. Build the Docker Images

From the project root (where `docker-compose.yml` is located):

```bash
docker-compose build
```

### 3. Run the Containers

```bash
docker-compose up -d
```

This starts:
- A **Postgres** container (db)
- A **Django** container (web) that depends on the db service

### 4. Apply Migrations (Inside Docker)

Once the containers are running, run the migrations inside the **web** container:

```bash
docker-compose exec web python lembra_ai/manage.py migrate
```

### 5. Create a Superuser (Inside Docker)

```bash
docker-compose exec web python lembra_ai/manage.py createsuperuser
```

---

## Ngrok + WhatsApp Webhook Setup

### 1. Install Ngrok

1. Create an account on [ngrok.com](https://ngrok.com/).
2. Download and install ngrok on your system.
3. Authenticate your ngrok client (per ngrok’s setup instructions).

### 2. Start Ngrok on Your Local Port

Assuming your local Django server is running on port **8000**, run:

```bash
ngrok http 8000
```

Ngrok will display something like:

```
Forwarding    https://abc1234.ngrok.io -> http://localhost:8000
```

### 3. Configure WhatsApp Webhook

1. Go to the [Meta for Developers dashboard](https://developers.facebook.com/) for your WhatsApp app.  
2. Under **WhatsApp > Configuration**, find the webhook settings.  
3. Set the **Webhook URL** to your ngrok forwarding address **plus** the path your Django app expects. For example:
   ```
   https://abc1234.ngrok.io/whatsapp/<WHATSAPP_WEBHOOK_PATH>
   ```
4. Set the **Verify Token** to the same value you have in `VERIFY_TOKEN` in your `.env`.
5. Click **Verify and Save** to confirm your webhook.
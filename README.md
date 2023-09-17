# Dialogue Bot

---
Fine-tuned dialog bot based on SOTA model from hugging face. 
The model was fine-tuned using an open set of telegram dialogs. <br />
<br>The work of the model can be seen here: https://huggingface.co/DiTy/dialogpt?text=Hi+dude

## Setup

---
```
>> git clone https://github.com/dtischencko/dialo_bot.git
>> cd dialo_bot
>> echo -e "BOT_TOKEN=YOUR_TOKEN\nMODEL_IP=127.0.0.1\nMODEL_PORT=YOUR_CONTAINER_PORT" > bot/.env
>> docker-compose up -d
```


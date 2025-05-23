import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Defining Gemini 1.5 Flash and Pro models
flash_model = "gemini-1.5-flash"  # Gemini 1.5 Flash model
pro_model = "gemini-1.5-pro"      # Gemini 1.5 Pro model

# Defining input and output costs for the Flash model in dollars
flash_input_cost = 0.075
flash_output_cost = 0.3

# Defining input and output costs for the Pro model in dollars
pro_input_cost = 3.5
pro_output_cost = 10.5


########## FLASH ##########

# Token counter for Gemini 1.5 Flash models
flash_model_full = genai.get_model(f"models/{flash_model}")
flash_limits = {
    "input_tokens": flash_model_full.input_token_limit,
    "output_tokens": flash_model_full.output_token_limit,
}
print(f"\nFlash model limits: {flash_limits}")

# Token counter for the Flash model
llm_flash = genai.GenerativeModel(model_name=flash_model)

flash_token_count = llm_flash.count_tokens("What is a `calça de shopping`?")
print(f"\nToken count: {flash_token_count}")

flash_response = llm_flash.generate_content("What is a `calça de shopping`?")
flash_prompt_tokens = flash_response.usage_metadata.prompt_token_count
flash_response_tokens = flash_response.usage_metadata.candidates_token_count

total_cost = (flash_prompt_tokens * flash_input_cost) / 1000000 + (flash_response_tokens * flash_output_cost) / 1000000
print(f"\nTotal cost: {total_cost} USD")


########### PRO ##########

# Token counter for Gemini 1.5 Pro models
pro_model_full = genai.get_model(f"models/{pro_model}")
pro_limits = {
    "input_tokens": pro_model_full.input_token_limit,
    "output_tokens": pro_model_full.output_token_limit,
}
print(f"\nPro model limits: {pro_limits}")

llm_pro = genai.GenerativeModel(model_name=pro_model)

pro_token_count = llm_pro.count_tokens("What is a shopping pants?")
print(f"\nToken count: {pro_token_count}")

pro_response = llm_pro.generate_content("What is a shopping pants?")
pro_prompt_tokens = pro_response.usage_metadata.prompt_token_count
pro_response_tokens = pro_response.usage_metadata.candidates_token_count

total_cost = (pro_prompt_tokens * pro_input_cost) / 1000000 + (pro_response_tokens * pro_output_cost) / 1000000
print(f"\nTotal cost: {total_cost} USD")
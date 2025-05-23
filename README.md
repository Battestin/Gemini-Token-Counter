# Token Counter

Python script to count tokens and estimate usage costs for Google Gemini 1.5 Flash and Pro models.  
Measures token limits, counts tokens for sample prompts, and calculates approximate costs based on input/output token pricing.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:  
   ```
   GEMINI_API_KEY=your_google_api_key_here
   ```

4. Run the script:  
   ```bash
   python token_counter.py
   ```

## 🧠 What it Does

- Retrieves token limits for Flash and Pro Gemini models  
- Counts tokens for example prompts  
- Calculates estimated cost of usage based on token pricing

## ⚠️ Notes

- Costs are approximations based on provided input/output token prices  
- Useful for budgeting and monitoring API usage before production

## 📄 License

MIT

import sys
from google import genai
from google.genai import types


GEMINI_API_KEY = "AIzaSyBYxT5KY-E_UgDlfS6BSkM_dIXTEBLAW7I"

def run_chat_bot():

    try:
       
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        print("Please check the API key or your network connection.")
        sys.exit(1)

  
    model_name = "gemini-2.5-flash"
    
   
    system_prompt = "You are Krishinetra, a helpful and knowledgeable agricultural assistant. Answer questions concisely based on farm practices, schemes, or crop diseases."

    
    chat = client.chats.create(
        model=model_name,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

    print(" Krishinetra bot: Hello! I'm your assistant. How can I help with your farming questions? (Type 'exit' to end)")
    print("-" * 70)
    
    # 

  
    while True:
        try:
            user_input = input(" You: ")
        except EOFError:
            break
        
        if user_input.lower() in ["quit", "exit"]:
            print("\n Krishinetra: Goodbye! Happy farming.")
            break

        if not user_input.strip():
            continue

        try:
            
            response = chat.send_message(user_input)
            print(f" Krishinetra: {response.text}")
        
        except Exception as e:
            print(f"An error occurred during message sending: {e}")
            break

if __name__ == "__main__":
    print("Starting Krishinetra Chatbot...")
    run_chat_bot()
    print("\nExiting the chatbot. Goodbye!")
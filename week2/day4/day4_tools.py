import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv
import gradio as gr
from google import genai
from google.genai import types

# 1. Environment and Workspace Setup
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

# Initialize the Google Client
client = genai.Client()
DB_FILE = "prices.db"

# 2. Database Initialization (SQLite)
def init_db():
    """Creates a local relational database and populates mock prices."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            city TEXT PRIMARY KEY,
            price REAL
        )
    """)
    # Seed data
    mock_data = [("london", 799.0), ("paris", 850.0), ("berlin", 499.0), ("tokyo", 1420.0)]
    cursor.executemany("INSERT OR REPLACE INTO prices VALUES (?, ?)", mock_data)
    conn.commit()
    conn.close()

# Initialize the DB right away
init_db()

# 3. Define the Python Tool Function
def get_ticket_price(destination_city: str) -> str:
    """
    Gets the current return ticket price for a specific destination city.
    
    Args:
        destination_city: The name of the city the customer wants to travel to.
    """
    print(f"⚙️ [LOCAL TOOL CALL] Querying database for city: {destination_city}")
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM prices WHERE city = ?", (destination_city.lower().strip(),))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return f"The price of a return ticket to {destination_city.title()} is ${row[0]}."
    return f"No price data available for the city: {destination_city}."


# 4. Core Chat Handler (The Agentic Loop)
def chat_callback(message: str, history: list):
    model_name = "gemini-2.5-flash"
    
    # Re-assemble conversation history logs safely
    formatted_contents = []
    for turn in history:
        role = "user" if turn["role"] == "user" else "model"
        raw_content = turn["content"]
        clean_text = " ".join([item["text"] for item in raw_content if "text" in item]) if isinstance(raw_content, list) else str(raw_content)
        formatted_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=clean_text)]))
        
    # Append the new current question
    formatted_contents.append(types.Content(role="user", parts=[types.Part.from_text(text=str(message))]))
    
    # Configure the system boundaries and pass the python function direct as a tool
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful assistant for Mighty Light Airlines. Give short, courteous answers.",
        temperature=0.0, # Low temperature ensures strict, accurate tool selections
        tools=[get_ticket_price] # Pass the function signature directly!
    )
    
    # Request generation from Gemini
    response = client.models.generate_content(
        model=model_name,
        contents=formatted_contents,
        config=config
    )
    
    # Process potential Tool Calls using a while/if evaluation loop
    if response.function_calls:
        for function_call in response.function_calls:
            # Check if Gemini requested our specific tool
            if function_call.name == "get_ticket_price":
                # Extract args predicted by the model
                args = function_call.args
                city_arg = args.get("destination_city")
                
                # Run the actual local Python function
                tool_result = get_ticket_price(destination_city=city_arg)
                
                # Append the function call execution history back to the chat timeline
                formatted_contents.append(response.candidates[0].content)
                
                # Append the tool's return answer so Gemini can read the result
                formatted_contents.append(
                    types.Content(
                        role="tool",
                        parts=[types.Part.from_function_response(
                            name="get_ticket_price",
                            response={"result": tool_result}
                        )]
                    )
                )
                
                # Call Gemini a SECOND time with the new database facts injected
                final_response = client.models.generate_content(
                    model=model_name,
                    contents=formatted_contents,
                    config=config
                )
                return final_response.text

    return response.text

# 5. Launch UI
demo = gr.ChatInterface(
    fn=chat_callback,
    title="✈️ Week 2 Day 4: Airline AI Agent with SQL Tools",
    description="Ask about ticket prices to London, Paris, or Tokyo to trigger live database tool calls!"
)

if __name__ == "__main__":
    demo.launch()
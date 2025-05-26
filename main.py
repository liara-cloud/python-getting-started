from openai import OpenAI
import json
import requests
from dotenv import load_dotenv
import os


load_dotenv()
client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("LIARA_API_KEY"),
)


def get_current_weather(location: str, unit: str = "celsius"):
    try:
        # Format unit
        m_unit = "m" if unit == "celsius" else "u"  # m = metric, u = US (fahrenheit)
        
        # API call to wttr.in
        url = f"https://wttr.in/{location}?format=j1"
        response = requests.get(url)
        data = response.json()
        
        current = data["current_condition"][0]
        temperature = current["temp_C"] if unit == "celsius" else current["temp_F"]
        condition = current["weatherDesc"][0]["value"]
        
        return {
            "location": location.title(),
            "temperature": int(temperature),
            "unit": unit,
            "condition": condition
        }
    except Exception as e:
        return {"error": str(e)}


tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and country, e.g. Tehran, Iran",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

messages = [
    {"role": "user", "content": "What's the weather like in Tehran?"}
]

completion = client.chat.completions.create(
  model="openai/gpt-4.1",
  messages=messages,
  tools=tools,
  tool_choice="auto"
)

# Extract arguments proposed by the model
args = json.loads(completion.choices[0].message.tool_calls[0].function.arguments)

# Call real API function
weather = get_current_weather(
    location=args["location"],
    unit=args.get("unit", "celsius")
)

# Output
if "error" in weather:
    print(f"❌ Error fetching weather: {weather['error']}")
else:
    print(f"🌤️ The weather in {weather['location']} is {weather['temperature']}°{weather['unit'][0].upper()} and {weather['condition']}.")

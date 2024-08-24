from openai import OpenAI
from dotenv import load_dotenv
# from migration.extractor import CSVColumnFinder


load_dotenv()
client = OpenAI()

# csvExtractor = CSVColumnFinder("appliances.csv")
# columns = csvExtractor.get_columns()

tools = {

}
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
print(completion.choices[0].message.content)

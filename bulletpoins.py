from openai import OpenAI

client = OpenAI()
system_prompt = "Du bist ein hilfreicher Assistent für Informatikstudenten. Deine Aufgabe ist es aus dem Text ausführliche Bullet points zu genererieren"

file = open("stocha_2_3.txt", "r")


def generate_bulletpoints(temperature, system_prompt, file):
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": file
            }
        ]
    )
    return response.choices[0].message.content


bullet_text = generate_bulletpoints(0, system_prompt, file.read())
print(bullet_text)
bullet = open("bullet2.txt", "w")
bullet.write(bullet_text)


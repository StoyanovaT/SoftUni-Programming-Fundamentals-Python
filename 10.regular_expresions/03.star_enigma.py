import re
attacked_planets = []
destroyed_planets = []

num_messages = int(input())

for _ in range(num_messages):
    working_message = ""
    text = input()
    regex = r"[S,s,T,t,A,a,R,r]"
    matches = re.findall(regex, text)
    decrease_num = int(len(matches))

    for i in text:
        working_message += chr(ord(i) - decrease_num)
    regex_commands = r"([^@\-!:>]+)?@(?P<planet>[A-Za-z]+)([^@\-!:>]+)?:([0-9]+)([^@\-!:>]+)?!(?P<attack>[A,D])!([^@\-!:>]+)?->([0-9]+)([^@\-!:>]+)?"
    planets_info = re.finditer(regex_commands, working_message)

    for match in planets_info:
        planet = match.group("planet")
        attack_type = match.group("attack")
        if attack_type == "A":
            attacked_planets.append(planet)
        elif attack_type == "D":
            destroyed_planets.append(planet)

attacked_planets.sort()
destroyed_planets.sort()
print(f"Attacked planets: {len(attacked_planets)}")
for attacked in attacked_planets:
    print(f"-> {attacked}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed in destroyed_planets:
    print(f"-> {destroyed}")

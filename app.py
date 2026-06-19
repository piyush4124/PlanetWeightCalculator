from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My Python project is live 🚀"

if __name__ == "__main__":
    app.run()
  
print('Number	Planet	Relative Gravity\n1	Mercury	0.38\n2	Venus	0.91\n3	Mars	0.38\n4	Jupiter	2.53\n5	Saturn	1.07\n6	Uranus	0.89\n7	Neptune	1.14')

weight = float(input('\nEnter your weight on Earth: '))
planet = int(input('\nEnter destination planet number: '))

if planet == 1:
  destination_weight = weight * 0.38
elif planet == 2:
  destination_weight = weight * 0.91
elif planet == 3:
  destination_weight = weight * 0.38
elif planet == 4:
  destination_weight = weight *2.53
elif planet == 5:
  destination_weight = weight * 1.07
elif planet == 6:
  destination_weight = weight * 0.89
elif planet == 7:
  destination_weight = weight * 1.14
else:
  print('\nEnter a valid planet number, 1 or 2 or 3 or 4 or 5 or 6 or 7')

print(destination_weight)

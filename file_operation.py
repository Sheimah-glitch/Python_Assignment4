with open("story.txt", "r") as f:
  text = f.read()
  
new_text = text.upper()
with open("new_story.txt","w") as f:
  f.write(new_text)

with open("new_story.txt", "a") as file:
  file.write("\nThen Bunny added a new part of the story!")

filename = input("Enter the filename: ")
try:
  with open(filename, "r") as f:
    text = f.read()
    print("File opened successfully!")
    new_text = text.upper()
    print("I changed your text!")
except FileNotFoundError:
  print("Oops! That file doesn’t exist.")

 
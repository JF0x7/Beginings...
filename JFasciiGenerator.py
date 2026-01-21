# Local ASCII art bank
ascii_bank = {

    "baby": r"""

              -------- 
             / -   -  \
            |  .-. .- |
            |  \o| |o (
            \     ^    \
             '.  )--'  /
               '-...-'`
""",
    "qtum": r"""
         o-----o-----o
         / \         / \
        o---o QTUM  o---o
         \ /         \ /
          o-----o-----o
           \         / \
            o-------o   o
""",
    "bird": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠋⠙⢿⣿⣦⣄⡀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣤⣤⣾⣿⡿⠟⠉
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⢤⣤⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀
⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠙⠻⠿⠿⣿⣿⣿⣿⣿⣯⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠛⠛⠻⢿⡿⠁⠀⠀⠀⠀⠀
""",
    "cat": """
 /\\_/\\  
 ( o.o ) 
  > ^ <  
""",
    "dog": """
  / \\__
 (    @\\___
 /         O
/   (_____/
\\_____/ U
""",
    "skull": r"""
      ______
   .-'      '-.
  /            \\
 |              |
 |,  .-.  .-.  ,|
 | )(_o/  \o_)( |
 |/     /\     \|
 (_     ^^     _)
  \__|IIIIII|__/
   | \IIIIII/ |
   \          /
    `--------`
""",
    "car": r"""
        ______
       /|_||_\\`.__
      (   _    _ _\\
      =`-(_)--(_)-'
""",
    "coin": """
     
""",
    "diamond": r"""
    /\    
   /  \   
  / /\ \  
 / /  \ \ 
 \ \  / /
  \ \/ /
   \  /
    \/
""",
    "book": """
     ________
    /     ///
   /     ///
  /_____///
 (______(/
"""
}

# Fetch ASCII art from the bank
def fetch_ascii_art(subject):
    subject = subject.lower()
    return ascii_bank.get(subject, "❌ No ASCII image found for that subject.")

# Main loop
def main():
    print("🐾 ASCII Image Generator — Type 'exit' to quit")
    print("🎯 Try subjects like: baby, skull, bird, car, cat, coin, dog, diamond, book, qtum")
    while True:
        subject = input("\n🧙‍♂️ What image would you like in ASCII? ").strip()
        if subject.lower() == "exit":
            print("👋 Goodbye!")
            break
        print("\n🧙‍♂️ Summoning your ASCII art...\n")
        art = fetch_ascii_art(subject)
        print(art)

if __name__ == "__main__":
    main()

# SN DreamBuild Starter 🌌✨

def music_search():
    song = input("Search for a song: ")
    print(f"🎶 Searching for '{song}'... Just imagine the vibes!")

def chat_random():
    print("💬 Connecting you to a random friend... Hello there!")

def ai_assistant():
    question = input("Ask your AI assistant anything: ")
    print(f"🤖 AI says: 'That’s interesting! Let’s explore {question} together!'")

def main():
    print("Welcome to SN DreamBuild! 🌟")
    while True:
        print("\nWhat do you want to do?")
        print("1. Search Music 🎶")
        print("2. Chat Random 💬")
        print("3. Ask AI 🤖")
        print("4. Exit ❌")
        
        choice = input("Pick 1, 2, 3, or 4: ")
        if choice == "1":
            music_search()
        elif choice == "2":
            chat_random()
        elif choice == "3":
            ai_assistant()
        elif choice == "4":
            print("Bye! Keep building your dreams ✨")
            break
        else:
            print("Oops! Pick a valid option 😅")

# Run the app
main()
💡 What this d

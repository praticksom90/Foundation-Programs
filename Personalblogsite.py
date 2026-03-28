

posts = []

def load_posts():
    try:
        with open("posts.txt", "r") as file:
            data = file.read().split("---\n")
            for post in data:
                if post.strip():
                    lines = post.strip().split("\n")
                    title = lines[0].replace("Title: ", "")
                    content = lines[1].replace("Content: ", "")
                    posts.append({"title": title, "content": content})
    except FileNotFoundError:
        pass

def save_posts():
    with open("posts.txt", "w") as file:
        for post in posts:
            file.write(f"Title: {post['title']}\n")
            file.write(f"Content: {post['content']}\n")
            file.write("---\n")

def create_post():
    title = input("Enter post title: ")
    content = input("Enter post content: ")
    posts.append({"title": title, "content": content})
    save_posts()
    print("✅ Post published!\n")

def view_posts():
    if not posts:
        print("No posts yet.\n")
        return

    for i, post in enumerate(posts, 1):
        print(f"{i}. {post['title']}")
        print(post['content'])
        print("-" * 30)

def edit_post():
    view_posts()
    if not posts:
        return

    choice = int(input("Enter post number to edit: ")) - 1
    if 0 <= choice < len(posts):
        posts[choice]["title"] = input("New title: ")
        posts[choice]["content"] = input("New content: ")
        save_posts()
        print("✏️ Post updated!\n")
    else:
        print("Invalid choice.\n")

def main():
    load_posts()

    while True:
        print("📝 Personal Blog App")
        print("1) Create Post")
        print("2) View Posts")
        print("3) Edit Post")
        print("0) Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            edit_post()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()

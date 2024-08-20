import sqlite3
import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('blog.db')
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        # Create Users Table with Role Column
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT UNIQUE NOT NULL,
                               password TEXT NOT NULL,
                               role TEXT NOT NULL)''')
        # Comment: Stores user information including username, password, and role (Admin, Editor, Author, Subscriber)
        
        # Create Categories Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT UNIQUE NOT NULL)''')
        # Comment: Stores categories for blog posts (e.g., Technology, Lifestyle, etc.)

        # Create Tags Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tags (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT UNIQUE NOT NULL)''')
        # Comment: Stores tags for categorizing blog posts (e.g., Python, Web Development, etc.)

        # Create Posts Table with Category, Tags, and Date
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               title TEXT NOT NULL,
                               content TEXT NOT NULL,
                               author_id INTEGER NOT NULL,
                               category_id INTEGER NOT NULL,
                               date TEXT NOT NULL,
                               FOREIGN KEY (author_id) REFERENCES users(id),
                               FOREIGN KEY (category_id) REFERENCES categories(id))''')
        # Comment: Stores blog posts including title, content, author, category, and publication date

        # Create Post-Tags Relationship Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS post_tags (
                               post_id INTEGER NOT NULL,
                               tag_id INTEGER NOT NULL,
                               FOREIGN KEY (post_id) REFERENCES posts(id),
                               FOREIGN KEY (tag_id) REFERENCES tags(id))''')
        # Comment: Relationship table for associating posts with multiple tags

        # Create Comments Table (No Nested Comments)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               post_id INTEGER NOT NULL,
                               user_id INTEGER NOT NULL,
                               content TEXT NOT NULL,
                               FOREIGN KEY (post_id) REFERENCES posts(id),
                               FOREIGN KEY (user_id) REFERENCES users(id))''')
        # Comment: Stores comments made on posts, including the user who commented and the content

        self.conn.commit()

    def close(self):
        self.conn.close()

    def register_user(self, username, password, role):
        try:
            self.cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                                (username, password, role))
            self.conn.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def login_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        if user:
            return user  # Returns the user tuple (id, username, password, role)
        else:
            print("Invalid username or password.")
            return None

class Post:
    def __init__(self, title, content, author_id, category_id):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.category_id = category_id
        self.date = datetime.date.today().strftime('%Y-%m-%d')

    def create(self, tags=[]):
        db = Database()
        db.cursor.execute("INSERT INTO posts (title, content, author_id, category_id, date) VALUES (?, ?, ?, ?, ?)",
                          (self.title, self.content, self.author_id, self.category_id, self.date))
        post_id = db.cursor.lastrowid
        for tag_id in tags:
            db.cursor.execute("INSERT INTO post_tags (post_id, tag_id) VALUES (?, ?)", (post_id, tag_id))
        db.conn.commit()
        print(f"Post '{self.title}' created successfully.")
        db.close()

    def update(self, post_id):
        db = Database()
        db.cursor.execute("UPDATE posts SET title=?, content=?, category_id=?, date=? WHERE id=? AND author_id=?",
                          (self.title, self.content, self.category_id, self.date, post_id, self.author_id))
        db.conn.commit()
        if db.cursor.rowcount > 0:
            print(f"Post ID {post_id} updated successfully.")
        else:
            print("You can only update your own posts.")
        db.close()

    @staticmethod
    def view_all():
        db = Database()
        db.cursor.execute("SELECT * FROM posts")
        posts = db.cursor.fetchall()
        db.close()
        return posts

    @staticmethod
    def search(keyword):
        db = Database()
        db.cursor.execute("SELECT * FROM posts WHERE title LIKE ? OR content LIKE ?", 
                          ('%' + keyword + '%', '%' + keyword + '%'))
        posts = db.cursor.fetchall()
        db.close()
        return posts

    @staticmethod
    def filter_by_category(category_id):
        db = Database()
        db.cursor.execute("SELECT * FROM posts WHERE category_id=?", (category_id,))
        posts = db.cursor.fetchall()
        db.close()
        return posts

    @staticmethod
    def filter_by_tag(tag_id):
        db = Database()
        db.cursor.execute('''SELECT p.* FROM posts p
                             JOIN post_tags pt ON p.id = pt.post_id
                             WHERE pt.tag_id=?''', (tag_id,))
        posts = db.cursor.fetchall()
        db.close()
        return posts

    @staticmethod
    def filter_by_date(start_date, end_date):
        db = Database()
        db.cursor.execute("SELECT * FROM posts WHERE date BETWEEN ? AND ?", (start_date, end_date))
        posts = db.cursor.fetchall()
        db.close()
        return posts

class Comment:
    def __init__(self, post_id, user_id, content):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    def add(self):
        db = Database()
        db.cursor.execute("INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)",
                          (self.post_id, self.user_id, self.content))
        db.conn.commit()
        print("Comment added successfully.")
        db.close()

    @staticmethod
    def view(post_id):
        db = Database()
        db.cursor.execute("SELECT * FROM comments WHERE post_id=?", (post_id,))
        comments = db.cursor.fetchall()
        db.close()
        return comments

def user_menu(user):
    role = user[3]  # Assuming the role is stored in the 4th column (index 3) of the user tuple
    
    while True:
        print("\n1. Create Post")
        print("2. View Posts")
        print("3. Update Post")
        print("4. Add Comment to Post")
        print("5. View Comments on Post")
        print("6. Search Posts")
        print("7. Filter Posts by Category")
        print("8. Filter Posts by Tag")
        print("9. Filter Posts by Date")
        print("10. Logout")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            if role in ['Admin', 'Editor', 'Author']:
                title = input("Enter post title: ")
                content = input("Enter post content: ")
                category_id = int(input("Enter category ID: "))
                tags = [int(tag) for tag in input("Enter tag IDs (comma-separated): ").split(',')]
                post = Post(title, content, user[0], category_id)
                post.create(tags)
            else:
                print("You do not have permission to create a post.")
        
        elif choice == "2":
            posts = Post.view_all()
            for post in posts:
                print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Author ID: {post[3]}, Date: {post[5]}")
        
        elif choice == "3":
            if role in ['Admin', 'Editor', 'Author']:
                post_id = int(input("Enter post ID to update: "))
                title = input("Enter new title: ")
                content = input("Enter new content: ")
                category_id = int(input("Enter new category ID: "))
                post = Post(title, content, user[0], category_id)
                post.update(post_id)
            else:
                print("You do not have permission to update posts.")
        
        elif choice == "4":
            if role in ['Admin', 'Editor', 'Author', 'Subscriber']:
                post_id = int(input("Enter post ID to comment on: "))
                content = input("Enter comment content: ")
                comment = Comment(post_id, user[0], content)
                comment.add()
            else:
                print("You do not have permission to comment.")
        
        elif choice == "5":
            post_id = int(input("Enter post ID to view comments: "))
            comments = Comment.view(post_id)
            for comment in comments:
                print(f"Comment ID: {comment[0]}, User ID: {comment[2]}, Content: {comment[3]}")
        
        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            posts = Post.search(keyword)
            for post in posts:
                print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Author ID: {post[3]}, Date: {post[5]}")
        
        elif choice == "7":
            category_id = int(input("Enter category ID to filter by: "))
            posts = Post.filter_by_category(category_id)
            for post in posts:
                print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Author ID: {post[3]}, Date: {post[5]}")
        
        elif choice == "8":
            tag_id = int(input("Enter tag ID to filter by: "))
            posts = Post.filter_by_tag(tag_id)
            for post in posts:
                print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Author ID: {post[3]}, Date: {post[5]}")
        
        elif choice == "9":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            posts = Post.filter_by_date(start_date, end_date)
            for post in posts:
                print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Author ID: {post[3]}, Date: {post[5]}")
        
        elif choice == "10":
            break

def main_menu():
    db = Database()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (Admin, Author, Subscriber, Viewer): ")
            db.register_user(username, password, role)
        
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = db.login_user(username, password)
            if user:
                user_menu(user)
        
        elif choice == "3":
            db.close()
            break

if __name__ == "__main__":
    main_menu()



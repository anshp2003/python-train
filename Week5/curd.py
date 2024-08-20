import sqlite3
import hashlib

# Database Class
class Database:
    def __init__(self, db_name="blog_app.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_tables()
 
    def setup_tables(self):
        # Create Users Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT UNIQUE NOT NULL,
                               password TEXT NOT NULL,
                               role TEXT NOT NULL)''')
        # Create Posts Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               title TEXT NOT NULL,
                               content TEXT NOT NULL,
                               author_id INTEGER NOT NULL,
                               category_id INTEGER,
                               tags TEXT,
                               likes INTEGER DEFAULT 0,
                               FOREIGN KEY (author_id) REFERENCES users(id))''')
        # Create Comments Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               post_id INTEGER NOT NULL,
                               user_id INTEGER NOT NULL,
                               content TEXT NOT NULL,
                               parent_id INTEGER,
                               FOREIGN KEY (post_id) REFERENCES posts(id),
                               FOREIGN KEY (user_id) REFERENCES users(id),
                               FOREIGN KEY (parent_id) REFERENCES comments(id))''')
        # Create Categories Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               name TEXT UNIQUE NOT NULL)''')
        # Create Likes Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS likes (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               post_id INTEGER NOT NULL,
                               user_id INTEGER NOT NULL,
                               FOREIGN KEY (post_id) REFERENCES posts(id),
                               FOREIGN KEY (user_id) REFERENCES users(id))''')
        self.conn.commit()
 
    def close(self):
        self.conn.close()
 
# User Class
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = self.hash_password(password)
        self.role = role
 
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
 
    @staticmethod
    def verify_password(stored_password, provided_password):
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()
 
    def register(self):
        db = Database()
        try:
            db.cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                              (self.username, self.password, self.role))
            db.conn.commit()
            print(f"User {self.username} registered successfully.")
        except sqlite3.IntegrityError:
            print(f"Username {self.username} already exists.")
            print("Username already exists.")
        finally:
            db.close()
 
    @staticmethod
    def login(username, password):
        db = Database()
        db.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = db.cursor.fetchone()
        db.close()
        if user and User.verify_password(user[2], password):
            print(f"User {username} logged in successfully.")
            return user
        else:
            print(f"Login failed for user {username}.")
            print("Invalid username or password.")
            return None
 
# Post Class
class Post:
    def __init__(self, title, content, author_id, category_id=None, tags=None):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.category_id = category_id
        self.tags = tags
 
    def create_post(self):
        db = Database()
        try:
            db.cursor.execute("INSERT INTO posts (title, content, author_id, category_id, tags) VALUES (?, ?, ?, ?, ?)",
                              (self.title, self.content, self.author_id, self.category_id, self.tags))
            db.conn.commit()
            print(f"Post '{self.title}' created by user ID {self.author_id}.")
        except Exception as e:
            print(f"Failed to create post: {e}")
        finally:
            db.close()
 
    @staticmethod
    def view_posts():
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM posts")
            posts = db.cursor.fetchall()
            return posts
        except Exception as e:
            print(f"Failed to retrieve posts: {e}")
            return []
        finally:
            db.close()
 
    @staticmethod
    def update_post(post_id, title=None, content=None, category_id=None, tags=None):
        db = Database()
        try:
            if title:
                db.cursor.execute("UPDATE posts SET title=? WHERE id=?", (title, post_id))
            if content:
                db.cursor.execute("UPDATE posts SET content=? WHERE id=?", (content, post_id))
            if category_id:
                db.cursor.execute("UPDATE posts SET category_id=? WHERE id=?", (category_id, post_id))
            if tags:
                db.cursor.execute("UPDATE posts SET tags=? WHERE id=?", (tags, post_id))
            db.conn.commit()
            print(f"Post ID {post_id} updated.")
        except Exception as e:
            print(f"Failed to update post: {e}")
        finally:
            db.close()
 
    @staticmethod
    def delete_post(post_id):
        db = Database()
        try:
            db.cursor.execute("DELETE FROM posts WHERE id=?", (post_id,))
            db.conn.commit()
            print(f"Post ID {post_id} deleted.")
        except Exception as e:
            print(f"Failed to delete post: {e}")
        finally:
            db.close()
 
    @staticmethod
    def like_post(post_id, user_id):
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM likes WHERE post_id=? AND user_id=?", (post_id, user_id))
            like = db.cursor.fetchone()
            if like:
                db.cursor.execute("DELETE FROM likes WHERE id=?", (like[0],))
                db.cursor.execute("UPDATE posts SET likes = likes - 1 WHERE id=?", (post_id,))
                action = "unliked"
            else:
                db.cursor.execute("INSERT INTO likes (post_id, user_id) VALUES (?, ?)", (post_id, user_id))
                db.cursor.execute("UPDATE posts SET likes = likes + 1 WHERE id=?", (post_id,))
                action = "liked"
            db.conn.commit()
            print(f"Post ID {post_id} {action} by user ID {user_id}.")
        except Exception as e:
            print(f"Failed to like/unlike post: {e}")
        finally:
            db.close()
 
# Comment Class
class Comment:
    def __init__(self, post_id, user_id, content, parent_id=None):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.parent_id = parent_id
 
    def add_comment(self):
        db = Database()
        try:
            db.cursor.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (?, ?, ?, ?)",
                              (self.post_id, self.user_id, self.content, self.parent_id))
            db.conn.commit()
            print(f"Comment added by user ID {self.user_id} to post ID {self.post_id}.")
        except Exception as e:
            print(f"Failed to add comment: {e}")
        finally:
            db.close()
 
    @staticmethod
    def view_comments(post_id):
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM comments WHERE post_id=? AND parent_id IS NULL", (post_id,))
            comments = db.cursor.fetchall()
            return comments
        except Exception as e:
            print(f"Failed to retrieve comments: {e}")
            return []
        finally:
            db.close()
 
    @staticmethod
    def view_nested_comments(comment_id):
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM comments WHERE parent_id=?", (comment_id,))
            comments = db.cursor.fetchall()
            return comments
        except Exception as e:
            print(f"Failed to retrieve nested comments: {e}")
            return []
        finally:
            db.close()
 
# Adding this method to the Comment class
Comment.view_comments_with_nested = Comment.view_comments
 
# Category Class
class Category:
    def __init__(self, name):
        self.name = name
 
    def add_category(self):
        db = Database()
        try:
            db.cursor.execute("INSERT INTO categories (name) VALUES (?)", (self.name,))
            db.conn.commit()
            print(f"Category '{self.name}' added.")
        except Exception as e:
            print(f"Failed to add category: {e}")
        finally:
            db.close()
 
    @staticmethod
    def view_categories():
        db = Database()
        try:
            db.cursor.execute("SELECT * FROM categories")
            categories = db.cursor.fetchall()
            return categories
        except Exception as e:
            print(f"Failed to retrieve categories: {e}")
            return []
        finally:
            db.close()
 
    @staticmethod
    def update_category(category_id, name):
        db = Database()
        try:
            db.cursor.execute("UPDATE categories SET name=? WHERE id=?", (name, category_id))
            db.conn.commit()
            print(f"Category ID {category_id} updated to {name}.")
        except Exception as e:
            print(f"Failed to update category: {e}")
        finally:
            db.close()
 
    @staticmethod
    def delete_category(category_id):
        db = Database()
        try:
            db.cursor.execute("DELETE FROM categories WHERE id=?", (category_id,))
            db.conn.commit()
            print(f"Category ID {category_id} deleted.")
        except Exception as e:
            print(f"Failed to delete category: {e}")
        finally:
            db.close()
 
# AccessControl Class
class AccessControl:
    @staticmethod
    def has_permission(user, permission):
        role_permissions = {
            'admin': ['create_post', 'edit_post', 'delete_post', 'create_category', 'edit_category', 'delete_category'],
            'editor': ['create_post', 'edit_post', 'delete_post', 'create_category', 'edit_category'],
            'author': ['create_post', 'edit_post'],
            'subscriber': []
        }
        return permission in role_permissions.get(user[3], [])
 
# Helper Functions
def main_menu(user=None):
    if not user:
        print("Welcome! Please choose an option:")
        print("1. Register")
        print("2. Login")
        choice = input("Enter choice (1/2): ")
 
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/editor/author/subscriber): ").lower()
            user = User(username, password, role)
            user.register()
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User.login(username, password)
            if user:
                main_menu(user)
    else:
        while True:
            print(f"Welcome {user[1]}! You are logged in as a {user[3]}.")
            print("1. View Posts")
            if AccessControl.has_permission(user, 'create_post'):
                print("2. Create Post")
            if AccessControl.has_permission(user, 'edit_post'):
                print("3. Edit Post")
            if AccessControl.has_permission(user, 'delete_post'):
                print("4. Delete Post")
            if AccessControl.has_permission(user, 'create_category'):
                print("5. Create Category")
            if AccessControl.has_permission(user, 'edit_category'):
                print("6. Edit Category")
            if AccessControl.has_permission(user, 'delete_category'):
                print("7. Delete Category")
            print("8. Search and Filter Posts")
            print("9. Like/Unlike Post")
            print("10. Comment on Post")
            print("11. Logout")
 
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    view_posts(user)
                elif choice == 2 and AccessControl.has_permission(user, 'create_post'):
                    manage_posts(user)
                elif choice == 3 and AccessControl.has_permission(user, 'edit_post'):
                    manage_posts(user, edit=True)
                elif choice == 4 and AccessControl.has_permission(user, 'delete_post'):
                    manage_posts(user, delete=True)
                elif choice == 5 and AccessControl.has_permission(user, 'create_category'):
                    manage_categories()
                elif choice == 6 and AccessControl.has_permission(user, 'edit_category'):
                    manage_categories(edit=True)
                elif choice == 7 and AccessControl.has_permission(user, 'delete_category'):
                    manage_categories(delete=True)
                elif choice == 8:
                    search_and_filter()
                elif choice == 9:
                    like_unlike_post(user)
                elif choice == 10:
                    comment_on_post(user)
                elif choice == 11:
                    break
                else:
                    print("Invalid choice or insufficient permissions.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("An error occurred. Please try again.")
def print_comments_with_nested(comments, level=0):
    for comment in comments:
        print("  " * level + f"Comment ID: {comment[0]}")
        print("  " * level + f"User ID: {comment[2]}")
        print("  " * level + f"Content: {comment[3]}")
        nested_comments = Comment.view_nested_comments(comment[0])
        if nested_comments:
            print("  " * level + "Replies:")
            print_comments_with_nested(nested_comments, level + 1)
 
def view_posts(user):
    posts = Post.view_posts()
    for post in posts:
        print("="*50)
        print(f"Post ID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Content: {post[2]}")
        print(f"Author ID: {post[3]}")
        print(f"Category ID: {post[4]}")
        print(f"Tags: {post[5]}")
        print(f"Likes: {post[6]}")
       
        if Post.has_liked(post[0], user[0]):
            print("Status: You have liked this post. (Unlike)")
        else:
            print("Status: You have not liked this post. (Like)")
 
        print("-"*50)
        comments = Comment.view_comments(post[0])
        if comments:
            print("Comments:")
            print_comments_with_nested(comments)
        else:
            print("No comments yet.")
        print("="*50)
        print()
 
def like_unlike_post(user):
    post_id = int(input("Enter post ID to like/unlike: "))
    if Post.has_liked(post_id, user[0]):
        Post.unlike_post(post_id, user[0])
        print(f"Unliked post ID {post_id}.")
    else:
        Post.like_post(post_id, user[0])
        print(f"Liked post ID {post_id}.")
 
def comment_on_post(user):
    post_id = int(input("Enter post ID to comment on: "))
    parent_id = input("Enter parent comment ID (optional, leave blank if not a reply): ")
    if parent_id == '':
        parent_id = None
    else:
        parent_id = int(parent_id)
    content = input("Enter your comment: ")
    Comment.add_comment(post_id, user[0], content, parent_id)
    print(f"Commented on post ID {post_id}.")
 
def manage_posts(user, edit=False, delete=False):
    if edit:
        post_id = int(input("Enter post ID to edit: "))
        title = input("Enter new title: ")
        content = input("Enter new content: ")
        category_id = input("Enter new category ID (optional): ")
        category_id = int(category_id) if category_id else None
        tags = input("Enter new tags (optional): ")
        Post.update_post(post_id, title, content, category_id, tags)
        print(f"Post ID {post_id} updated.")
    elif delete:
        post_id = int(input("Enter post ID to delete: "))
        Post.delete_post(post_id)
        print(f"Post ID {post_id} deleted.")
    else:
        title = input("Enter title: ")
        content = input("Enter content: ")
        category_id = input("Enter category ID (optional): ")
        category_id = int(category_id) if category_id else None
        tags = input("Enter tags (optional): ")
        post = Post(title, content, user[0], category_id, tags)
        post.create_post()
        print("Post created.")
 
def manage_categories(edit=False, delete=False):
    if edit:
        category_id = int(input("Enter category ID to edit: "))
        name = input("Enter new name: ")
        Category.update_category(category_id, name)
        print(f"Category ID {category_id} updated to {name}.")
    elif delete:
        category_id = int(input("Enter category ID to delete: "))
        Category.delete_category(category_id)
        print(f"Category ID {category_id} deleted.")
    else:
        name = input("Enter category name: ")
        category = Category(name)
        category.add_category()
        print(f"Category '{name}' created.")
 
def search_and_filter():
    keyword = input("Enter keyword to search: ")
    db = Database()
    try:
        db.cursor.execute("SELECT * FROM posts WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?",
                          (f'%{keyword}%', f'%{keyword}%', f'%{keyword}%'))
        posts = db.cursor.fetchall()
        for post in posts:
            print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Author ID: {post[3]}, Category ID: {post[4]}, Tags: {post[5]}, Likes: {post[6]}")
    except Exception as e:
        print(f"Failed to search posts: {e}")
    finally:
        db.close()
 
# Function to check if a user has liked a post
def has_liked(post_id, user_id):
    db = Database()
    try:
        db.cursor.execute("SELECT * FROM likes WHERE post_id=? AND user_id=?", (post_id, user_id))
        like = db.cursor.fetchone()
        return like is not None
    except Exception as e:
        print(f"Failed to check if post is liked: {e}")
        return False
    finally:
        db.close()
 
# Adding this method to Post class
Post.has_liked = has_liked
 
# Function to unlike a post
def unlike_post(post_id, user_id):
    db = Database()
    try:
        db.cursor.execute("SELECT * FROM likes WHERE post_id=? AND user_id=?", (post_id, user_id))
        like = db.cursor.fetchone()
        if like:
            db.cursor.execute("DELETE FROM likes WHERE id=?", (like[0],))
            db.cursor.execute("UPDATE posts SET likes = likes - 1 WHERE id=?", (post_id,))
            db.conn.commit()
            print(f"Post ID {post_id} unliked by user ID {user_id}.")
        else:
            print(f"Post ID {post_id} was not liked by user ID {user_id}.")
    except Exception as e:
        print(f"Failed to unlike post: {e}")
    finally:
        db.close()
 
# Adding this method to Post class
Post.unlike_post = unlike_post
 
# Function to add a comment
def add_comment(post_id, user_id, content, parent_id=None):
    db = Database()
    try:
        db.cursor.execute("INSERT INTO comments (post_id, user_id, content, parent_id) VALUES (?, ?, ?, ?)",
                          (post_id, user_id, content, parent_id))
        db.conn.commit()
        print(f"Comment added by user ID {user_id} to post ID {post_id}.")
    except Exception as e:
        print(f"Failed to add comment: {e}")
    finally:
        db.close()
 
# Adding this method to Comment class
Comment.add_comment = add_comment
 
if __name__ == "__main__":
    main_menu()
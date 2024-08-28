from django.shortcuts import render
from django.db.models import Count,Avg,Q
from Query.models import BlogPost,Author
total_post= BlogPost.objects.aggregate(total=Count('id'))
print(total_post)

average_comments = BlogPost.objects.aggregate(avg_comments=Avg('comment__id'))
print(average_comments)

blog_posts = BlogPost.objects.annotate(num_comments=Count('comment'))

for post in blog_posts:
    print(f"Post: {post.title}, Number of Comments: {post.num_comment}")


filtered_posts = BlogPost.objects.filter(
    Q(title__icontains='Django') & (Q(author__name='Alice') | Q(author__name='Bob'))
)

for post in filtered_posts:
    print(f"Title: {post.title}, Author: {post.author}")


django_posts = BlogPost.objects.filter(Q(title__icontains='Django'))
for post in django_posts:
    print(f"Title: {post.title}, Author: {post.author}")


posts_with_many_comments = BlogPost.objects.annotate(num_comments=Count('comment')).filter(num_comments__gt=1)

for post in posts_with_many_comments:
    print(f"Post: {post.title} has {post.num_comments} comments")

# Example: Selecting blog posts with their authors using select_related
blog_posts = BlogPost.objects.select_related('author').all()
for post in blog_posts:
    print(f"Title: {post.title}, Author: {post.author.name}")


# Example: Prefetch comments related to each blog post
blog_posts = BlogPost.objects.prefetch_related('comment_set').all()
for post in blog_posts:
    print(f"Title: {post.title}, Comments: {post.comment_set.count()}")

import random
import datetime
from uuid import uuid4

from KanJanBlog.models import db, User, Tag, Post

user = User(id=str(uuid4()), username='KanJan', password='ADDR66')
db.session.add(user)
db.session.commit()

user = db.session.query(User).first()
tag_one = Tag(id=str(uuid4()), name='PHP')
tag_two = Tag(id=str(uuid4()), name='C')
tag_three = Tag(id=str(uuid4()), name='JavaScript')
tag_four = Tag(id=str(uuid4()), name='SQLALchemy')
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = "EXAMPLE TEXT"

for i in range(100):
    new_post = Post(id=str(uuid4()), title='Post' + str(i))
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = s
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()

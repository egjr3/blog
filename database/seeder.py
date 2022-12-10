import sqlite3 as sql


def create_db():
    conn = sql.connect('blog.db')
    conn.commit()
    conn.close()


def create_table():
    conn = sql.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE Posts (
            title text,
            subtitle text,
            content text
        )"""
    )
    conn.commit()
    conn.close()


def insert_row(title, subtitle, content):
    conn = sql.connect("blog.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO Posts VALUES ('{title}', '{subtitle}', '{content}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def delete_rows(field, value):
    conn = sql.connect("blog.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM Posts WHERE {field} = '{value}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def delete_all_rows():
    conn = sql.connect("blog.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM Posts"
    cursor.execute(instruction)
    conn.commit()
    conn.close()


def read_rows():
    conn = sql.connect("blog.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM Posts"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    print(data)


if __name__ == '__main__':
    # create_db()
    # create_table()
    delete_all_rows()
    insert_row(
        'I got accepted into BLACKWELL ACADEMY!',
        'July 10',
        'If words could dance this would be a rave. Even though I''ve never been to one. But who cares because I GOT INTO BLACKWELL ACADEMY! I didn''t think I would be so excited since it''s not like I didn''t used to live in the same town. But when I saw the text from the Blackwell scholarship office, I could literally feel my pulse speed up. \n\r\n\r I thought it was going to say, "Sorry! Thanks for playing!" It took me a few seconds before I read the whole thing. I guess I wanted to enjoy that last moment of blissful ignorance. And when I saw the first word, "Congratulations..." I think I screamed. \n\r\n\r My mom cried, and my dad laughed. They''re so weird. But they''re happy and this means extra financial support because they don''t have to pay anything to Blackwell. This means new clothes and if I can work it, a new laptop. \n\r\n\r Oh, and I have to keep telling myself in caps that I AM GOING TO BLACKWELL ACADEMY.'
    )
    insert_row(
        'Back to Arcadia Bay',
        'August 18',
        'So this is it. I''m leaving Seattle to go back to Arcadia Bay. Usually people go to the High School closest to home. I suppose I am too, it''s just I haven''t lived there for 5 years. Out of all the best photography programs in the world, I choose to go to the smallest, back in a town I was excited about leaving.\n\r\n\rMaybe I wanted to come back all along, just to see if Chloe and I are still even friends. But I do wish Chloe could have moved with us to Seattle... That city was made for her. When we would play pirates in our rooms and in the woods, it seemed like Seattle was that fabled faraway island of treasure and adventure that we were always seeking. With coffee shops.\n\r\n\rBut Seattle wasn''t like a fable. Au contraire. Now Blackwell Academy seems more exotic to me than any other place in the world. To study photography under Mark Jefferson... SIGH. Insert hearts and flowers. Plus there will be cool diverse students from everywhere. It won''t be like my high school now... I never really found a groove with my classmates. (Or boys...) I''m lucky I have a couple great friends here. But it''s time to ship out.\n\r\n\rSo maybe Arcadia Bay will actually turn out to be the island of treasure and adventure I''ve been looking for...'
    )
    insert_row(
        'A new beginning',
        'August 25',
        'Shit is krazy here. I didn''t realize how much crap I had to pack until I had to pack all my crap. Mom and Dad are gettin'' a little too excited I''m clearing out my room. Tho I caught mom crying when she was packing my shirts. \n\r\n\r That made me want to cry like a little girl. And never leave Seattle. So instead of packing, I feel like burning all my clothes, then just raiding a thrift store to build up a new Max wardrobe over my junior year. Not that I even have an old Max wardrobe. \n\r\n\r Nobody will know me except for Chloe and who knows how different we are now. So I can cut my hair, get a tat and some piercings... Maybe date a cute foreign exchange artiste from Paris or Rome. I can do anything. Unless I get busted. \n\r\n\r And there will be so many supercool chances for my photography to get exposed! Thinking about that is when I get scared, but excited. And then I don''t feel like crying at all. I get tingles down my arms, sensing the universe opening up for me. I can''t wait to leave. \n\r\n\r I just want things to be... different at Blackwell.'
    )
    read_rows()

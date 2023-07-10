from app.models import db, Review
from datetime import date


def seed_reviews():
    today = date.today()
    review1 = Review(
        user_id=2,
        listing_id=1,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review2 = Review(
        user_id=2,
        listing_id=25,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=2,
        created_at=today,
        updated_at=today,
    )

    review3 = Review(
        user_id=3,
        listing_id=25,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review4 = Review(
        user_id=3,
        listing_id=24,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=2,
        created_at=today,
        updated_at=today,
    )

    review5 = Review(
        user_id=5,
        listing_id=24,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review6 = Review(
        user_id=2,
        listing_id=23,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review7 = Review(
        user_id=4,
        listing_id=23,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review8 = Review(
        user_id=5,
        listing_id=23,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review9 = Review(
        user_id=5,
        listing_id=22,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=3,
        created_at=today,
        updated_at=today,
    )

    review10 = Review(
        user_id=4,
        listing_id=21,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review11 = Review(
        user_id=2,
        listing_id=20,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review12 = Review(
        user_id=3,
        listing_id=19,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review13 = Review(
        user_id=4,
        listing_id=18,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review14 = Review(
        user_id=4,
        listing_id=17,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=3,
        created_at=today,
        updated_at=today,
    )

    review15 = Review(
        user_id=2,
        listing_id=16,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review16 = Review(
        user_id=3,
        listing_id=15,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review17 = Review(
        user_id=5,
        listing_id=14,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=3,
        created_at=today,
        updated_at=today,
    )

    review18 = Review(
        user_id=2,
        listing_id=13,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review19 = Review(
        user_id=3,
        listing_id=12,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=3,
        created_at=today,
        updated_at=today,
    )

    review20 = Review(
        user_id=4,
        listing_id=11,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review21 = Review(
        user_id=4,
        listing_id=10,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review22 = Review(
        user_id=2,
        listing_id=9,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review23 = Review(
        user_id=5,
        listing_id=8,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review24 = Review(
        user_id=3,
        listing_id=7,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review25 = Review(
        user_id=4,
        listing_id=6,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    review26 = Review(
        user_id=2,
        listing_id=5,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=1,
        created_at=today,
        updated_at=today,
    )

    review27 = Review(
        user_id=3,
        listing_id=5,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review28 = Review(
        user_id=5,
        listing_id=4,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review29 = Review(
        user_id=5,
        listing_id=3,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=4,
        created_at=today,
        updated_at=today,
    )

    review30 = Review(
        user_id=5,
        listing_id=3,
        title="It was ok",
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud",
        rating=5,
        created_at=today,
        updated_at=today,
    )

    db.session.add(review1)
    db.session.add(review2)
    db.session.add(review3)
    db.session.add(review4)
    db.session.add(review5)
    db.session.add(review6)
    db.session.add(review7)
    db.session.add(review8)
    db.session.add(review10)
    db.session.add(review11)
    db.session.add(review12)
    db.session.add(review13)
    db.session.add(review14)
    db.session.add(review15)
    db.session.add(review16)
    db.session.add(review17)
    db.session.add(review18)
    db.session.add(review19)
    db.session.add(review20)
    db.session.add(review21)
    db.session.add(review22)
    db.session.add(review23)
    db.session.add(review24)
    db.session.add(review25)
    db.session.add(review26)
    db.session.add(review27)
    db.session.add(review28)
    db.session.add(review29)
    db.session.add(review30)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_reviews():
    db.session.execute("TRUNCATE reviews RESTART IDENTITY CASCADE;")
    db.session.commit()

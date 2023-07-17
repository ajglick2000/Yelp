from app.models import db, Listing, User
from datetime import date


def seed_listings():
    today = date.today()

    user1 = User.query.get(1)
    user2 = User.query.get(2)
    user3 = User.query.get(3)
    user4 = User.query.get(4)
    user5 = User.query.get(5)

    listing1 = Listing(
        user=user1,
        title="Business Listing 1",
        location="Definitely Somewhere",
        category=3,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing2 = Listing(
        user=user2,
        title="Business Listing 2",
        location="Definitely Somewhere",
        category=2,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing3 = Listing(
        user=user3,
        title="Business Listing 3",
        location="Definitely Somewhere",
        category=2,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing4 = Listing(
        user=user4,
        title="Business Listing 4",
        location="Definitely Somewhere",
        category=2,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing5 = Listing(
        user=user5,
        title="Business Listing 5",
        location="Definitely Somewhere",
        category=6,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing6 = Listing(
        user=user1,
        title="Business Listing 6",
        location="Definitely Somewhere",
        category=2,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing7 = Listing(
        user=user2,
        title="Business Listing 7",
        location="Definitely Somewhere",
        category=2,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing8 = Listing(
        user=user3,
        title="Business Listing 8",
        location="Definitely Somewhere",
        category=1,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing9 = Listing(
        user=user4,
        title="Business Listing 9",
        location="Definitely Somewhere",
        category=6,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing10 = Listing(
        user=user5,
        title="Business Listing 10",
        location="Definitely Somewhere",
        category=5,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing11 = Listing(
        user=user1,
        title="Business Listing 11",
        location="Definitely Somewhere",
        category=5,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing12 = Listing(
        user=user2,
        title="Business Listing 12",
        location="Definitely Somewhere",
        category=5,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing13 = Listing(
        user=user3,
        title="Business Listing 13",
        location="Definitely Somewhere",
        category=4,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing14 = Listing(
        user=user4,
        title="Business Listing 14",
        location="Definitely Somewhere",
        category=4,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing15 = Listing(
        user=user5,
        title="Business Listing 15",
        location="Definitely Somewhere",
        category=4,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing16 = Listing(
        user=user1,
        title="Business Listing 16",
        location="Definitely Somewhere",
        category=4,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing17 = Listing(
        user=user2,
        title="Business Listing 17",
        location="Definitely Somewhere",
        category=4,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing18 = Listing(
        user=user3,
        title="Business Listing 18",
        location="Definitely Somewhere",
        category=4,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing19 = Listing(
        user=user4,
        title="Business Listing 19",
        location="Definitely Somewhere",
        category=3,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing20 = Listing(
        user=user5,
        title="Business Listing 20",
        location="Definitely Somewhere",
        category=3,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing21 = Listing(
        user=user1,
        title="Business Listing 21",
        location="Definitely Somewhere",
        category=3,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing22 = Listing(
        user=user2,
        title="Business Listing 22",
        location="Definitely Somewhere",
        category=1,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing23 = Listing(
        user=user3,
        title="Business Listing 23",
        location="Definitely Somewhere",
        category=2,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing24 = Listing(
        user=user4,
        title="Business Listing 24",
        location="Definitely Somewhere",
        category=1,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    listing25 = Listing(
        user=user5,
        title="Business Listing 25",
        location="Definitely Somewhere",
        category=5,
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        image_url="https://s3-media0.fl.yelpcdn.com/bphoto/QvzMTNnm4w-wU6ZhuyBHww/348s.jpg",
        created_at=today,
        updated_at=today,
    )

    db.session.add(listing1)
    db.session.add(listing2)
    db.session.add(listing3)
    db.session.add(listing4)
    db.session.add(listing5)
    db.session.add(listing6)
    db.session.add(listing7)
    db.session.add(listing8)
    db.session.add(listing9)
    db.session.add(listing10)
    db.session.add(listing11)
    db.session.add(listing12)
    db.session.add(listing13)
    db.session.add(listing14)
    db.session.add(listing15)
    db.session.add(listing16)
    db.session.add(listing17)
    db.session.add(listing18)
    db.session.add(listing19)
    db.session.add(listing20)
    db.session.add(listing21)
    db.session.add(listing22)
    db.session.add(listing23)
    db.session.add(listing24)
    db.session.add(listing25)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_listings():
    db.session.execute("TRUNCATE listings RESTART IDENTITY CASCADE;")
    db.session.commit()

import os, random, sys

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from main.models import Items, Inventory


ITEMS_IMAGES_DIR = os.path.join(
    settings.BASE_DIR, "examples", "items"
)
all_images = os.listdir(ITEMS_IMAGES_DIR)
ITEMS_LIST = []

for image_name in all_images:
    image = open(os.path.join(ITEMS_IMAGES_DIR, image_name), "rb")
    image_object = SimpleUploadedFile(image.name, image.read(), content_type="multipart/form-data")
    ITEMS_LIST.append(
        {
            "item_name": image_name.split(".")[0],
            "item_price": random.randint(500, 10000),
            "picture": image_object
        }
    )

class Command(BaseCommand):
    help = "Seeds the database"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Seeding the database, please wait...")
        )
        run(self)


def check_database():
    print("Are you sure to clear the existing development database and reseed it? (Y/N)")
    if settings.DEBUG and input().lower() == "y":
        if sys.version_info[0] < 3:
            os.system("python manage.py flush --no-input")
        else:
            os.system("python3 manage.py flush --no-input")
        return True
    else:
        return False


def create_user(is_admin, username=""):
    """
        Creates a superuser
    """
    email = "%s@example.com" % (username)
    user = User.objects.create_user(
        email=email,
        first_name=username,
        last_name="user",
        username=username,
        password="password",
        is_staff=is_admin,
        is_superuser=is_admin
    )
    print("{} was created with\nusername: {}\npassword: password\n".format(
        "Super user" if is_admin else username.capitalize() + " user", username
    ))
    return user

""" 
    adding all the items in the database 
"""

def create_items():
    for item in ITEMS_LIST:
        Items.objects.create(
            item_name=item["item_name"],
            item_price=item["item_price"],
            picture=item["picture"]
        )

"""
    creating inventory with all the item list
"""

def create_inventories():
    item_list = Items.objects.all()
    for item in item_list:
        inventory, created = Inventory.objects.get_or_create(
            item=item,
            item_count=random.randint(5, 15)
        )

""" 
    main flow will start from here
"""

def run(self):
    status = check_database()
    if status is False:
        print("Seeding aborted.")
        return 0
    print("Seeding...")
    # Create superusers
    create_user(is_admin=True, username="admin1")
    create_user(is_admin=True, username="admin2")
    # Create items tables
    create_items()
    print("Items list has been created.")
    # Create inventory tables
    create_inventories()
    print("Invetories has been created.")
    print("Database successfully seeded.")

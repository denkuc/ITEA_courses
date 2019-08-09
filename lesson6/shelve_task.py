import shelve

db_name = "local.db"


def create_item(key, value):
    with shelve.open(db_name) as db:
        db[key] = value


def get_item(key):
    with shelve.open(db_name) as db:
        try:
            result = db[key]
        except KeyError:
            return None

        return result


def delete_item(key):
    with shelve.open(db_name) as db:
        return db.pop(key, None)


def clear_db():
    with shelve.open(db_name) as db:
        db.clear()


create_item("name", "Den")
create_item("country", "Ukraine")

clear_db()
print(delete_item("name"))
print(get_item("name"), get_item("country"), get_item("day"))
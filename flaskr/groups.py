from flaskr.db import get_db


class Group:
    def __init__(self, user_id, group_id, members=None, name=None):
        self.owner = user_id
        self.ref = group_id

        if members is not None and name is not None:
            self.name = name
            self.members = members
        else:
            db = get_db()
            row = db.execute(
                "SELECT group_name FROM Groups WHERE id = ? AND user_id = ?",
                (group_id, user_id)
            ).fetchone()
            self.name = row['group_name']
            rows = db.execute(
                "SELECT user_id FROM GroupMembers WHERE group_id = ?",
                (group_id,)
            )
            self.members = [row['user_id'] for row in rows]

    def ranking(self):
        db = get_db()
        rows = db.execute("""
        SELECT id, name, score FROM Users
        WHERE id = ? OR id IN (
           SELECT user_id FROM GroupMembers WHERE group_id = ?
        )
        ORDER BY score DESC
        """, (self.owner, self.ref)
        ).fetchall()
        return rows


def query_groups(user_id):
    db = get_db()
    rows = db.execute(
        "SELECT id FROM Groups WHERE user_id = ?",
        (user_id,)
    ).fetchall()
    return [Group(user_id, row['id']) for row in rows]

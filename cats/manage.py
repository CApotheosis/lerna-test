from flask.cli import FlaskGroup

from project import app, db
from project.models import Cats


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    cats = []
    for i in range(1, 21):
        cats.append(
            Cats(
                breed=f"Abyssinian {i}",
                name=f"Jostar {i}",
                age_by_month=i,
                description="The cutest cat you can ever have.",
            )
        )
    db.session.add_all(cats)
    db.session.commit()


if __name__ == "__main__":
    cli()

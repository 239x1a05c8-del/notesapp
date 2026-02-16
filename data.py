from app import db,User,app

with app.app_context():
    user=User(username="Pothan",password="12345")
    db.session.add(user)
    db.session.commit()
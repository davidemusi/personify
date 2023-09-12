from ..utils import db


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Person {self.id}>"
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(model, id):
        return model.query.get_or_404(id)
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()

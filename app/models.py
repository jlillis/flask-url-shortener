from app import db

class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(8), index=True, unique=True)
    destination = db.Column(db.String(120), index=False, unique=False)
    hits = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<ShortURL (id={self.id})>"
    
    def __str__(self):
        return f"<ShortURL (id={self.id})>"
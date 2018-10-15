#coding=utf-8
from main.database import Column, Model, SurrogatePK, db, reference_col, relationship
from main.extensions import bcrypt

class Role(SurrogatePK,Model):
    """A role for a user."""

    __tablename__ = 'roles'

    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# prueba
with app.app_context():
    AlbumSchema = AlbumSchema()
    a = Album(titulo='chuchis', anio=2028, descripcion='chuchis', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    print(Album_Schema.dumps(album) for album in Album.query.all())


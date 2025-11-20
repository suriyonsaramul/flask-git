from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Pokemon

@app.route('/')
def index():
  return render_template('index.html', title='Home Page')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
  pokemons = db.session.scalars(db.select(Pokemon)).all()

  return render_template('pokemon/index.html', title='Pokemon Page', pokemons=pokemons)

@app.route('/pokemon/new', methods=['GET', 'POST'])
def new_pokemon():
  if request.method == 'POST':
    name = request.form.get('pokemon_name')
    description = request.form.get('pokemon_description')
    weight = request.form.get('pokemon_weight')
    height = request.form.get('pokemon_height')
    img_url = request.form.get('pokemon_img_url')
    # print(name)
    pokemon = Pokemon(name=name, description=description, weight=weight, height=height, img_url=img_url)
    db.session.add(pokemon)
    db.session.commit()

    return redirect(url_for('pokemon'))

  return render_template('pokemon/new_pokemon.html', title='New Pokemon Page')

@app.route('/pokemon/<int:id>/detail', methods=['GET', 'POST'])
def pokemon_detail(id):
  pokemon = db.session.get(Pokemon, id)
  return render_template('pokemon/pokemon_detail.html', title='Pokemon Detail Page', pokemon=pokemon)
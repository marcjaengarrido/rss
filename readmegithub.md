# README ITERACIÓ 3
### ENUNCIAT
> Crear un fitxer README.md (markdown baby!) a l'arrel del projecte (és a dir, al mateix nivell que app.py) amb les instruccions per a desplegar l'aplicatiu. Ha d'incloure les instruccions de l'entorn virtual i com iniciar l'aplicatiu. També ha d'incloure com fer servir el mode remot (on es fa servir l'XML directament de la web de la vanguardia) o local (on es fa servir el XML descarregat). El README ha d'incloure algun enllaç (per exemple, a la doc de flask, o una web on expliqui que són els entorns virtuals...).

### INDEX

1. [Inicialització i ús d'un entorn virtual (venv)](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/readme.md#1-inicialitzaci%C3%B3-i-%C3%BAs-dun-entorn-virtual-venv)
2. [Execució del programari](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/readme.md#2-execuci%C3%B3-del-programari)
3. [Modes: remot i local](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/readme.md#3-modes-remot-i-local)
* [ERRORS](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/readme.md#errors-como-odio-los-errores)

### DOCUMENTACIÓ REAL

![GIF flask](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/allhailflask.gif?raw=true)

#### 1. Inicialització i ús d'un entorn virtual (venv)

L'objectiu d'un entorn virtual és principalment crear, per dir-ho d'alguna forma, una nova "instancia" de python. En aquest lloc podem tenir paquest diferents als que tenim per defecte. En comparació es podría considerar com una nova dimensió de python.

El procés d'activació es bastant senzill. Primer executarem la seguent comanda al directori on volguem fer servir l'entorn. Aquesta será l'encarregada de crear un directori amb tot el que necessita venv: 

Amb linux:
* `python3 -m venv .venv`

Amb windows:
* `python -m venv .venv`


Ara ho hem d'activar. Bàsicament el que fa aquesta "activació" (les comandes a continuació) es re definir variables temporals de la terminal, modificant rutes i/o el mateix prompt:

Amb linux:
* `source .venv/bin/activate`

Amb Windows:
* `.\.venv\bin\Activate.ps1` <!-- El de el enunciado no me iba -->

I boom, ja hauriem de ser-hi dins. Si veiem un `(.venv)` a l'inici del nostre prompt, és que tot ha anat bé.

![Foto terminal venv activado](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/venv.png?raw=true)

Si volem tornar a la nostra terminal de tota la vida podem o bé petar el procés de la terminmal actual o fer servir la comanda `deactivate`:

![Foto terminal venv deactivate](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/deactivate.png?raw=true)

Ara que tenim el nostre entorn virtual, ens podem facilitar una mica la vida. Podem descarregar l'extensió anomenada [Python Environment Manager](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager) amb l'objectiu de facilitar l'administració d'entorns virtuals. Mira que bonic:

![Extensió Python Environment Manager](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/pythonenvextension.png?raw=true)

#### 2. Execució del programari

Abans s'executar el script hem d'instalar els paquets requerits pel mateix.

Els que necessitem son [feedparser](https://pypi.org/project/feedparser/) i [flask](https://pypi.org/project/Flask/):

```
pip install feedparser
pip install flask
```

![Instalació feedparser](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/installfeedparser.png?raw=true)

![Instalació flask](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/installflask.png?raw=true)

(En veritat hi han més, però els podem instalar fàcilment amb la seguent comanda gràcies a que ja en tenim un arxiu `requirements.txt` preparat)
```
pip install -r requirements.txt
```

Iniciar el programa és molt fàcil. Obrim la ruta on es troba el nostre arxiu `app.py` i executem la comanda `flask run` i ja ho hem encés

![Execució del programari](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/flaskrun.png?raw=true)

#### 3. Modes: remot i local

Al codi podem veure clarament que tenim dos formes d'agafar les dades.

![Remot Local Codi](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/remotlocal.png?raw=true)

Segons la [documentació de feedparser](https://pythonhosted.org/feedparser/introduction.html), podem obtenir el xml de pràcticament qualsevol lloc, ja siguin arxius locals, remots o fins i tot cadenes de text. Així que simplement, el que fem al codi és o seleccionar una ruta local amb els nostres arxius i secció depenent d'una variable o ruta remota (domini [lavanguardia.com](https://www.lavanguardia.com)) al seu rss on la ruta també compta amb la nostra variable de secció.

![Documentació feedparser](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/feedparser.png?raw=true)


### ERRORS (COMO ODIO LOS ERRORES)

CORS. Los servidores (a pesar de ser por cuestiones de seguridad) últimamente se han vuelto muy 'picky'. CORS és el ejemplo de ello. De lo que me quejo especificamente es algo conocido como Access-Control-Allow-Origin. Básicamente de lo que trata es simplemente que un servidor puede escoger si permitir a otros servidores acceder a mis archivos públicos desde URLs externos o no. El input y botón para buscar en mi navbar mira si existe el rss del tema introducido en la vanguardia y en caso de existir abriría su pestaña, cargando xml remoto. Para hacer eso, hacía una petición al rss en cuestión. Por alguna razón, después de buscar entre 1 y 3 veces, me saltaba el error de CORS que sería el siguiente:

![Error Cors](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/errorcors.png?raw=true)


No sé por que, por alguna razón quería hacerle captura y ya no me volvió a aparecer. Menos mal.

![Página Funcionando Correctamente](https://github.com/marcjaengarrido/daw/blob/main/m4/uf3/flask/consolacors.png?raw=true)

Mi intención era descargar el [proxy cors-anywhere de Rob--W](https://github.com/Rob--W/cors-anywhere/) y seguir el proceso. Básicamente lo que hace esto es hacer de intermediario (sería el servidor, heroku en este caso) entre nosotros y la vanguardia y, por así decirlo, canaliza las respuestas hacia nosotros. De esta forma, la respuesta está permitida por la vanguardia y, al mismo tiempo, nosotros no usamos el método `mode: 'no-cors'` que, por si no se sabía, [hace que la página no pueda ver la respuesta de la petición](https://developer.mozilla.org/en-US/docs/Web/API/Request/mode#no-cors) (`dice 'In addition, JavaScript may not access any properties of the resulting Response.'`), volviendose inútil para nuestra situación.

```
git clone https://github.com/Rob--W/cors-anywhere.git
cd cors-anywhere/
npm install
heroku create
git push heroku master
```

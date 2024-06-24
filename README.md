## Installation

Mettez vous dans le dossier ou vous souhaitez recevoir le projet puis effectuez cette commande:
```bash
git clone https://github.com/Varian99/django.git
```
A la racine du projet, lancez la commande:
(Il est conseillé de créer un environnement virtuel python pour le projet car il y a beaucoup de packages, et notamment une version ancienne de numpy)
```bash
pip install -r requirements
```

## Exécution

Pour exécuter le projet lancez ces commandes à la racine du projet:
```bash
cd multilang_site
python manage.py runserver
```
Vous devriez être en mesure de vous connecter au site via cette URL http://127.0.0.1:8000/fr/
A partir d'ici vous pouvez naviguer et tester les fonctionnalités du site. Le changement de langue s'effectue avec le bouton en haut à gauche de la page, le changement de langue se fait de Français - Anglais / Anglais Français.
Pour le chatbot, il faut cliquer sur le bouton en haut à droite de la page, il faut patienter un peu pour avoir une réponse, cette réponse est d'ailleurs étrange, celà est du au fait que j'ai installé un GPT-2 en local car je n'ai pas la version payante d'openAI pour utiliser chatGPT en ligne.

## Administration
L'esapce administration est l'espace de base proposé par django où j'ai ajouté la possibilité de mettre des articles, vous pouvez vous y connecter sur cette URL: http://127.0.0.1:8000/fr/admin/
- **Login:** admin
- **Password:** 1

PS: le site ne peut pas être déployé sur render.com car il demande trop de ressources du fait de GPT-2 en local, par ailleurs je n'ai pas réussi à implémenter le RAG.

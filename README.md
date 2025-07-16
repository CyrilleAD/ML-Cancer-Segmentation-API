# Medical Image Segmentation API

🏥 **API de Segmentation d'Images Médicales** utilisant un modèle U-Net pour la détection et segmentation de cellules cancéreuses.

## 🚀 Fonctionnalités

- ✅ **API REST** avec FastAPI
- ✅ **Modèle U-Net** pour segmentation médicale (6 classes)
- ✅ **Interface Swagger** pour tests interactifs
- ✅ **Déploiement Heroku** prêt
- ✅ **Visualisation** des résultats de segmentation
- ✅ **Support TensorFlow CPU** optimisé

## 📁 Structure du Projet

```
ML-Cancer-Segmentation-API/
├── api.py                 # Application FastAPI principale
├── model_definition.py    # Architecture du modèle U-Net
├── test_api.py           # Script de test avec visualisation
├── requirements.txt      # Dépendances Python
├── runtime.txt          # Version Python pour Heroku
├── Procfile            # Configuration Heroku
├── deploy_setup.py     # Script d'aide au déploiement
├── .gitignore         # Fichiers à ignorer
└── README.md          # Documentation
```

## 🛠️ Installation

### Prérequis
- Python 3.9+
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

### 1. Démarrer l'API

```bash
uvicorn api:app --reload
```

L'API sera accessible sur `http://127.0.0.1:8000`

### 2. Interface Swagger UI

Accédez à `http://127.0.0.1:8000/docs` pour tester l'API interactivement.

### 3. Test avec Python

```bash
python test_api.py
```

### 4. Test avec cURL

```bash
curl -X POST "http://127.0.0.1:8000/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@testimg.jpg"
```

## 📊 API Endpoints

### POST `/`
- **Description**: Segmentation d'image médicale
- **Input**: Fichier image (JPEG, PNG)
- **Output**: Prédictions JSON avec 6 classes de segmentation

**Exemple de réponse**:
```json
{
  "prediction": "[[[[0.1, 0.2, 0.3, 0.15, 0.05, 0.2], ...]]]"
}
```

## 🧠 Modèle

- **Architecture**: U-Net
- **Input**: Images 256x256x3
- **Output**: 6 classes de segmentation
- **Framework**: TensorFlow/Keras
- **Optimisation**: CPU

### Classes de Segmentation
1. Classe 0: Arrière-plan
2. Classe 1: Cellules normales
3. Classe 2: Cellules suspectes
4. Classe 3: Cellules cancéreuses
5. Classe 4: Nécrose
6. Classe 5: Inflammation

## 🚀 Déploiement Heroku

### Méthode 1: Script automatique
```bash
python deploy_setup.py
```

### Méthode 2: Manuel
```bash
# 1. Initialiser Git
git init
git add .
git commit -m "Initial commit"

# 2. Créer l'app Heroku
heroku create your-app-name

# 3. Déployer
git push heroku main
```

## 📈 Visualisation des Résultats

Le script `test_api.py` génère automatiquement :
- Image originale
- 6 masques de segmentation (une par classe)
- Seuillage configurable
- Sauvegarde en haute résolution

## 🔧 Technologies Utilisées

- **FastAPI**: Framework web moderne
- **TensorFlow**: Deep learning
- **OpenCV**: Traitement d'images
- **Matplotlib**: Visualisation
- **Uvicorn/Gunicorn**: Serveurs ASGI/WSGI
- **Heroku**: Plateforme de déploiement

## ⚠️ Limitations

- Modèle entraîné sur des données spécifiques
- Optimisé pour CPU (pas GPU)
- Taille d'image fixe (256x256)
- 6 classes prédéfinies

## 🔮 Améliorations Futures

- [ ] Support GPU
- [ ] Modèles multiples
- [ ] API de réentraînement
- [ ] Métriques de confiance
- [ ] Authentification
- [ ] Cache Redis
- [ ] Monitoring

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Distribué sous licence MIT. Voir `LICENSE` pour plus d'informations.

## 📞 Contact

**Dady Akrou Cyrille** - [@CyrilleAD](https://github.com/CyrilleAD)

Lien du projet: [https://github.com/CyrilleAD/ML-Cancer-Segmentation-API](https://github.com/CyrilleAD/ML-Cancer-Segmentation-API)

---

⭐ **N'hésitez pas à donner une étoile si ce projet vous a aidé !**
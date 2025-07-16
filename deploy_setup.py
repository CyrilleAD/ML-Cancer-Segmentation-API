#!/usr/bin/env python3
"""
Script pour préparer le déploiement Heroku
Basé sur la transcription de la vidéo YouTube
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Succès")
            if result.stdout:
                print(result.stdout)
        else:
            print(f"❌ {description} - Erreur")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de '{command}': {e}")
        return False
    return True

def main():
    print("🚀 Préparation du déploiement Heroku")
    print("Basé sur la vidéo YouTube 'Medical Image Segmentation API'")
    
    # Vérifier si nous sommes dans le bon répertoire
    if not os.path.exists('api.py'):
        print("❌ Erreur: api.py non trouvé. Assurez-vous d'être dans le bon répertoire.")
        sys.exit(1)
    
    # Initialiser Git si nécessaire
    if not os.path.exists('.git'):
        run_command('git init', 'Initialisation du repository Git')
    
    # Ajouter tous les fichiers
    run_command('git add .', 'Ajout des fichiers au repository')
    
    # Commit initial
    run_command('git commit -m "Initial commit - Medical Image Segmentation API"', 'Commit initial')
    
    # Vérifier le statut Git
    run_command('git status', 'Vérification du statut Git')
    
    print("\n📋 Étapes suivantes pour le déploiement Heroku:")
    print("1. heroku login")
    print("2. heroku create your-app-name")
    print("3. git push heroku master")
    print("\n⚠️  N'oubliez pas: gunicorn doit être dans requirements.txt !")
    print("\n🎯 Projet prêt pour le déploiement !")

if __name__ == "__main__":
    main()
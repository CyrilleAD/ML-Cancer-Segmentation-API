import requests
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt

def test_api():
    # URL de l'API
    url = "http://127.0.0.1:8000/"
    
    # Charger l'image de test
    image_path = "testimg.jpg"
    
    # Envoyer la requête
    with open(image_path, "rb") as f:
        files = {"file": ("testimg.jpg", f, "image/jpeg")}
        response = requests.post(url, files=files)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # Parser la réponse JSON
        result = response.json()
        prediction_str = result["prediction"]
        prediction = json.loads(prediction_str)
        
        # Convertir en numpy array
        prediction_array = np.array(prediction)
        print(f"Prediction shape: {prediction_array.shape}")
        
        # Charger l'image originale pour affichage
        original_image = cv2.imread(image_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
        
        # Créer la visualisation
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # Afficher l'image originale
        axes[0, 0].imshow(original_image)
        axes[0, 0].set_title("Image Originale")
        axes[0, 0].axis('off')
        
        # Afficher les 6 classes de segmentation
        class_names = ["Classe 0", "Classe 1", "Classe 2", "Classe 3", "Classe 4", "Classe 5"]
        
        for i in range(6):
            row = (i + 1) // 3
            col = (i + 1) % 3
            
            # Extraire la prédiction pour cette classe
            class_prediction = prediction_array[0, :, :, i]
            
            # Appliquer un seuil
            threshold = 0.3
            binary_mask = (class_prediction > threshold).astype(np.uint8) * 255
            
            axes[row, col].imshow(binary_mask, cmap='gray')
            axes[row, col].set_title(f"{class_names[i]} (seuil: {threshold})")
            axes[row, col].axis('off')
        
        plt.tight_layout()
        plt.savefig('segmentation_results.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Segmentation completed successfully!")
    else:
        print(f"Erreur: {response.text}")

if __name__ == "__main__":
    test_api()